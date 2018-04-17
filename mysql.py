import pymysql
import csv
import re

def pattern_and_acc_num_from_database():
    '''Получаем pattern и account_number из таблицы базы данных
       в виде кортежей
    '''
    conn = pymysql.connect("127.0.0.1","root","890","playground")
    cur = conn.cursor()
    mys = ("""
            select pattern, account_number
            from catalog
        """)
    cur.execute(mys)
    return cur.fetchall()
    
values_from_database = pattern_and_acc_num_from_database()  


def create_list_from_csv(csvfile):
    global data_list
    reader = csv.reader(csvfile, delimiter=';')
    data_list = []
    for line in reader:
        data_list.append(line)
    
#читаем csv файл и получаем двумерный массив data_list
with open('csv_table.csv') as filename:
    create_list_from_csv(filename)
    



def appending_values_to_acc_num():
    for i in data_list:
        if i[4]:
            continue
        for tupl in values_from_database:
            res = re.search(tupl[0], i[2])
            if not res:
                continue
            i[4] = str(tupl[1])
    
appending_values_to_acc_num()

def write_new_data_to_csv():
    with open('csv_table.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for line in data_list:
            writer.writerow(line)

write_new_data_to_csv()
