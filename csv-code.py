import sqlite3
import codecs
import csv
import os as inner_os
QUERY = '''
    SELECT * FROM commit_comments WHERE commits_count not in ('');
'''
conn = sqlite3.connect('test.db',timeout=180)
cursor = conn.execute(QUERY)
rows = cursor.fetchall()
count = 0
set_count = 0
with open('dataset.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in rows:
        lists = []
        commit_log = row[3].split("\n--\n")
        for commit_array in commit_log:
            writer.writerow([str(row[0]),u"{}".format(commit_array)]) 
        count += int(str(row[2]))
        commit_ids = row[4].replace('"',"").split("\n--\n")
        commit_id_list = []
        for xy in commit_ids:
            if(len(xy) > 0):
                commit_id_list.append(xy)
        commit_id_list = list(set(commit_id_list))
        set_count += len(commit_id_list)
           
conn.close()
print('number of commits in total: ',count)
print('actual id count: ',set_count)