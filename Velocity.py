#importing library
from tkinter import *
from PIL import ImageTk, Image
import time
import subprocess

w = Tk()

width_of_window = 600
height_of_window = 400
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)  # for hiding titlebar

def new_win():
    # Specify the command to run the other Python file
    cmd = [r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe",
           r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\my_main.py"]
    # Run the other script
    subprocess.run(cmd, check=True, shell=True)


Frame(w, width=620, height=400, bg='#ffffff', highlightthickness=0).place(x=0,y=0)
image_c = ImageTk.PhotoImage(Image.open('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Frame 1.png'))
label1 = Label(w, image=image_c, borderwidth=0, relief="flat")  # decorate it
label1.place(x=150, y=50)

# making animation

image_a = ImageTk.PhotoImage(Image.open('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Group 2.png'))
image_b = ImageTk.PhotoImage(Image.open('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Group 3.png'))




for i in range(3):  # 5loops
    l1 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=277, y=340)
    l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=297, y=340)
    l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=314, y=340)
    l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=329, y=340)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=277, y=340)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=297, y=340)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=314, y=340)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=329, y=340)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=277, y=340)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=297, y=340)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=314, y=340)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=329, y=340)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=277, y=340)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=297, y=340)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=314, y=340)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=329, y=340)
    w.update_idletasks()
    time.sleep(0.5)

w.destroy()
new_win()
w.mainloop()
