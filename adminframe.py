from tkinter import*

af=Tk()
af.geometry('500x400')
af.title('VGS Student Elections')

options_frame = Frame(af, bg='#c3c3c3')
options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=1000)


af.mainloop()