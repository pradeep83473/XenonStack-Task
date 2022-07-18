#!C:/Python39/python
import cgi
import mysql.connector
import webbrowser

webbrowser.open('logout.html')

f = cgi.FieldStorage()
fname = f.getvalue("fname")
phone = f.getvalue("phone")
email = f.getvalue("email")
msg = f.getvalue("msg")

con = mysql.connector.connect(user="root",
                              password='',
                              host="localhost",
                              database="contact")
cur = con.cursor()

cur.execute("insert into ppl values(%s,%s,%s,%s)", (fname, phone, email, msg))
con.commit()

cur.close()
con.close()
