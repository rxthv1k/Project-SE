from tkinter import*
from tkinter import messagebox


login=Tk()
login.title("Election system ")

login.minsize(width=800, height=800)
login.maxsize(width=1580, height=1080)

vgslogo=PhotoImage(file="D:\Project SE\VGS.png")
l1=Label(login, image=vgslogo)
l1.pack()

l1=Label(login, text="Welcome to VGS Student Elections 2023-24", font=("Times", 24))
l1.place(x=130, y=220)

l2=Label(login, text="Username:", font=("Times", 18))
l2.place(x=320, y=350)

uname=StringVar()
e2=Entry(login, font=("Calibri", 16), width=20, textvariable=uname)
e2.place(x=320,y=380)

l3=Label(login, text="Password:", font=("Times", 18))
l3.place(x=320, y=430)

pswd=StringVar()
e3=Entry(login, font=("Calibri", 16), width=20, textvariable=pswd, show="*")
e3.place(x=320,y=460)

admins={"Sasikala": "Sasikala@123"}
def check_uname_and_pwd() :
    u=uname.get()
    p=pswd.get()

    if u in admins:
        if admins[u]==p :
            messagebox.showinfo("Login", "Login successful!")
            login.destroy()
        else:
            messagebox.showerror("Login", "Login failed. Incorrect Password.")
    else:
        messagebox.showerror("Login", "Login failed. Incorrect Username.")

b1=Button(login, text="Login", font=("Calibri", 16), command=check_uname_and_pwd)
b1.place(x=380, y=500)

def toggle_password_visibility():
    if show_password_var.get():
        e3.config(show="")
    else:
        e3.config(show="*")

show_password_var = BooleanVar()
show_password_checkbutton = Checkbutton(login, text="Show Password", font=("Calibri", 16), variable=show_password_var, command=toggle_password_visibility )
show_password_checkbutton.place(x=550,y=455)




login.mainloop()