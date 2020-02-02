import csv 
import json 

json_file = open('all.json', mode='r', encoding='utf-8')
csv_file = open('all.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(csv_file)
data = json.load(json_file)

sheet_title = data[0].keys()
content_list = [dict.values() for dict in data]

csv_writer.writerow(sheet_title)
csv_writer.writerows(content_list)

json_file.close()
csv_file.close()