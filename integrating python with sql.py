import sqlite3
cn=sqlite3.connect("students.db")
crsr=cn.cursor()
crsr.execute("""create table student1 (rollno integer not null primary key,name varchar(20),class integer)""")
print("Table created ")
qinsert="""insert into student1 values(1001,'arun',12);"""
crsr.execute(qinsert)
print("Values added")
crsr.execute("select*from student1")
result=crsr.fetchall()
print(result)
