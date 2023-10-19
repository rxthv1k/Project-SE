from tkinter import*
from tkinter import messagebox
from Login import admins

from mysql.connector import*

studb= connect(host="localhost", user="root", passwd="mysql123", database= "studentelections")

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

def acwindow():
    ac=Tk()
    ac.title("Add Candidate")

    ac.minsize(width=500, height=200)
    ac.maxsize(width=1580, height=1080)

    Labelname=Label(ac, text="Name:", font=("Calibri", 18))
    Labelname.place(x=30, y=70)

    def add_candidate():
        name = nameentry.get()
        if name:
            Candidates.append(name)
            messagebox.showinfo("Add candidates", "Added candidates successfully!")
            ac.destroy()

    nameentry=Entry(ac, textvariable=Name, font=("Calibri", 18))
    nameentry.place(x=120, y=70)

    acbutton=Button(ac, text=" Add ", font=("Calibri", 14), command=add_candidate)
    acbutton.place(x=380, y=65)

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

    u=newuser.get()
    p=newpass.get()


    def Create():
        if u in admins:
            messagebox.showerror("Create new user", "Username already exists!")

        else:
            admins[u] = p
            messagebox.showinfo("Create new user", "User Created")
            cu.destroy()

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






def avwindow():
    av=Tk()
    av.title("Add Voter")

    av.minsize(width=500, height=200)
    av.maxsize(width=1580, height=1080)

    Labelname=Label(av, text="Name:", font=("Calibri", 18))
    Labelname.place(x=30, y=70)

    def add_voter():
        name = nameentry.get()
        if name:
            Voterslist.append(name)
            messagebox.showinfo("Add Voter", "Added Voter successfully!")

            grade=gradeentry.get()
            


    gradeentry=Entry(av, textvariable=Name, font=("Calibri", 18))
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








b5=Button(admin, text="Voters list", font=("Calibri", 18), command=voters)
b5.pack()




ExitButton=Button(admin, text="Exit", font=("Calibri", 18), command=admin.destroy)
ExitButton.pack()

















admin.mainloop()

