__author__ = "praveen,Gowtham,Bhaskar,Surya"
import os 
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

root = Tk()
root.geometry('1366x768')
root.title('Velocity Retail Manager ')
root.resizable(0,0)
root.iconbitmap('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico')


def ext():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit", parent=root)
    if sure:
        root.destroy()


root.protocol("WM_DELETE_WINDOW", ext)

def emp():
    root.withdraw()

    # Specify the command to run the other Python file
    cmd = [r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe", r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\my_employee.py"]

    # Run the other script
    subprocess.run(cmd, check=True, shell=True)

    root.deiconify()

def adm():
    root.withdraw()
    # Specify the command to run the other Python file
    cmd = [r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe",
           r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\my_admin.py"]

    # Run the other script
    subprocess.run(cmd, check=True, shell=True)
    root.deiconify()

bg = Label(root)
bg.place(relx=-0.09,rely=0, width=1600, height=768)
img =ImageTk.PhotoImage(Image.open('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\login_query page.png'))
bg.configure(image=img)

button1 = Button(root)
button1.place(x=413, y=307, width=160, height=170)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Group 10.png"))
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(root)
button2.place(x=787, y=307, width=160, height=170)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Group 11.png"))
button2.configure(image=img3)
button2.configure(command=adm)

root.mainloop()