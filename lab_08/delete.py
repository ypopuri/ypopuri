#!/usr/bin/python
import pymysql



print("Content-type: text/html\n\n");
db = pymysql.connect(host='localhost',database='lab08',user='root',passwd='Y@shu1234')

import cgi


cursor= db.cursor()
form = cgi.FieldStorage()
name =  form.getvalue('delrec')
print(name + "'s record is Deleted succesfully")
sql = "DELETE FROM student_grades WHERE Fullname= %s"
cursor.execute(sql , (name,))
db.commit()
db.close()
