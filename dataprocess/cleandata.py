import json
import csv 

result = {'中文名': '无信息', '类型': '无信息'}

fw = open('./dataprocess/type.txt', 'w', encoding='utf-8')
with open('./spider/all.json', 'r', encoding='utf-8') as fr:
    str_data = fr.read()
    full_data = json.loads(str_data)
    # print(len(full_data[0]))
    for i in range(len(full_data)):
        for key, value in full_data[i].items():
            if key == '中文名':
                result['中文名'] = value 
                # print(result['中文名'])
            if key == '类型':
                result['类型'] = value
                # print(result['类型'])
        fw.write("{'中文名': '" + result['中文名'] + "', '类型': '" + result['类型'] + "'}\n")
    fw.close()
