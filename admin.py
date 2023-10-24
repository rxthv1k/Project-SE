from tkinter import*
from tkinter import messagebox
from mysql.connector import *
from MySQLdb import *

studb=connect(host='localhost', user='root', passwd='mysql123', database='studentelections' )

admin = Tk()
admin.title("Election system")

admin.minsize(width=800, height=800)
admin.maxsize(width=1580, height=1080)

vgslogo = PhotoImage(file = "D:\Project SE\VGS.png")
l1 = Label(admin, image= vgslogo)
l1.pack()

















#Add Candidate Window
Candidates=[]
Name=StringVar()
Position=StringVar()

def acwindow():
    ac=Tk()
    ac.title("Add Candidate")

    ac.minsize(width=500, height=200)
    ac.maxsize(width=1580, height=1080)

    Labelname=Label(ac, text="Name:", font=("Calibri", 18))
    Labelname.place(x=30, y=30)

    Labelposition=Label(ac, text="Position:", font=("Calibri", 18))
    Labelposition.place(x=30, y=70)

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

b1=Button(admin, text="Add Candidate", font=("Calibri", 18), command=acwindow)
b1.pack()

















#Show Candidates Window
def scwindow():
    sc=Tk()
    sc.title("List of Candidates")

    sc.minsize(width=500, height=200)
    sc.maxsize(width=1580, height=1080)

    for name in Candidates:
        Name = Label(sc, text=name, font=("Calibri", 18))
        Name.pack()

    def ExitButton2():
        sc.destroy()

    backbutton2=Button(sc, text="Back", font=("Times", 14), command=ExitButton2)
    backbutton2.pack()

    sc.mainloop()

b2=Button(admin, text="Show Candidates", font=("Calibri", 18), command=scwindow)
b2.pack()
















#Get Winner Window
def gwwindow():
    gw=Tk()
    gw.title("Get winner")

    gw.minsize(width=500, height=200)
    gw.maxsize(width=1580, height=1080)


    if not Candidates:
        return None
    else:
        pass

    winner = max(Candidates, key=lambda x: x.votes)
    return winner

    def ExitButton3():
        gw.destroy()

    backbutton2=Button(gw, font=("Times", 14), text="Back", command=ExitButton3)
    backbutton2.pack()

    gw.mainloop()

b3=Button(admin, text="Get Winner", font=("Calibri", 18), command=gwwindow)
b3.pack()









#Create User Window
def cuwindow():
    cu=Tk()
    cu.title("Create New User")

    cu.minsize(width=500, height=200)
    cu.maxsize(width=1580, height=1080)

    newuser=StringVar()
    newpass=StringVar()

    uLabel = Label(cu, text="Enter New Username:", font=("Times", 18))
    uLabel.pack()

    uentry = Entry(cu, font=("Calibri", 16), width=20, textvariable=newuser)
    uentry.pack()

    pLabel = Label(cu, text="Enter New Password:", font=("Times", 18))
    pLabel.pack()

    pentry = Entry(cu, font=("Calibri", 16), width=20, textvariable=newpass)
    pentry.pack()

    def Create():
        cur = studb.cursor()
        cur.execute("select* from logindetails")
        adminlist = list(cur)

        u = uentry.get()
        p = pentry.get()

        found = False
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
                    messagebox.showinfo("Create User", "User Created Successfully")
                    cu.destroy()
            else:
                messagebox.showerror("Create User", "Password should not be empty")
        else:
            messagebox.showerror("Create User", "Username should not be empty")

    CreateButton=Button(cu, font=("Times", 14), text="Create", command=Create)
    CreateButton.pack()

    def ExitButton3():
        cu.destroy()

    backbutton2=Button(cu, font=("Times", 14), text="Back", command=ExitButton3)
    backbutton2.pack()

    cu.mainloop()

b4=Button(admin, text="Create New User", font=("Calibri", 18), command=cuwindow)
b4.pack()






Voterslist=['Darshan', 'Sriram']
def voters():
    v=Tk()
    v.title("Voters")

    v.minsize(width=500, height=200)
    v.maxsize(width=1580, height=1080)

    for name in Voterslist:
        Name = Label(v, text=name, font=("Calibri", 18))
        Name.pack()


    def ExitButton3():
        v.destroy()

    backbutton2 = Button(v, font=("Times", 14), text="Back", command=ExitButton3)
    backbutton2.pack()

    v.mainloop()





'''we need to work on this
def avwindow():
    av=Tk()
    av.title("Add Voter")

    av.minsize(width=500, height=200)
    av.maxsize(width=1580, height=1080)

    Labelname=Label(av, text="Name:", font=("Calibri", 18))
    Labelname.place(x=30, y=70)



    Grade=IntVar()

    def add_voter():
        name = nameentry.get()
        if name:
            Voterslist.append(name)

            grade=gradeentry.get()
            if grade:
                Voterslist.append(name)
                messagebox.showinfo("Add Voter", "Added Voter successfully!")

                grade = gradeentry.get()
                if name:
                    Voterslist.append(name)
                    messagebox.showinfo("Add Voter", "Added Voter successfully!")
                    
                    
    gradeentry=Entry(av, textvariable=Grade, font=("Calibri", 18))
    gradeentry.place(x=120, y=70)


    nameentry=Entry(av, textvariable=Name, font=("Calibri", 18))
    nameentry.place(x=120, y=70)

    avbutton=Button(av, text=" Add ", font=("Calibri", 14), command=add_voter)
    avbutton.place(x=380, y=65)

    def ExitButton1():
        av.destroy()

    backbutton1=Button(av, text="Back", font=("Times", 14), command=ExitButton1)
    backbutton1.place(x=230, y=130)

    av.mainloop()

b1=Button(admin, text="Add Voter", font=("Calibri", 18), command=avwindow)
b1.pack()


'''





b5=Button(admin, text="Voters list", font=("Calibri", 18), command=voters)
b5.pack()




ExitButton=Button(admin, text="Exit", font=("Calibri", 18), command=admin.destroy)
ExitButton.pack()

















admin.mainloop()

