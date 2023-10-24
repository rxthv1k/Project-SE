from tkinter import*
from tkinter import messagebox
from mysql.connector import *
from MySQLdb import *

studb=connect(host='localhost', user='root', passwd='mysql123', database='studentelections')

admin = Tk()
admin.title("Election system")

admin.minsize(width=1580, height=1080)
admin.maxsize(width=1580, height=1080)

vgslogo = PhotoImage(file = "D:\Project SE\VGS.png")
l1 = Label(admin, image= vgslogo)
l1.pack()

def acwindow():
    ac=Tk()
    ac.title("Add Candidate")

    ac.minsize(width=500, height=200)
    ac.maxsize(width=1580, height=1080)

    Labelname=Label(ac, text="Name:", font=("Calibri", 18))
    Labelname.place(x=30, y=30)

    Labelposition=Label(ac, text="Position:", font=("Calibri", 18))
    Labelposition.place(x=30, y=70)

    Name = StringVar()
    Position = StringVar()

    def add_candidate():
        cur = studb.cursor()
        cur.execute("SELECT * FROM candidatelist")
        candidatelist = list(cur)

        name = nameentry.get()
        position = positionentry.get()

        found = False
        if name:
            if position:
                for pair in candidatelist:
                    if pair[0] == name:
                        found = True
                        messagebox.showerror("Add Candidate", "Candidate already exists")
                        break

                if not found:
                    query = "INSERT INTO candidatelist VALUES ('{0}', '{1}')".format(name, position)
                    cur.execute(query)
                    studb.commit()
                    messagebox.showinfo("Add Candidate", "Candidate added Successfully")
                    ac.destroy()
            else:
                messagebox.showerror("Add Candidate", "Position should not be empty")
        else:
            messagebox.showerror("Add Candidate", "Name should not be empty")


    nameentry=Entry(ac, textvariable=Name, font=("Calibri", 18))
    nameentry.place(x=120, y=30)

    positionentry=Entry(ac, textvariable=Position, font=("Calibri", 18))
    positionentry.place(x=120, y=70)

    acbutton=Button(ac, text=" Add ", font=("Calibri", 14), command=add_candidate)
    acbutton.place(x=300, y=125)

    def ExitButton1():
        ac.destroy()

    backbutton1=Button(ac, text="Back", font=("Times", 14), command=ExitButton1)
    backbutton1.place(x=230, y=130)

    ac.mainloop()

b1=Button(admin, text=" + Add Candidate ", font=("Calibri", 18), command=acwindow)
b1.place(x=1200, y=200)



admin.mainloop()