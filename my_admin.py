#=======================IMPORTING NECESSARY MODULES=======================
import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from time import strftime
from tkinter import scrolledtext as tkst
from PIL import Image, ImageTk   #pip install Pillow( run this in cmd)
from tkinter import ttk
import os
#==========================================================================

#C:\Users\prave\OneDrive\Documents\dumps\Dump20230906\store_anal.sql

root = Tk()
root.geometry('1366x768')
root.title(' Velocity: The Retail manager(ADMIN)')

#=======================VARIABLES==========================================

user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()

#=======================FUNCTIONS==========================================

with sqlite3.connect('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db') as db:
    cur = db.cursor()

def random_emp_id(stringlength, des):
    Digits = string.digits
    l = "ADMIN"
    if des.upper() == l.upper():
        strr = ''.join(random.choice(Digits) for i in range(stringlength-3))
        return 'ADM'+strr
    else:
        strr = ''.join(random.choice(Digits) for i in range(stringlength - 3))
        return 'EMP'+strr


def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def valid_aadhar(aad):
    if aad.isdigit() and len(aad) == 12:
        return True
    return False

#======================CLASSES==============================================

class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0,0)
        top.title(" Velocity: The Retail manager(ADMIN)")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(root) #BACKGROUND IMAGE
        self.label1.place(relx=0,rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\admin login page.png"))
        self.label1.configure(image=self.img)


        self.entry1 = Entry(root) #USER NAME
        self.entry1.place(relx=0.395, rely=0.289, width=340, height= 24)
        self.entry1.configure(font="-family {Poppins} -size 16")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)


        self.entry2 = Entry(root) # PASSWORD
        self.entry2.place(relx=0.395, rely=0.539, width=340, height=24)
        self.entry2.configure(font="-family {Poppins} -size 16")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)

        self.button1 = Button(root) # LOGIN BUTTON
        self.button1.place(relx=0.387, rely=0.729, width=315, height=57)
        self.button1.configure(text='Login')
        self.button1.configure(command=self.login)
        self.button1.configure(font="-family {Poppins SemiBold} -size 30")
        self.button1.configure(relief="flat")
        self.button1.configure(activeforeground="#ffffff")
        self.button1.configure(activebackground="#00CC8E")
        self.button1.configure(foreground="white")
        self.button1.configure(borderwidth=0)
        self.button1.configure(cursor="hand2")
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(background="#00CC8E")

    def login(self, Event=None):
        username = user.get()
        password = passwd.get()

        with sqlite3.connect('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db') as db:
            cur = db.cursor()
        find_user = "SELECT * FROM employee WHERE emp_id =? and password = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchall()
        if results:
            l = "Admin"
            if (results[0][6].strip()).upper() == l.upper():
                messagebox.showinfo('Login page', 'The Login is successful.')
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)
                root.withdraw()
                global adm
                global page2
                adm = Toplevel()
                page2 = Admin_page(adm)
                adm.protocol("WM_DELETE_WINDOW", exitt)
                adm.mainloop()
            else:
                messagebox.showinfo('Oops!!!','You are not an admin.')
        else:
            messagebox.showinfo('Oops!!!','Invalid Username or Password.')
            page1.entry2.delete(0, END)

def exitt():
    sure = messagebox.askyesno('Exit', 'Are you sure you want to exit.', parent=root)
    if sure==True:
        adm.destroy()
        root.destroy()

def inventory():
    adm.withdraw()
    global inv
    global page3
    inv = Toplevel()
    page3 = Inventory(inv)
    page3.time()
    inv.protocol("WM_DELETE_WINDOW", exitt)
    inv.mainloop()

def employee():
    adm.withdraw()
    global emp
    global page5
    emp = Toplevel()
    page5 = Employee(emp)
    page5.time()
    emp.protocol("WM_DELETE_WINDOW", exitt)
    emp.mainloop()

def invoices():
    adm.withdraw()
    global invoice 
    invoice = Toplevel()
    page7 = Invoice(invoice)
    page7.time()
    invoice.protocol("WM_DELETE_WINDOW", exitt)
    invoice.mainloop()

def analysis():
    adm.withdraw()
    global analyse
    analyse = Toplevel()
    page8 = Analysis(analyse)
    page8.time()
    analyse.protocol("WM_DELETE_WINDOW", exitt)
    analyse.mainloop()


class Admin_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0,0)
        top.title(" Velocity: The Retail manager(ADMIN MODE)")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(adm)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\admin page.png"))
        self.label1.configure(image=self.img)

        self.button1 = Button(adm)  # LOGOUT BUTTON
        self.button1.place(relx=0.04, rely=0.098, width=85, height=30)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(activeforeground="#00CC8E")
        self.button1.configure(background="#FFFFFF")
        self.button1.configure(foreground="#00CC8E")
        self.button1.configure(background="#ffffff")
        self.button1.configure(font="-family {Inter} -size 17")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=self.Logout)

        self.button2 = Button(adm)  # INVENTORY BUTTON
        self.button2.place(relx=0.184, y=313, width=140, height=140)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\inventory.png"))
        self.button2.configure(image=self.img2)
        self.button2.configure(foreground="#333333")
        self.button2.configure(background="#ffffff")
        self.button2.configure(font="-family {Inter light} -size 16")
        self.button2.configure(borderwidth="0")
        self.button2.configure(command=inventory)

        self.button3 = Button(adm)  # EMPLOYEE BUTTON
        self.button3.place(relx=0.36, y=313, width=140, height=140)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\employee.png"))
        self.button3.configure(image=self.img3)
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#333333")
        self.button3.configure(background="#ffffff")
        self.button3.configure(font="-family {Inter light} -size 16")
        self.button3.configure(borderwidth="0")
        self.button3.configure(command=employee)


        self.button4 = Button(adm)  # INVOICE BUTTON
        self.button4.place(relx=0.537, y=313, width=140, height=140)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.img4 = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\invoice.png"))
        self.button4.configure(image=self.img4)
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#333333")
        self.button4.configure(background="#ffffff")
        self.button4.configure(font="-family {Inter light} -size 16")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Invoices""")
        self.button4.configure(command=invoices)


        self.button5 = Button(adm) #ANALYSIS BUTTON
        self.button5.place(relx=0.715, y=313, width=140, height=140)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.img5 = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\sales.png"))
        self.button5.configure(image=self.img5)
        self.button5.configure(activebackground="#ffffff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#333333")
        self.button5.configure(background="#ffffff")
        self.button5.configure(font="-family {Inter light} -size 16")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Sales analysis""")
        self.button5.configure(command=analysis)

    def Logout(self):
        sure = messagebox.askyesno("Logout","Are you sure you want to logout.",parent=adm)
        if sure:
            adm.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class Inventory:
    def __init__(self, top=None):
        top.geometry('1366x768')
        top.resizable(0,0)
        top.title('Velocity: The Retail manager(INVENTORY)')
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(inv)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\inventory page.png"))
        self.label1.configure(image=self.img)

        self.clock = Label(inv) #CLOCK LABEL
        self.clock.place(relx=0.83,rely=0.065,width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(inv) #ENTRY LABEL
        self.entry1.place(relx=0.08, rely=0.351, width=217, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(inv) #SEARCH BUTTON
        self.button1.place(relx=0.253, rely=0.358, width=72, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(activeforeground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(activeforeground="#000000")
        self.button1.configure(command=self.search_product)

        self.button2 = Button(inv) #LOGOUT BUTTON
        self.button2.place(relx=0.055, rely=0.140, width=85, height=30)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#00AB78")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(activeforeground="#ffffff")
        self.button2.configure(background="#00AB78")
        self.button2.configure(font="-family {Poppins SemiBold} -size 17")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(inv) #ADD PRODUCT
        self.button3.place(relx=0.0835, rely=0.497, width=280, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#00AB78")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(activeforeground="#ffffff")
        self.button3.configure(background="#00AB78")
        self.button3.configure(font="-family {Poppins Bold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD PRODUCT""")
        self.button3.configure(command=self.add_product)

        self.button4 = Button(inv) #UPDATE  PRODUCT
        self.button4.place(relx=0.0835, rely=0.572, width=280, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#00AB78")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(activeforeground="#ffffff")
        self.button4.configure(background="#00AB78")
        self.button4.configure(font="-family {Inter} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""UPDATE PRODUCT""")
        self.button4.configure(command=self.update_product)

        self.button5 = Button(inv) #DELETE BUTTON
        self.button5.place(relx=0.0835, rely=0.645, width=280, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#00AB78")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#00AB78")
        self.button5.configure(activeforeground="#ffffff")
        self.button5.configure(font="-family {Inter} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE PRODUCT""")
        self.button5.configure(command=self.delete_product)

        self.button6 = Button(inv) #EXIT BUTTON
        self.button6.place(relx=0.162, rely=0.866, width=70, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#00AB78")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(activeforeground="#ffffff")
        self.button6.configure(background="#00AB78")
        self.button6.configure(font="-family {Inter} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", foregorund="#ffffff")
        self.style.configure("Treeview.Heading", font=('Calibri', 10,'bold'),foreground="#ffffff", background="#00AB78")
        self.style.map("Treeview", background=[('selected', '#00AB78')])

        self.scrollbarx = Scrollbar(inv, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(inv, orient=VERTICAL)
        self.tree = ttk.Treeview(inv)
        self.tree.place(relx=0.329, rely=0.232, width=880, height=550) # table view 
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.on_tree_double_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.307, rely=924, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=924, width=884, height=22)

        self.tree.configure(
            columns=(
                'product_id',
                'product_name',
                'product_cat',
                'product_subcat',
                'stock',
                'mrp',
                'cost_price',
                'vendor_phn',
            )
        )

        self.tree.heading("product_id", text="Product ID", anchor=W)
        self.tree.heading("product_name", text="Name", anchor=W)
        self.tree.heading("product_cat", text="Category", anchor=W)
        self.tree.heading("product_subcat", text="Sub-Category", anchor=W)
        self.tree.heading("stock", text="In Stock", anchor=W)
        self.tree.heading("mrp", text="MRP", anchor=W)
        self.tree.heading("cost_price", text="Cost Price", anchor=W)
        self.tree.heading("vendor_phn", text="Vendor No.", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)
        self.tree.column("#8", stretch=NO, minwidth=0, width=77)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM raw_inventory")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values= (data))

    def search_product(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)['values']:
                val.append(j)
        try:
            to_search = int(self.entry1.get())
        except ValueError:
            messagebox.showerror("Oops!!!", "Invalid product Id.", parent=inv)
        else:
            for search in val:
                if search == to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!!", "Product ID : {}  found.".format(self.entry1.get()), parent=inv)
                    break
            else:
                messagebox.showinfo("Oops!!!", "Product ID : {} not found.".format(self.entry1.get()), parent=inv)

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def on_tree_double_select(self, Event):
        self.sel.clear()
        self.tree.selection_remove(self.tree.selection())

    def delete_product(self):
        val = []
        to_delete = []

        if len(self.sel) != 0:
            sure = messagebox.askyesno("confirm", "Are you sure you want to delete the selected product?",parent=inv)
            if sure:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                for j in range(len(val)):
                    if j % 8 == 0:
                        to_delete.append(val[j])

                for k in to_delete:
                    delete = "DELETE FROM raw_inventory WHERE product_id=?"
                    delete1 = "DELETE FROM anal WHERE product_id=?"
                    cur.execute(delete, [k])
                    cur.execute(delete1, [k])
                    db.commit()

                messagebox.showinfo("Success!!", "Product deleted from database.", parent=inv)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()

        else:
            messagebox.showerror("Error!!!", "Please select a product.", parent=inv)

    def update_product(self):
        if len(self.sel)==1:
            global p_update
            p_update = Toplevel()
            page9 = Update_product(p_update)
            page9.time()
            p_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global valll
            valll = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    valll.append(j)

            page9.entry1.insert(0, valll[1])
            page9.entry2.insert(0, valll[2])
            page9.entry3.insert(0, valll[4])
            page9.entry4.insert(0, valll[5])
            page9.entry6.insert(0, valll[3])
            page9.entry7.insert(0, valll[6])
            page9.entry8.insert(0, valll[7])

            p_update.mainloop()

        elif len(self.sel) == 0:
            messagebox.showerror("Error!!!","Please select a product to update.", parent=inv)
        else:
            messagebox.showerror("Error!!!","Please select only one product to update.",parent=inv)


    def add_product(self):
        global p_add
        global page4
        p_add = Toplevel()
        page4 = add_product(p_add)
        page4.time()
        p_add.mainloop()

    def batch_entry(self):
        os.system("python qr(list_decode_real_time).py")


    def time(self):
        string = strftime("%H:%M:%S:%p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit", "are you sure you want to exit.", parent=inv)
        if sure:
            inv.destroy()
            adm.deiconify()

    def ex2(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit.", parent=p_update)
        if sure:
            self.tree.selection_remove(self.tree.selection())
            p_update.destroy()
            inv.deiconify()


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout.")
        if sure:
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

class add_product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Product")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img =ImageTk. PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Add product page.png"))
        self.label1.configure(image=self.img)

        self.clock = Label(p_add) # Clock
        self.clock.place(relx=0.815, rely=0.065, width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(p_add) #PRODUCT NAME ENTRY
        self.entry1.place(relx=0.148, rely=0.312, width=972, height=30)
        self.entry1.configure(font="-family {Poppins SemiBold} -size 16")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_add) # Category Entry
        self.entry2.place(x = 200, y=350, width=430, height=30)
        self.entry2.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry2.configure(relief="flat")
        self.entry2.configure(background="#ffffff")

        self.r2 = p_add.register(self.testint)

        self.entry3 = Entry(p_add) #Quantity Entry
        self.entry3.place(x=200, y=443, width=430, height=30)
        self.entry3.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry3.configure(relief="flat")
        self.entry3.configure(background="#ffffff")
        self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry4 = Entry(p_add) #Selling Price Entry
        self.entry4.place(x=200,y=539, width=430, height=30)
        self.entry4.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry4.configure(relief="flat")
        self.entry4.configure(background="#ffffff")

        self.entry6 = Entry(p_add) #SubCategory Entry
        self.entry6.place(x=722, y=350, width=430, height=30)
        self.entry6.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry6.configure(relief="flat")
        self.entry6.configure(background="#ffffff")

        self.entry7 = Entry(p_add)
        self.entry7.place(x=722, y=443, width=430, height=30)
        self.entry7.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry7.configure(relief="flat")
        self.entry7.configure(background="#ffffff")

        self.entry8 = Entry(p_add)
        self.entry8.place(x=722, y=539, width=430, height=30)
        self.entry8.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry8.configure(relief="flat")
        self.entry8.configure(validate="key", validatecommand=(self.r2, "%P"))
        self.entry8.configure(background="#ffffff")

        self.button1 = Button(p_add)
        self.button1.place(x=575, y=658, width=60, height=25)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Add""")
        self.button1.configure(command=self.add)

        self.button2 = Button(p_add)
        self.button2.place(x=726, y=658, width=64, height=25)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#00AB78")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#00AB78")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Clear""")
        self.button2.configure(command=self.clearr)

    def pro_id_gen(self):
        with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
            c = db.cursor()
            c.execute("SELECT product_id FROM raw_inventory")
            results = c.fetchall()
            
            if results:
                last_product_id = results[-1][0]
                new_product_id = last_product_id + 1
            else:
                
                new_product_id = 327001
            return new_product_id



    def add(self):
        pid = self.pro_id_gen()
        pqty = self.entry3.get()
        pcat = self.entry2.get()  
        pmrp = self.entry4.get()  
        pname = self.entry1.get()  
        psubcat = self.entry6.get()  
        pcp = self.entry7.get()  
        pvendor = self.entry8.get() 

        if pname.strip():
            if pcat.strip():
                if psubcat.strip():
                    if pqty:
                        if pcp:
                            try:
                                float(pcp)
                            except ValueError:
                                messagebox.showerror("Oops!!","Invalid cost price.", parent=p_add)
                            else:
                                if pmrp:
                                    try:
                                        float(pmrp)
                                    except ValueError:
                                        messagebox.showerror("Oops!!","Invalid MRP.", parent=p_add)
                                    else:
                                        if valid_phone(pvendor):
                                            conn = sqlite3.connect('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db')
                                            cur = conn.cursor()
                                            insert = ("INSERT INTO raw_inventory(product_id,product_name, product_cat, product_subcat, stock, mrp, cost_price, vendor_phn) VALUES(?,?,?,?,?,?,?,?)")
                                            cur.execute(insert, [pid, pname, pcat, psubcat, int(pqty), float(pmrp), float(pcp), pvendor])
                                            insert1 = ("INSERT INTO anal(product_id,product_name, category, subcategory,quantity, amount) VALUES(?,?,?,?,?,?)")
                                            try:
                                                cur.execute(insert1, [pid, pname, pcat, psubcat, 0, 0])
                                            except Exception as e:
                                                str = e
                                                messagebox.showerror('Oops!!', str)
                                            conn.commit()
                                            messagebox.showinfo("Success!!", "Product successfully added in inventory.", parent=p_add)
                                            p_add.destroy()
                                            page3.tree.delete(*page3.tree.get_children())
                                            page3.DisplayData()
                                            p_add.destroy()
                                        else:
                                            messagebox.showerror("Oops!", "Invalid phone number.", parent=p_add)
                                else:
                                    messagebox.showerror("Oops!", "Please enter MRP.", parent=p_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter product cost price.", parent=p_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter product quantity.", parent=p_add)
                else:
                    messagebox.showerror("Oops!", "Please enter product sub-category.", parent=p_add)
            else:
                messagebox.showerror("Oops!", "Please enter product category.", parent=p_add)
        else:
            messagebox.showerror("Oops!", "Please enter product name", parent=p_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False
    
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

class Update_product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Product")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(p_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\update product page.png"))
        self.label1.configure(image=self.img)

        self.clock = Label(p_update)  #CLOCK
        self.clock.place(relx=0.815, rely=0.065, width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(p_update) #PRODUCT_NAME
        self.entry1.place(relx=0.148, rely=0.312, width=972, height=30)
        self.entry1.configure(font="-family {Poppins SemiBold} -size 16")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_update) #category Entry
        self.entry2.place(x=200, y=350, width=430, height=30)
        self.entry2.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry2.configure(relief="flat")

        self.r2 = p_update.register(self.testint)

        self.entry3 = Entry(p_update) #quantity entry
        self.entry3.place(x=200, y=443, width=430, height=30)
        self.entry3.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry4 = Entry(p_update) #SELLING PRICE ENTRY
        self.entry4.place(x=200,y=539, width=430, height=30)
        self.entry4.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry4.configure(relief="flat")


        self.entry6 = Entry(p_update) #subcategory ENTRY
        self.entry6.place(x=722, y=350, width=430, height=30)
        self.entry6.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry6.configure(relief="flat")


        self.entry7 = Entry(p_update)
        self.entry7.place(x=722, y=443, width=430, height=30)
        self.entry7.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry7.configure(relief="flat")


        self.entry8 = Entry(p_update)
        self.entry8.place(x=722,y=539, width=430, height=30)
        self.entry8.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry8.configure(relief="flat")


        self.button1 = Button(p_update)
        self.button1.place(x=575, y=658, width=64, height=25)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Update""")
        self.button1.configure(command=self.update)

        self.button2 = Button(p_update)
        self.button2.place(x=726, y=658, width=64, height=25)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#00AB78")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#00AB78")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Clear""")
        self.button2.configure(command=self.clearr)

    def update(self):
        pqty = self.entry3.get()
        pcat = self.entry2.get()  
        pmrp = self.entry4.get()  
        pname = self.entry1.get()  
        psubcat = self.entry6.get()  
        pcp = self.entry7.get()  
        pvendor = self.entry8.get()  


        if pname.strip():
            if pcat.strip():
                if psubcat.strip():
                    if pqty:
                        if pcp:
                            try:
                                float(pcp)
                            except ValueError:
                                messagebox.showerror("Oops!", "Invalid cost price.", parent=p_update)
                            else:
                                if pmrp:
                                    try:
                                        float(pmrp)
                                    except ValueError:
                                        messagebox.showerror("Oops!", "Invalid MRP.", parent=p_update)
                                    else:
                                        if valid_phone(pvendor):
                                            product_id = valll[0]
                                            with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
                                                cur = db.cursor()
                                            update = (
                                            "UPDATE raw_inventory SET product_name = ?, product_cat = ?, product_subcat = ?, stock = ?, mrp = ?, cost_price = ?, vendor_phn = ? WHERE product_id = ?"
                                            )
                                            cur.execute(update, [pname, pcat, psubcat, int(pqty), float(pmrp), float(pcp), pvendor, product_id])
                                            db.commit()
                                            messagebox.showinfo("Success!!", "Product successfully updated in inventory.", parent=p_update)
                                            valll.clear()
                                            Inventory.sel.clear()
                                            page3.tree.delete(*page3.tree.get_children())
                                            page3.DisplayData()
                                            p_update.destroy()
                                        else:
                                            messagebox.showerror("Oops!", "Invalid phone number.", parent=p_update)
                                else:
                                    messagebox.showerror("Oops!", "Please enter MRP.", parent=p_update)
                        else:
                            messagebox.showerror("Oops!", "Please enter product cost price.", parent=p_update)
                    else:
                        messagebox.showerror("Oops!", "Please enter product quantity.", parent=p_update)
                else:
                    messagebox.showerror("Oops!", "Please enter product sub-category.", parent=p_update)
            else:
                messagebox.showerror("Oops!", "Please enter product category.", parent=p_update)
        else:
            messagebox.showerror("Oops!", "Please enter product name", parent=p_update)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

class Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Employee Management")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(emp)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\employee details  page.png"))
        self.label1.configure(image=self.img)

        self.clock = Label(emp) #CLOCK LABEL
        self.clock.place(relx=0.83, rely=0.065, width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(emp) #ENTRY
        self.entry1.place(relx=0.08, rely=0.351, width=217, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(emp) #SEARCH EMPLOYEE
        self.button1.place(relx=0.253, rely=0.358, width=72, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(activeforeground="#ffffff")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_emp)

        self.button2 = Button(emp) #LOGOUT BUTTON
        self.button2.place(relx=0.055, rely=0.140, width=85, height=30)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#00AB78")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#00AB78")
        self.button2.configure(activeforeground="#ffffff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 17")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(emp) #ADD EMPLOYEE
        self.button3.place(relx=0.0835, rely=0.497, width=280, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#00AB78")
        self.button3.configure(cursor="hand2")
        self.button3.configure(activeforeground="#ffffff")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#00AB78")
        self.button3.configure(font="-family {Poppins Bold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD EMPLOYEE""")
        self.button3.configure(command=self.add_emp)

        self.button4 = Button(emp) #UPDATE EMPLOYEE
        self.button4.place(relx=0.0835, rely=0.572, width=280, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#00AB78")
        self.button4.configure(cursor="hand2")
        self.button4.configure(activeforeground="#ffffff")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#00AB78")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""UPDATE EMPLOYEE""")
        self.button4.configure(command=self.update_emp)

        self.button5 = Button(emp) #DELETE EMPLOYEE
        self.button5.place(relx=0.0835, rely=0.645, width=280, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#00AB78")
        self.button5.configure(cursor="hand2")
        self.button5.configure(activeforeground="#ffffff")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#00AB78")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE EMPLOYEE""")
        self.button5.configure(command=self.delete_emp)

        self.button6 = Button(emp) #EXIT BUTTON
        self.button6.place(relx=0.162, rely=0.866, width=70, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#00AB78")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#00AB78")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(activeforeground="#ffffff")
        self.button6.configure(command=self.Exit)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview",foregorund="#ffffff")
        self.style.configure("Treeview.Heading", font=('Calibri', 10,'bold'),foreground="#ffffff", background="#00AB78")
        self.style.map("Treeview",background=[('selected','#00AB78')])


        self.scrollbarx = Scrollbar(emp, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(emp, orient=VERTICAL)


        self.tree = ttk.Treeview(emp)
        self.tree.place(relx=0.329, rely=0.232, width=880, height=550)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.tree.configure(
            columns=("emp_id","Name","Contact_number","Address","Aadhar_num","Password","Designation","Salary"))
        
        self.tree.heading("emp_id", text="Employee ID", anchor=W)
        self.tree.heading("Name", text="Employee Name", anchor=W)
        self.tree.heading("Contact_number", text="Contact No.", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Aadhar_num", text="Aadhar No.", anchor=W)
        self.tree.heading("Password", text="Password", anchor=W)
        self.tree.heading("Designation", text="Designation", anchor=W)
        self.tree.heading("Salary", text="Salary", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=160)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=170)
        self.tree.column("#5", stretch=NO, minwidth=0, width=120)
        self.tree.column("#6", stretch=NO, minwidth=0, width=100)
        self.tree.column("#7", stretch=NO, minwidth=0, width=77)
        self.tree.column("#8", stretch=NO, minwidth=0, width=70)
        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM employee")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("","end", values=(data))

    def search_emp(self):
        val =[]
        f=0
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)
        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("success!!","Employee ID:{} found".format(self.entry1.get()),parent=emp)
                f=f+1
                break
        if f==0:
            messagebox.showerror("Oops!!", "Employee ID: {} not found.".format(self.entry1.get()), parent=emp)
    
    sel=[]
    def on_tree_select(self,Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_emp(self):
        val=[]
        to_delete=[]

        if len(self.sel)!=0:
            sure = messagebox.askyesno("delete","Are you sure you want to delete selected employee(s)?",parent=emp)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])

                flag = 1

                for k in to_delete:
                    if k=="ADM000":
                        flag=0
                        break
                    else:
                        delete = "DELETE FROM employee WHERE emp_id = ?"
                        cur.execute(delete,[k])
                        db.commit()

                if flag==1:
                    messagebox.showinfo("Succes!!","Employee(s) successfully deleted from the database.",parent=emp)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
                else:
                    messagebox.showerror("Error!!","Cannot delete Admin.")
        else:
            messagebox.showerror("Error!!","please select an employee.", parent=emp)

    def update_emp(self):
        if len(self.sel)==1:
            global e_update
            e_update = Toplevel()
            page8 = Update_Employee(e_update)
            page8.time()
            e_update.protocol("WM_DELETE_WINDOW",self.ex2)
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)

            page8.entry1.insert(0, vall[1])
            page8.entry2.insert(0, vall[2])
            page8.entry3.insert(0, vall[4])
            page8.entry4.insert(0, vall[6])
            page8.entry5.insert(0, vall[3])
            page8.entry6.insert(0, vall[5])
            e_update.mainloop()
        elif len(self.sel) == 0:
            messagebox.showerror("Error", "Please select an employee to update.")
        else:
            messagebox.showerror("Error", "Can only update one employee at a time.")


    def add_emp(self):
        global e_add
        e_add = Toplevel()
        page6 = add_employee(e_add)
        page6.time()
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()


    def ex(self):
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()   

    def ex2(self):
        e_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()  



    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=emp)
        if sure == True:
            emp.destroy()
            adm.deiconify()


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            emp.destroy()
            root.deiconify()
            
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Employee")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Add employee page.png"))
        self.label1.configure(image=self.img)

        self.clock = Label(e_add)
        self.clock.place(relx=0.815, rely=0.065, width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.r1 = e_add.register(self.testint)
        self.r2 = e_add.register(self.testchar)

        self.entry1 = Entry(e_add) #name 
        self.entry1.place(x=196, y=289, width=466, height=30)
        self.entry1.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(e_add) #contact
        self.entry2.place(x=196, y=407, width=466, height=30)
        self.entry2.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_add) #aadhar
        self.entry3.place(x=196, y=558,width=466, height=30)
        self.entry3.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_add)  #designation
        self.entry4.place(x=716, y=289, width=466, height=30)
        self.entry4.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_add) #address
        self.entry5.place(x=716, y=407, width=466, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_add) #password
        self.entry6.place(x=716, y=557,width=466, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.button1 = Button(e_add)
        self.button1.place(x=586, y=658, width=67, height=25)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Add""")
        self.button1.configure(command=self.add)

        self.button2 = Button(e_add)
        self.button2.place(x=716, y=658, width=67, height=25)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#00AB78")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#00AB78")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Clear""")
        self.button2.configure(command=self.clearr)


    def testint(self,val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False
    
    def testchar(self,val):
        if val.isalpha():
            return True
        elif val=="":
            return True
        return False
    
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, self.time)

    def add(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()
        
        if ename.strip():
            if valid_phone(econtact):
                if valid_aadhar(eaddhar):
                    if edes:
                        if eadd:
                            if epass:
                                emp_id = random_emp_id(7,edes)
                                insert =( "INSERT INTO employee(emp_id, Name, Contact_number, Address, Aadhar_num, Password, Designation) VALUES(?,?,?,?,?,?,?)")
                                cur.execute(insert, [emp_id, ename, econtact, eadd, eaddhar, epass, edes])
                                db.commit()
                                messagebox.showinfo("Success!!", "Employee ID: {} successfully added in database.".format(emp_id), parent=e_add)
                                self.clearr()
                            else:
                                messagebox.showerror("Oops!", "Please enter a password.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter address.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter designation.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Please enter employee name.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)


class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Employee")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\update employee page.png"))
        self.label1.configure(image=self.img)

        self.clock = Label(e_update)
        self.clock.place(relx=0.815, rely=0.065, width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

        self.entry1 = Entry(e_update) #name
        self.entry1.place(x=196, y=289, width=466, height=30)
        self.entry1.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(e_update) #contact
        self.entry2.place(x=196,y=407,width=466, height=30)
        self.entry2.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_update) #aadhar
        self.entry3.place(x=196, y=558,width=466, height=30)
        self.entry3.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_update) #designation
        self.entry4.place(x=716, y=289, width=466, height=30)
        self.entry4.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_update) #address
        self.entry5.place(x=716, y=407,width=466, height=30)
        self.entry5.configure(font="-family {Poppins SemiBold} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_update) #password
        self.entry6.place(x=716, y=557, width=466, height=30)
        self.entry6.configure(font="-family {Poppins SemiBold} -size 14")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.button1 = Button(e_update)
        self.button1.place(x=586, y=658, width=67, height=25)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Update""")
        self.button1.configure(command=self.update)

        self.button2 = Button(e_update)
        self.button2.place(x=716, y=658, width=67, height=25)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#00AB78")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#00AB78")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Clear""")
        self.button2.configure(command=self.clearr)

    def update(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        if ename.strip():
            if valid_phone(econtact):
                if valid_aadhar(eaddhar):
                    if edes:
                        if eadd:
                            if epass:
                                emp_id = vall[0]
                                update = ("UPDATE employee SET name=?, Contact_number =?, Address=?, Aadhar_num=?, Password = ?, Designation=? WHERE emp_id=?")
                                cur.execute(update, [ename, econtact, eadd, eaddhar, epass, edes, emp_id])
                                db.commit()
                                messagebox.showinfo("Success!!", "Employee ID: {} successfully updated in database.".format(emp_id), parent=e_update)
                                vall.clear()
                                page5.tree.delete(*page5.tree.get_children())
                                page5.DisplayData()
                                Employee.sel.clear()
                                e_update.destroy()
                            else:
                                messagebox.showerror("Oops!", "Please enter a password.", parent=e_update)
                        else:
                            messagebox.showerror("Oops!", "Please enter address.", parent=e_update)
                    else:
                        messagebox.showerror("Oops!", "Please enter designation.", parent=e_update)
                else:
                    messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=e_update)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_update)
        else:
            messagebox.showerror("Oops!", "Please enter employee name.", parent=e_update)


    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


class Invoice:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Invoices")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(invoice)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\invoice page.png"))
        self.label1.configure(image=self.img)
        
        self.clock = Label(invoice) #clock Label
        self.clock.place(relx=0.83, rely=0.065, width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(invoice) #entry
        self.entry1.place(x=75, y=263, width=215, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(invoice) # search invoice
        self.button1.place(x=325,y=271, width=65, height=25)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(activeforeground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_inv)

        self.button2 = Button(invoice)  # logout button
        self.button2.place(relx=0.055, rely=0.140, width=85, height=30)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#00AB78")
        self.button2.configure(activeforeground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#00AB78")
        self.button2.configure(font="-family {Poppins SemiBold} -size 17")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(invoice) #delete invoice
        self.button3.place(x=92,y=379, width=280, height=30)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#00AB78")
        self.button3.configure(activeforeground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#00AB78")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""DELETE INVOICE""")
        self.button3.configure(command=self.delete_invoice)

        self.button4 = Button(invoice) # exit
        self.button4.place(x=210, y=663, width=62, height=25)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#00AB78")
        self.button4.configure(cursor="hand2")
        self.button4.configure(activeforeground="#ffffff")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#00AB78")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""EXIT""")
        self.button4.configure(command=self.Exit)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview",foregorund="#ffffff")
        self.style.configure("Treeview.Heading", font=('Calibri', 10,'bold'),foreground="#ffffff", background="#00AB78")
        self.style.map("Treeview",background=[('selected','#00AB78')])

        self.scrollbarx = Scrollbar(invoice, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(invoice, orient=VERTICAL)


        self.tree = ttk.Treeview(invoice)
        self.tree.place(relx=0.318, rely=0.231, width=880, height=550)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbarx.place(x=432,y=735, width=871, height=9)

        self.tree.configure(
            columns=(
                "Bill_no",
                "date",
                "Customer_Name",
                "Customer_no",
                "Employee"
            )
        )
        self.tree.heading("Bill_no", text="Bill Number", anchor=W)
        self.tree.heading("date", text="Date", anchor=W)
        self.tree.heading("Customer_Name", text="Customer Name", anchor=W)
        self.tree.heading("Customer_no", text="Customer Phone No.", anchor=W)
        self.tree.heading("Employee", text="Employee Name", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=180)
        self.tree.column("#2", stretch=NO, minwidth=0, width=180)
        self.tree.column("#3", stretch=NO, minwidth=0, width=200)
        self.tree.column("#4", stretch=NO, minwidth=0, width=180)
        self.tree.column("#5", stretch=NO, minwidth=0, width=137)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT Bill_no,date,Customer_Name,Customer_no,Employee FROM bill")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("","end", values=(data))

    sel =[]
    def on_tree_select(self,Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def double_tap(self, Event):
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        bill_num = self.tree.item(item)['values'][0]

        global bill
        bill = Toplevel()
        pg = open_bill(bill)
        bill.mainloop()

    
    def delete_invoice(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected invoice(s)?", parent=invoice)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j % 5 == 0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    delete = "DELETE FROM bill WHERE Bill_no = ?"
                    cur.execute(delete, [k])
                    db.commit()

                messagebox.showinfo("Success!!", "Invoice(s) deleted from database.", parent=invoice)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!", "Please select an invoice", parent=invoice)

    def search_inv(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search == to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Bill Number: {} found.".format(self.entry1.get()), parent=invoice)
                break
        else: 
            messagebox.showerror("Oops!!", "Bill NUmber: {} not found.".format(self.entry1.get()), parent=invoice)


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure :
            invoice.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=invoice)
        if sure :
            invoice.destroy()
            adm.deiconify()


class open_bill:
    def __init__(self, top=None):
        
        top.geometry("765x768")
        top.resizable(0, 0)
        top.title("Bill")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(bill)
        self.label1.place(relx=0, rely=0, width=765, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\Bill_print.png"))
        self.label1.configure(image=self.img)
        
        self.name_message = Text(bill) #name
        self.name_message.place(x=134, y=93, width=150, height=23)
        self.name_message.configure(font="-family {Verdana} -size 8")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(background="#ffffff")

        self.num_message = Text(bill) #number
        self.num_message.place(x=649, y=93, width=90, height=20)
        self.num_message.configure(font="-family {Verdana} -size 8")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(bill) #bill number
        self.bill_message.place(x=114, y=120, width=100, height=19)
        self.bill_message.configure(font="-family {Verdana} -size 8")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(bill) #bill_date
        self.bill_date_message.place(x=598,y=120, width=90, height=18)
        self.bill_date_message.configure(font="-family {Verdana} -size 8")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")


        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(x=26, y=184, width=725, height=768)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        find_bill = "SELECT * FROM bill WHERE Bill_no = ?"
        cur.execute(find_bill, [bill_num])
        results = cur.fetchall()
        if results:
            self.name_message.insert(END, results[0][2])
            self.name_message.configure(state="disabled")
    
            self.num_message.insert(END, results[0][3])
            self.num_message.configure(state="disabled")
    
            self.bill_message.insert(END, results[0][0])
            self.bill_message.configure(state="disabled")

            self.bill_date_message.insert(END, results[0][1])
            self.bill_date_message.configure(state="disabled")

            self.Scrolledtext1.configure(state="normal")
            self.Scrolledtext1.insert(END, results[0][4])
            self.Scrolledtext1.configure(state="disabled")



class Analysis:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title(" Velocity: The Retail manager(ADMIN MODE)")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(analyse)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\sales page.png"))
        self.label1.configure(image=self.img)

        self.button1 = Button(analyse)  # logout button
        self.button1.place(x=71, y=91, width=85, height=30)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#00AB78")
        self.button1.configure(activeforeground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#00AB78")
        self.button1.configure(font="-family {Poppins SemiBold} -size 17")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=self.Logout)

        self.clock = Label(analyse)  # CLOCK LABEL
        self.clock.place(relx=0.83, rely=0.065, width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.button2 = Button(top, text="Week Days",          # WEEKDAYS BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.weekdays)
        self.button2.place(x=215, y=246, width=170, height=30)

        self.button3 = Button(top, text="Category",  # Category (TOP SELLING) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.ts_cat)
        self.button3.place(x=200, y=475, width=170, height=30)

        self.button4 = Button(top, text="Sub-Category",  # sub-Category (TOP SELLING) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.ts_subcat)
        self.button4.place(x=200, y=550, width=170, height=30)

        self.button5 = Button(top, text="Product",  # product (TOP SELLING) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.ts_pro)
        self.button5.place(x=200, y=622, width=170, height=30)

        self.button6 = Button(top, text="Category",  # Category (Inventory Analysis) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.inv_cat)
        self.button6.place(x=590, y=235, width=170, height=30)

        self.button7 = Button(top, text="Sub-Category",  # sub-Category (Inventory Analysis) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.inv_subcat)
        self.button7.place(x=590, y=308, width=170, height=30)

        self.button8 = Button(top, text="Category",  # Category (PROFIT AMOUNT) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.c_w_p)
        self.button8.place(x=585, y=461, width=170, height=30)

        self.button9 = Button(top, text="Sub-Category",  # sub-Category (PROFIT AMOUNT) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.s_w_p)
        self.button9.place(x=585, y=535, width=170, height=30)

        self.button10 = Button(top, text="Product",  # product (PROFIT AMOUNT) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.p_w_p)
        self.button10.place(x=585, y=607, width=170, height=30)

        self.button11 = Button(top, text="Category",  # Category (PROFIT MARGIN) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.cpm)
        self.button11.place(x=1025, y=236, width=170, height=30)

        self.button12 = Button(top, text="Sub-Category",  # sub-Category (PROFIT MARGIN) BUTTON
                              font="-family {Inter} -size 18",
                              relief="flat",
                              overrelief="flat",
                              activebackground="#00CC8E",
                              cursor="hand2",
                              activeforeground="#ffffff",
                              background='#00CC8E',
                              foreground="#ffffff",
                              borderwidth="0",
                              command=self.spm)
        self.button12.place(x=1025, y=310, width=170, height=30)

        self.button13 = Button(top, text="Product",  # product (PROFIT AMOUNT) BUTTON
                               font="-family {Inter} -size 18",
                               relief="flat",
                               overrelief="flat",
                               activebackground="#00CC8E",
                               cursor="hand2",
                               activeforeground="#ffffff",
                               background='#00CC8E',
                               foreground="#ffffff",
                               borderwidth="0",
                               command=self.pmp)
        self.button13.place(x=1025, y=381, width=170, height=30)

        self.button14 = Button(top, text="Employee",  # Employee BUTTON
                               font="-family {Inter} -size 18",
                               relief="flat",
                               overrelief="flat",
                               activebackground="#00CC8E",
                               cursor="hand2",
                               activeforeground="#ffffff",
                               background='#00CC8E',
                               foreground="#ffffff",
                               borderwidth="0",
                               command=self.emp_per)
        self.button14.place(x=1005, y=540, width=170, height=30)

        self.button15 = Button(analyse)  # exit
        self.button15.place(x=1183, y=647, width=62, height=25)
        self.button15.configure(relief="flat")
        self.button15.configure(overrelief="flat")
        self.button15.configure(activebackground="#00AB78")
        self.button15.configure(cursor="hand2")
        self.button15.configure(activeforeground="#ffffff")
        self.button15.configure(foreground="#ffffff")
        self.button15.configure(background="#00AB78")
        self.button15.configure(font="-family {Poppins SemiBold} -size 12")
        self.button15.configure(borderwidth="0")
        self.button15.configure(text="""EXIT""")
        self.button15.configure(command=self.Exit)

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout.", parent=analyse)
        if sure:
            analyse.destroy()
            adm.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

    def time(self):
        string = strftime("%H:%M:%S:%p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def weekdays(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\dic.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def ts_pro(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\ts_pro.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def ts_cat(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\ts_cat.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def ts_subcat(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\ts_subcat.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def inv_cat(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\inv_cat.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def inv_subcat(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\inv_subcat.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def c_w_p(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\category_wise_profit.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def s_w_p(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\subcategory_wise_profit.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def p_w_p(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\product_wise_profit.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def cpm(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\cat_profit_mar.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def spm(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\subcat_profit_mar.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def pmp(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\pro_profit_mar.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def emp_per(self):
        my_main_path = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\praveen\emp_perf.py"
        my_python = r"C:\Users\prave\OneDrive\Desktop\PRAVEENPROJECT\venv\Scripts\python.exe"
        os.system(f'{my_python} {my_main_path}')

    def Exit(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=analyse)
        if sure:
            analyse.destroy()
            adm.deiconify()



page1 = login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()

