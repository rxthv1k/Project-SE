'''import tkinter as tk

def add_button():
    name = entry.get()
    button = tk.Button(root, text=name)
    button.pack()

# Create the main window
root = tk.Tk()
root.title("Name Buttons")

# Create an entry widget for entering names
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Create a button to add names
add_button = tk.Button(root, text="Add Button", command=add_button)
add_button.pack()

# Start the Tkinter event loop
root.mainloop()'''




'''
import tkinter as tk

def show_frame(frame):
    frame.tkraise()

def create_start_page(container, controller):
    start_page = tk.Frame(container)
    label = tk.Label(start_page, text="Start Page")
    label.pack(pady=10, padx=10)
    button = tk.Button(start_page, text="Go to Page One", command=lambda: show_frame(page_one))
    button.pack()
    return start_page

def create_page_one(container, controller):
    page_one = tk.Frame(container)
    label = tk.Label(page_one, text="Page One")
    label.pack(pady=10, padx=10)
    button = tk.Button(page_one, text="Go to Start Page", command=lambda: show_frame(start_page))
    button.pack()
    return page_one

app = tk.Tk()
app.geometry("400x300")

container = tk.Frame(app)
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

start_page = create_start_page(container, app)
page_one = create_page_one(container, app)

show_frame(start_page)

app.mainloop()'''


