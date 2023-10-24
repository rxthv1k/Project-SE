'''
from mysql.connector import *
from MySQLdb import *
from tkinter import messagebox

studb=connect(host='localhost', user='root', passwd='mysql123', database='studentelections' )
cur=studb.cursor()

u="Sidharth"
p="Nivas@9611"

cur.execute("select* from logindetails")
adminlist=list(cur)

for x in adminlist:
    print(x)

found=False
if u:
    if p:
        for pair in adminlist:
            if pair[0] == u:
                found = True
                messagebox.showerror("Create User", "Username already exists")
                break

        if found == False:
            query = "insert into logindetails values('{0}', '{1}')".format(u, p)
            cur.execute(query)
            studb.commit()
            print("User Created")
            messagebox.showinfo("Create User", "User Created Successfully")
    else:
        messagebox.showerror("Create User","Enter Password")
else:
    messagebox.showerror("Create User","Enter Username")'''

from mysql.connector import *
from MySQLdb import *
from tkinter import messagebox

studb=connect(host='localhost', user='root', passwd='mysql123', database='studentelections' )
cur=studb.cursor()

u="Sidharth"
p="Nivas@9611"

cur.execute("select* from logindetails")
adminlist=list(cur)

for x in adminlist:
    print(x)

found=False
if u:
    if p:
        for pair in adminlist:
            if pair[0] == u:
                found = True
                messagebox.showerror("Create User", "Username already exists")
                break

        if found == False:
            query = "insert into logindetails values('{0}', '{1}')".format(u, p)
            cur.execute(query)
            studb.commit()
            print("User Created")
            messagebox.showinfo("Create User", "User Created Successfully")
    else:
        messagebox.showerror("Create User","Enter Password")
else:
    messagebox.showerror("Create User","Enter Username")

