#!/usr/bin/env python3
# подключение к постгрес
import psycopg2

conn = psycopg2.connect(
host='77.232.139.236',
port='5432',
database='sano',
user='sano',
password='sano')

cur = conn.cursor()
cur.execute('SELECT * FROM book')
rows = cur.fetchall()
for row in rows:
    for elem in row:
        print ("{:<25}".format(elem), end=' ')
    print ()

conn.commit()   # реальное выполнение команд sql
cur.close()
conn.close()
