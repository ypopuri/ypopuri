#!/usr/bin/env python
import cgi
import cgitb
import pymysql

# Enable CGI error reporting
cgitb.enable()

# Connect to the MySQL database
db = pymysql.connect(host='localhost', user='root', passwd='Y@shu1234', db='lab08')
cursor = db.cursor()

# Retrieve form data
form = cgi.FieldStorage()
Fullname = form.getvalue('Fullname')
Midterm1 = int(form.getvalue('Midterm1'))
Midterm2 = int(form.getvalue('Midterm2'))
Finalexam = int(form.getvalue('Finalexam'))

# Calculate average score
Ave = (Midterm1 + Midterm2 + 2 * Finalexam) / 4

# Insert new record into the database
sql = "INSERT INTO student_grades (Fullname, Midterm1, Midterm2, Finalexam,Ave) VALUES (%s, %s, %s, %s,%s)"
data = (Fullname, Midterm1, Midterm2, Finalexam,Ave)
cursor.execute(sql, data)
db.commit()

# Close the database connection
db.close()

# Redirect back to the index page
print("Location: /home.html")
print("Status: 302 Found")
print()
