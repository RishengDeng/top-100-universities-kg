import jieba
import jieba.posseg as pseg 
import json 


with open('./spider/all.json', 'r', encoding='utf-8') as fr:
    str_data = fr.read()
    full_data = json.loads(str_data)
    fw1 = open('./dataprocess/Name.txt', 'w', encoding='utf-8')
    fw2 = open('./dataprocess/English.txt', 'w', encoding='utf-8')
    fw3 = open('./dataprocess/Abbr.txt', 'w', encoding='utf-8')
    fw4 = open('./dataprocess/Time.txt', 'w', encoding='utf-8')
    fw5 = open('./dataprocess/Type.txt', 'w', encoding='utf-8')
    fw6 = open('./dataprocess/Admin.txt', 'w', encoding='utf-8')
    
    for i in range(len(full_data)):
        for key, value in full_data[i].items():
            if key == '中文名':
                fw1.write("{'中文名': '" + value +"'}\n")
            if key == '英文名':
                fw2.write("{'英文名': '" + value +"'}\n")
            if key == '简称':
                fw3.write("{'简称': '" + value +"'}\n")
            if key == '创办时间':
                # fw4.write("{'创办时间': '" + value[0:4] +"年'}\n")
                fw4.write("{'创办时间': '" + value +"'}\n")
            if key == '类型':
                fw5.write("{'类型': '" + value +"'}\n")
            if key == '主管部门':
                fw6.write("{'主管部门': '" + value +"'}\n")

fw1.close()
fw2.close()
fw3.close()
fw4.close()
fw5.close()
fw6.close()
