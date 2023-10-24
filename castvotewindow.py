from tkinter import *
from tkinter import messagebox

cvw = Tk()
cvw.title("VGS ELECTIONS 2023-24")

cvw.minsize(width=800, height=800)
cvw.maxsize(width=1580, height=1080)

vgslogo = PhotoImage(file="D:\Project SE\VGS.png")
l1 = Label(cvw, image=vgslogo)
l1.pack()

label0 = Label(text="Hi", font=("Ubuntu", 30))
label0.pack()

label1 = Label(text="Welcome to VGS ELECTIONS 2023-24", font=("Ubuntu", 30))
label1.pack()

Candidates=['Sidharth Nivas', 'Rithvik S']
Candidatesdict = {}
for name in Candidates:
    Candidatesdict[name] = 0
print(Candidatesdict)
buttons={}


def increment_counter_button(key):
    increment_counter(key)
    '''messagebox.showinfo("Voting", "Thanks for voting!")
    cvw.destroy()'''
def increment_counter(key):
    Candidatesdict[key] += 1
    print(Candidatesdict)

for key in Candidatesdict.keys():
    vbutton = Button(text=key, font=("Ubuntu", 18), command=lambda k=key: increment_counter_button(k))
    vbutton.pack()

cvw.mainloop()