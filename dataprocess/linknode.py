import json 
import csv 

nodes = []
links = []

name_list = []
english_list = []
abbr_list = []
time_list = []
type_list = []
admin_list = []
# english2_list = []
# time2_list = []
# abbr2_list = []

# central node
nodes.append({'id': '大学', 'class': 'university', 'group': 0, 'size': 22})

# type node
fr = open('./dataprocess/Type.txt', 'r', encoding='utf-8')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in type_list:
            type_list.append(value)
            nodes.append({'id': value, 'class': 'type', 'group': 5,  'size': 18})
            links.append({'source': '大学', 'target': value, 'value': 3})
            links.append({'source': value, 'target': '大学', 'value': 3})
fr.close()

# english node
fr = open('./dataprocess/English.txt', 'r', encoding='utf-8')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in english_list:
            english_list.append(value)
            nodes.append({'id': value, 'class': 'english', 'group': 2,  'size': 15})
fr.close()

# abbr node
fr = open('./dataprocess/Abbr.txt', 'r', encoding='utf-8')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in abbr_list:
            abbr_list.append(value)
            nodes.append({'id': value, 'class': 'abbr', 'group': 3,  'size': 15})
fr.close()

# time node
fr = open('./dataprocess/Time.txt', 'r', encoding='utf-8')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in time_list:
            time_list.append(value)
            nodes.append({'id': value, 'class': 'time', 'group': 4,  'size': 11})
fr.close()

# admin node
fr = open('./dataprocess/Admin.txt', 'r', encoding='utf-8')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in admin_list:
            admin_list.append(value)
            nodes.append({'id': value, 'class': 'admin', 'group': 6,  'size': 11})
fr.close()

# # english2 node
# fr = open('./dataprocess/English.txt', 'r', encoding='utf-8')
# for line in fr.readlines():
#     tmp = line.strip('\n')
#     for key, value in eval(tmp).items():
#         if value not in english2_list:
#             english2_list.append(value)
#             nodes.append({'id': value, 'class': 'english2', 'group': 7,  'size': 13})
# fr.close()

# # abbr2 node
# fr = open('./dataprocess/Abbr.txt', 'r', encoding='utf-8')
# for line in fr.readlines():
#     tmp = line.strip('\n')
#     for key, value in eval(tmp).items():
#         if value not in abbr2_list:
#             abbr2_list.append(value)
#             nodes.append({'id': value, 'class': 'abbr2', 'group': 8,  'size': 13})
# fr.close()

# # time2 node
# fr = open('./dataprocess/Time.txt', 'r', encoding='utf-8')
# for line in fr.readlines():
#     tmp = line.strip('\n')
#     for key, value in eval(tmp).items():
#         if value not in time2_list:
#             time2_list.append(value)
#             nodes.append({'id': value, 'class': 'time2', 'group': 9,  'size': 13})
# fr.close()


with open('./spider/all.json', 'r', encoding='utf-8') as fr:
    str_data = fr.read()
    full_data = json.loads(str_data)
    for i in range(len(full_data)):
        # for key, value in full_data[i].items():
        # name node
        nodes.append({'id': full_data[i]['中文名'], 'class': 'names', 'group': 1, 'size': 20})
        links.append({'source': full_data[i]['类型'], 'target': full_data[i]['中文名'], 'value': 3})
        links.append({'source': full_data[i]['中文名'], 'target': full_data[i]['类型'], 'value': 3})
        # english node
        links.append({'source': full_data[i]['中文名'], 'target': full_data[i]['英文名'], 'value': 3})
        links.append({'source': full_data[i]['英文名'], 'target': full_data[i]['中文名'], 'value': 3})
        # abbr node
        links.append({'source': full_data[i]['中文名'], 'target': full_data[i]['简称'], 'value': 3})
        links.append({'source': full_data[i]['简称'], 'target': full_data[i]['中文名'], 'value': 3})
        # time node
        links.append({'source': full_data[i]['简称'], 'target': full_data[i]['创办时间'], 'value': 3})
        links.append({'source': full_data[i]['创办时间'], 'target': full_data[i]['简称'], 'value': 3})
        # admin node
        links.append({'source': full_data[i]['简称'], 'target': full_data[i]['主管部门'], 'value': 3})
        links.append({'source': full_data[i]['主管部门'], 'target': full_data[i]['简称'], 'value': 3})

fw = open('./html/nodes.json', 'w', encoding='utf-8')
fw.write(json.dumps({'nodes': nodes, 'links': links}, ensure_ascii=False))
fw.close()