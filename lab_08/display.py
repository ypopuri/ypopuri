#!/usr/bin/env python

import pymysql
print("Content-type: text/html\n\n");
connection = pymysql.connect(host='localhost',database='lab08',user='root',password='Y@shu1234')
sql_select_Query = "select * from student_grades"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
#print(records)
for row in records:
	print("<html>")
	print(row[0])
	print(row[4])
	print("</br>")
	print("</html>")
