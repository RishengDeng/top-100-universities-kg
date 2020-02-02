import requests
import json
from bs4 import BeautifulSoup


# open the website and get the content 
def url_open(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    r = requests.get(url, headers = headers)
    return r 

# get the school list
def school_list(filename):
    school = []
    fr = open(filename, 'r', encoding='utf-8')
    lines = fr.readlines()
    for line in lines:
        school.append(line.strip('\n'))
    fr.close()
    return school

if __name__ == "__main__":
    school = school_list('school.txt')
    # print(school)
    result_data = []
    for index in school:
        url = 'https://baike.baidu.com/item/' + index 
        print(url)
        data = url_open(url)
        soup = BeautifulSoup(data.content, 'html.parser', from_encoding='utf-8')
        name_data = []
        value_data = []
        name_node = soup.find_all('dt', class_='basicInfo-item name')
        # print(name_node)
        for i in range(len(name_node)):
            name_data.append(name_node[i].get_text().replace('\xa0', ''))
            # name_data.append(name_node[i].get_text())
            # print(name_data)
        value_node = soup.find_all('dd', class_='basicInfo-item value')
        for i in range(len(value_node)):
            value_data.append(value_node[i].get_text().replace('\n', ''))
            # print(type(value_node[i].get_text().replace('\n', '')))
            # print(value_node[i].get_text().replace('\n', ''))
            # print(value_data)
            # print(type(value_data))
        result = {'中文名': '无信息', '英文名': '无信息', '简称':'无信息','创办时间': '无信息', '类型': '综合', '主管部门': '无信息'}
        for i in range(len(name_data)):
            if name_data[i] == '中文名':
                result['中文名'] = value_data[i]
            if name_data[i] in ['英文名','外文名']:
                result['英文名'] = value_data[i]
            if name_data[i] == '简称':
                result['简称'] = value_data[i]
            if name_data[i] == '创办时间':
                result['创办时间'] = value_data[i]
            if name_data[i] == '类型':
                result['类型'] = value_data[i]
            if name_data[i] == '主管部门':
                result['主管部门'] = value_data[i]
        result_data.append({'中文名': result['中文名'], '英文名': result['英文名'], '简称': result['简称'], '创办时间': result['创办时间'], '类型': result['类型'], '主管部门': result['主管部门']})
        # print('reading the website...')
        # print(result_data)
    fw = open('all.json', 'w', encoding='utf-8')
    fw.write(json.dumps(result_data, ensure_ascii=False))
    fw.close()
    print('complete!')

# link = 'http://www.santostang.com/'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# r = requests.get(link, headers = headers)
# print(r)

# soup = BeautifulSoup(r.text, 'html.parser')
# title = soup.find('h1', class_='post-title').a.text.strip()

# print(title)