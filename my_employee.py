# importing the necessary packages 
import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
from PIL import Image, ImageTk
import tkinter as tk
import cv2
import time
import winsound
import calendar
from PIL import Image, ImageDraw, ImageFont
import win32print
import win32ui
import win32con
from PIL import ImageWin

#----------------------------------------------------------------

'''
# Install Pillow (PIL)
pip install Pillow

# Install OpenCV (cv2)
pip install opencv-python

# Install pyaudio (if needed for audio-related tasks, e.g., microphone input)
pip install pyaudio

'''

#creating a window

root = Tk()

root.geometry("1366x768")
root.title(" Velocity: The Retail manager")

#----------------------------------------------------------------
# This is for login purpose 

user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
new_user = StringVar()
new_passwd = StringVar()

#----------------------------------------------------------------
# For billing purposes only

cust_name = StringVar()
cust_num = StringVar()
cust_new_bill = StringVar()
cust_search_bill = StringVar()
bill_date = StringVar()
qty = 0
tsp = 0
#----------------------------------------------------------------

with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
    cur = db.cursor()

#----------------------------------------------------------------

def random_bill_no(stringLength):
    lettersAndDigits = string.ascii_letters.upper() + string.digits
    strr = ''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
    return ('VEL'+strr)

#----------------------------------------------------------------

def valid_phone(phn):
    if re.match(r"[789]\d{9}$",phn):
        return True
    return False

#----------------------------------------------------------------

def login(Event=None):
    global username
    username = user.get()
    password = passwd.get()

    with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
        cur = db.cursor()
    find_user = "SELECT * FROM employee WHERE emp_id=? and password=?"
    cur.execute(find_user,[username, password])
    results = cur.fetchall()
    if results:
        messagebox.showinfo("Login page","The login is successful")
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)
        root.withdraw()
        global biller
        global page2
        biller = Toplevel()
        page2 = bill_window(biller)
        page2.time()
        biller.protocol("WM_DELETE_WINDOW", exitt)
        biller.mainloop()
    else:
        messagebox.showerror("Error", "Incorrect username or password.")
        page1.entry2.delete(0, END)


#----------------------------------------------------------------

def logout():
    sure = messagebox.askyesno("Logout","Are you sure you want to logout",parent=biller)
    if sure == True:
        biller.destroy()
        root.deiconify()
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)
        
#----------------------------------------------------------------


class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0,0)
        top.title(" Velocity: The Retail manager")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(root) #BACKGROUND IMAGE
        self.label1.place(relx=0,rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\employee login page.png"))
        self.label1.configure(image=self.img)


        self.entry1 = Entry(root) #USER NAME
        self.entry1.place(relx=0.395, rely=0.289, width=340, height= 24)
        self.entry1.configure(font="-family {Poppins} -size 16")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)


        self.entry2 = Entry(root) #PASSWORD
        self.entry2.place(relx=0.395, rely=0.539, width=340, height=24)
        self.entry2.configure(font="-family {Poppins} -size 16")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)

        self.button1 = Button(root) # LOGIN BUTTON
        self.button1.place(relx=0.387, rely=0.729, width=315, height=57)
        self.button1.configure(text='Login')
        self.button1.configure(command=login)
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

#----------------------------------------------------------------

class Item:
    def __init__(self,name, price, qty):
        self.product_name = name
        self.price = price
        self.qty = qty

#----------------------------------------------------------------

class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        self.items.pop()

    def remove_items(self):
        self.items.clear()

    def total(self):
        total = 0.0
        for i in self.items:
            total += i.price * i.qty
        return total

    def isEmpty(self):
        if len(self.items) == 0:
            return True

    def allcart(self):
        for i in self.items:
            if (i.product_name in self.dictionary):
                self.dictionary[i.product_name] += i.qty
            else:
                self.dictionary.update({i.product_name:i.qty})

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?",parent=biller)
    if sure == True:
        biller.destroy()
        root.destroy()

#----------------------------------------------------------------

class bill_window:
    def __init__(self, top=None):
        self.result = ''
        top.geometry("1366x768")
        top.resizable(0,0)
        top.title(" Velocity: The Retail manager")
        top.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.l_bill = []

        self.label1 = Label(biller)  #BACKGROUND
        self.label1.place(relx=0,rely=0, width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\bill window page_3.png"))
        self.label1.configure(image=self.img)

        self.message = Label(biller) #USER NAME DISPLAY
        self.message.place(relx=0.075,rely=0.074,width=133, height=30)
        self.message.configure(font="-family {Poppins} -size 16")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")

        self.clock = Label(biller) # FOR CLOCK TIME
        self.clock.place(relx=0.83,rely=0.065,width=114, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 14")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(biller) #CUSTOMER NAME
        self.entry1.place(relx=0.498, rely=0.245, width=230, height= 24)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=cust_name)

        self.entry2 = Entry(biller) #CUSTOMER NUMBER
        self.entry2.place(relx=0.770, rely=0.245, width=240, height=24)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(textvariable=cust_num)

        self.entry3 = Entry(biller) #CUSTOMER SEARCH BILL
        self.entry3.place(relx=0.127,rely=0.245, width=240, height=24)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(textvariable=cust_search_bill)

        self.button1 = Button(biller)# LOG OUT BUTTON
        self.button1.place(relx=0.055, rely=0.143, width=84, height=25)
        self.button1.configure(text='Logout')
        self.button1.configure(command=logout)
        self.button1.configure(font="-family {Poppins SemiBold} -size 16")
        self.button1.configure(relief="flat")
        self.button1.configure(activebackground="#6DCF4B")
        self.button1.configure(foreground="white")
        self.button1.configure(borderwidth='0')
        self.button1.configure(activeforeground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(overrelief="flat")
        self.button1.configure(background="#6DCF4B")

        self.button2 = Button(biller)# SEARCH BUTTON
        self.button2.place(relx=0.314,rely=0.25, width=64, height=21)
        self.button2.configure(text='Search')
        self.button2.configure(command=self.search_bill)
        self.button2.configure(relief="flat")
        self.button2.configure(activeforeground="#ffffff")
        self.button2.configure(activebackground="#6DCF4B")
        self.button2.configure(foreground="white")
        self.button2.configure(borderwidth='0')
        self.button2.configure(cursor="hand2")
        self.button2.configure(overrelief="flat")
        self.button2.configure(background="#6DCF4B")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")


        self.button3 = Button(biller) #TOTAL BUTTON
        self.button3.place(relx=0.07,rely=0.889, width=67, height=23)
        self.button3.configure(text='Total')
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#6DCF4B")
        self.button3.configure(foreground="white")
        self.button3.configure(activeforeground="#ffffff")
        self.button3.configure(borderwidth='0')
        self.button3.configure(cursor="hand2")
        self.button3.configure(background="#6DCF4B")
        self.button3.configure(command=self.total_bill)
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")

        self.button4 = Button(biller) #GENERATE BUTTON
        self.button4.place(relx=0.144,rely=0.889, width=76, height=23)
        self.button4.configure(text='Generate')
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activeforeground="#ffffff")
        self.button4.configure(activebackground="#6DCF4B")
        self.button4.configure(foreground="white")
        self.button4.configure(borderwidth='0')
        self.button4.configure(cursor="hand2")
        self.button4.configure(background="#6DCF4B")
        self.button4.configure(command=self.gen_bill)
        self.button4.configure(font="-family {Poppins SemiBold} -size 11")

        self.button5 = Button(biller) # CLEAR BUTTON
        self.button5.place(relx=0.219,rely=0.889,width=74,height=23)
        self.button5.configure(text='Clear')
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activeforeground="#ffffff")
        self.button5.configure(activebackground="#6DCF4B")
        self.button5.configure(foreground="white")
        self.button5.configure(borderwidth='0')
        self.button5.configure(cursor="hand2")
        self.button5.configure(background="#6DCF4B")
        self.button5.configure(command=self.clear_bill)
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")

        self.button6 = Button(biller) # EXIT BUTTON
        self.button6.place(relx=0.296,rely=0.889,width=72,height=23)
        self.button6.configure(text='Exit')
        self.button6.configure(relief="flat")
        self.button6.configure(activeforeground="#ffffff")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#6DCF4B")
        self.button6.configure(foreground="white")
        self.button6.configure(borderwidth='0')
        self.button6.configure(cursor="hand2")
        self.button6.configure(background="#6DCF4B")
        self.button6.configure(command=exitt)
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")

        self.button7 = Button(biller) #ADD TO CART BUTTON
        self.button7.place(relx=0.0695,rely=0.759,width=75,height=23)
        self.button7.configure(text='Add To Cart')
        self.button7.configure(relief="flat")
        self.button7.configure(overrelief="flat")
        self.button7.configure(activebackground="#6DCF4B")
        self.button7.configure(foreground="white")
        self.button7.configure(activeforeground="#ffffff")
        self.button7.configure(borderwidth='0')
        self.button7.configure(cursor="hand2")
        self.button7.configure(background="#6DCF4B")
        self.button7.configure(command=self.add_to_cart)
        self.button7.configure(font="-family {Poppins SemiBold} -size 10")

        self.button8 = Button(biller) #CLEAR button
        self.button8.place(relx=0.296,rely=0.759,width=73,height=23)
        self.button8.configure(text='Clear')
        self.button8.configure(relief="flat")
        self.button8.configure(activeforeground="#ffffff")
        self.button8.configure(overrelief="flat")
        self.button8.configure(activebackground="#6DCF4B")
        self.button8.configure(foreground="white")
        self.button8.configure(borderwidth='0')
        self.button8.configure(cursor="hand2")
        self.button8.configure(background="#6DCF4B")
        self.button8.configure(command=self.clear_selection)
        self.button8.configure(font="-family {Poppins SemiBold} -size 11")

        self.button9 = Button(biller) #REMOVE BUTTON
        self.button9.place(relx=0.221,rely=0.759,width=68,height=23)
        self.button9.configure(text='Remove')
        self.button9.configure(relief="flat")
        self.button9.configure(activeforeground="#ffffff")
        self.button9.configure(overrelief="flat")
        self.button9.configure(activebackground="#6DCF4B")
        self.button9.configure(foreground="white")
        self.button9.configure(borderwidth='0')
        self.button9.configure(cursor="hand2")
        self.button9.configure(background="#6DCF4B")
        self.button9.configure(command=self.remove_product)
        self.button9.configure(font="-family {Poppins SemiBold} -size 11")

        self.button10 = Button(biller) #QR SCAN BUTTON
        self.button10.place(relx=0.147,rely=0.759,width=68,height=23)
        self.button10.configure(text='QR Scan')
        self.button10.configure(relief="flat")
        self.button10.configure(activeforeground="#ffffff")
        self.button10.configure(overrelief="flat")
        self.button10.configure(activebackground="#6DCF4B")
        self.button10.configure(foreground="white")
        self.button10.configure(borderwidth='0')
        self.button10.configure(cursor="hand2")
        self.button10.configure(background="#6DCF4B")
        self.button10.configure(font="-family {Poppins SemiBold} -size 11")
        self.button10.configure(command=self.qrcode)

        self.button11 = Button(biller) #PRINT BUTTON
        self.button11.place(relx=0.85,rely=0.163,width=56,height=23)
        self.button11.configure(text='Print')
        self.button11.configure(command=self.print_bill)
        self.button11.configure(font="-family {Poppins} -size 16")
        self.button11.configure(relief="flat")
        self.button11.configure(activebackground="#6DCF4B")
        self.button11.configure(foreground="white")
        self.button11.configure(borderwidth='0')
        self.button11.configure(activeforeground="#ffffff")
        self.button11.configure(cursor="hand2")
        self.button11.configure(overrelief="flat")
        self.button11.configure(background="#6DCF4B")
        self.button11.configure(state="disabled")

        text_font = ("Poppins", "8")
        self.combo1 = ttk.Combobox(biller)
        self.combo1.place(relx=0.0693, rely=0.408, width=400,height=26)

        find_category = "SELECT product_cat FROM raw_inventory"
        cur.execute(find_category)
        result1 = cur.fetchall()
        cat = []
        for i in range(len(result1)):
            if result1[i][0] not in cat:
                cat.append(result1[i][0])

        self.combo1.configure(values=cat)
        self.combo1.configure(state="readonly")
        self.combo1.configure(font=text_font)
        self.combo1.option_add("*TCombobox*Listbox.font", text_font)
        self.combo1.option_add("*TCombobox*Listbox.selectBackground","#6DCF4B")
        self.combo1.option_add("*TCombobox*Listbox.selectForeground","white")

        self.combo2 = ttk.Combobox(biller)
        self.combo2.place(relx=0.0693, rely=0.498, width=400, height=26)
        self.combo2.configure(font="-family {Poppins} -size 8")
        self.combo2.option_add("*TCombobox*Listbox.font", text_font)
        self.combo2.configure(state="disabled")

        self.combo3 = ttk.Combobox(biller)
        self.combo3.place(relx=0.0693, rely=0.588, width=400, height=26)
        self.combo3.configure(state="disabled")
        self.combo3.configure(font="-family {Poppins} -size 8")
        self.combo3.option_add("*TCombobox*Listbox.font", text_font)

        self.entry4 = ttk.Entry(biller)
        self.entry4.place(relx=0.0693, rely=0.678, width=400, height=26)
        self.entry4.configure(font="-family {Poppins} -size 8")
        self.entry4.configure(foreground="#000000")
        self.entry4.configure(state="disabled")

        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.415, rely=0.586, width=725, height=275)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        self.combo1.bind("<<ComboboxSelected>>", self.get_category)

    def get_category(self, Event):
        self.combo2.configure(state="readonly")
        self.combo2.set('')
        self.combo3.set('')
        find_subcat = "SELECT product_subcat FROM raw_inventory WHERE product_cat = ?"
        cur.execute(find_subcat, [self.combo1.get()])
        result2 = cur.fetchall()
        subcat=[]
        for i in range(len(result2)):
            if result2[i][0] not in subcat:
                subcat.append(result2[i][0])

        self.combo2.configure(values=subcat)
        self.combo2.bind("<<ComboboxSelected>>", self.get_subcat)
        self.combo3.configure(state="disabled")

    def get_subcat(self, Event):
        self.combo3.configure(state="readonly")
        self.combo3.set('')
        find_subsubcat = "SELECT product_name FROM raw_inventory WHERE product_cat =? and product_subcat=?"
        cur.execute(find_subsubcat, [self.combo1.get(), self.combo2.get()])
        result3 = cur.fetchall()
        pro =[]
        for k in range(len(result3)):
            pro.append(result3[k][0])

        self.combo3.configure(values=pro)
        self.combo3.bind("<<ComboboxSelected>>", self.show_qty)
        self.entry4.configure(state="disabled")

    def show_qty(self, Event):
        self.entry4.configure(state="normal")
        self.qty_label = Label(biller)
        self.qty_label.place(relx=0.0693, rely=0.73, width=78, height=14)
        self.qty_label.configure(font="-family {Poppins} -size 8")
        self.qty_label.configure(anchor="w")
        product_name = self.combo3.get()
        find_qty = "SELECT stock FROM raw_inventory WHERE product_name=?"
        cur.execute(find_qty,[product_name])
        results = cur.fetchone()
        self.qty_label.configure(font="-family {Poppins} -size 8")
        self.qty_label.configure(text="In Stock: {}".format(results[0]))
        self.qty_label.configure(background="#ffffff")
        self.qty_label.configure(foreground="#333333")

    def anal_up(self):
        for i in self.l_bill:
            query = 'SELECT quantity, amount FROM anal WHERE product_name= ?'
            cur.execute(query, [i['product_name'].strip()])
            result = cur.fetchall()
            qty = int(result[0][0])
            amt = int(result[0][1])
            qty += int(i['quantity'])
            amt += int(i['mrp'])
            query1 = 'UPDATE anal SET quantity=?, amount=? WHERE product_name = ?'
            cur.execute(query1, [qty, amt, i['product_name']])
            db.commit()


    cart = Cart()

    def add_to_cart(self):
        global qty,tsp
        self.Scrolledtext1.configure(state="normal")
        strr = self.Scrolledtext1.get('1.0', END)
        if strr.find('Total')==-1:
            product_name = self.combo3.get()
            if product_name != "":
                product_qty = self.entry4.get()
                find_mrp = "SELECT mrp, stock FROM raw_inventory WHERE product_name = ?"
                cur.execute(find_mrp, [product_name])
                result = cur.fetchall()
                mrp = result[0][0]
                stock = result[0][1]
                if product_qty.isdigit() and int(product_qty) > 0:
                    if(stock-int(product_qty)) >= 0:
                        sp = mrp*int(product_qty)
                        product = {
                            "product_name": product_name,
                            "quantity": product_qty,
                            "mrp": sp
                        }
                        self.l_bill.append(product)
                        item = Item(product_name, mrp, int(product_qty))
                        self.cart.add_item(item)
                        self.Scrolledtext1.configure(state="normal")
                        bill_text = "{}\t\t\t\t\t\t\t{}\t\t\t\t\t       \t{}\n".format(product_name, product_qty, sp)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!!", "Out of stock, Check quantity.", parent=biller)
                else:
                    messagebox.showerror("Oops!!", "Please enter valid quantity.", parent=biller)
            else:
                messagebox.showerror("Oops!!", "Please select product.", parent=biller)
        else:
            self.Scrolledtext1.delete('1.0', END)
            new_li = []
            li= strr.split('\n')
            for i in range(len(li)):
                if len(li[i]) != 0:
                    if li[i].find('Subtotal') == -1:
                        new_li.append(li[i])
                    else:
                        break
            for j in range(len(new_li)-1):
                self.Scrolledtext1.insert('insert', new_li[j])
                self.Scrolledtext1.insert('insert', '\n')
            product_name = self.combo3.get()
            if product_name != "":
                product_qty = self.entry4.get()
                find_mrp = "SELECT mrp, stock FROM raw_inventory WHERE product_name =?"
                cur.execute(find_mrp, [product_name])
                result = cur.fetchall()
                mrp = result[0][0]
                stock = result[0][1]
                if product_qty.isdigit():
                    if (stock-int(product_qty))>=0:
                        sp = result[0][0]*int(product_qty)
                        item = Item(product_name, mrp, int(product_qty))
                        product = {
                            "product_name": product_name,
                            "quantity": product_qty,
                            "mrp": sp
                        }
                        self.l_bill.append(product)
                        self.cart.add_item(item)
                        self.Scrolledtext1.configure(state="normal")
                        bill_text = "{}\t\t\t\t\t\t\t{}\t\t\t\t\t    \t{}\n".format(product_name,product_qty,sp)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!!","Out of stock, Check qunatity.", parent=biller)
                else:
                    messagebox.showerror("Oops!!","Please enter valid quantity.", parent=biller)
            else:
                messagebox.showerror("Oops!!","Please select product.", parent=biller)
    def remove_product(self):
        if self.cart.isEmpty()!= True :
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            self.l_bill.pop()
            if strr.find('Total') == -1:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!!", "Please select product.", parent=biller)
                else:
                    self.Scrolledtext1.configure(state="normal")
                    get_all_bill =(self.Scrolledtext1.get('1.0', END).split('\n'))
                    new_string = get_all_bill[:len(get_all_bill)-3]
                    self.Scrolledtext1.delete('1.0', END)
                    for i in range(len(new_string)):
                        self.Scrolledtext1.insert('insert', new_string[i])
                        self.Scrolledtext1.insert('insert', '\n')

                    self.Scrolledtext1.configure(state="disabled")
            else:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!!", "Please select product.", parent=biller)
                else:
                    self.Scrolledtext1.delete('1.0', END)
                    new_li = []
                    li = strr.split('\n')
                    for i in range(len(li)):
                        if len(li[i]) != 0:
                            if li[i].find('Total') == -1:
                                new_li.append(li[i])
                        else:
                            break
                    new_li.pop()
                    for j in range(len(new_li)-1):
                        self.Scrolledtext1.insert('insert', new_li[j])
                        self.Scrolledtext1.insert('insert', '\n')
                    self.Scrolledtext1.configure(state="disabled")

        else:
            messagebox.showerror("Oops!!", "Please select product.", parent=biller)

    def wel_bill(self):
        self.name_message = Text(biller) #CUSTOMER NAME ON BILL
        self.name_message.place(relx=0.494, rely=0.445, width=150, height=23)
        self.name_message.configure(background="#ffffff")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(foreground="#000000")
        self.name_message.configure(font="-family {Verdana} -size 8")

        self.num_message = Text(biller) #CUSTOMER NUMBER ON BILL
        self.num_message.place(relx=0.87, rely=0.444, width=90, height=20)
        self.num_message.configure(font="-family {Verdana} -size 8")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(foreground="#000000")
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(biller) #CUSTOMER BILL NUMBER
        self.bill_message.place(relx=0.476, rely=0.48, width=100, height=21)
        self.bill_message.configure(font="-family {Verdana} -size 8")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(foreground="#000000")
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(biller) #BILL DATE
        self.bill_date_message.place(relx=0.831, rely=0.48, width=90, height=21)
        self.bill_date_message.configure(font="-family {Verdana} -size 8")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(foreground="#000000")
        self.bill_date_message.configure(background="#ffffff")

    def total_bill(self):
        if self.cart.isEmpty():
            messagebox.showerror("Oops!!", "Please select product.", parent=biller)
        else:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total') == -1:
                self.Scrolledtext1.configure(state='normal')
                divider = "\n\n\n" + ("--" * 85)
                self.Scrolledtext1.insert('insert', divider)

                s = 0
                for i in self.l_bill:
                    s += int(i['mrp'])
                sub_total = s

                cgst = 0.025 * sub_total
                sgst = 0.025 * sub_total

                sub_t = '\nSubtotal \t\t\t\t\t\t\t\t\t\t\t\tRs. {:.2f}'.format(sub_total)
                cgst1 = "\nCGST 2.5%\t\t\t\t\t\t\t\t\t\t\t\tRs. {:.2f}".format(cgst)
                sgst1 = "\nSGST 2.5%\t\t\t\t\t\t\t\t\t\t\t\tRs. {:.2f}".format(sgst)

                grand_total = sub_total + cgst + sgst
                total1 = "\nGrand Total\t\t\t\t\t\t\t\t\t\t\t\tRs. {:.2f}".format(grand_total)


                self.Scrolledtext1.insert('insert', sub_t)
                self.Scrolledtext1.insert('insert', cgst1)
                self.Scrolledtext1.insert('insert', sgst1)

                divider2 = "\n" + ("--" * 85)
                self.Scrolledtext1.insert('insert', divider2)
                divider3 = "\n\n\n" + ("--" * 85)
                self.Scrolledtext1.insert('insert', divider3)
                self.Scrolledtext1.insert('insert', total1)
                divider4 = "\n\n\n" + ("--" * 85)
                self.Scrolledtext1.insert('insert', divider4)
                self.Scrolledtext1.configure(state="disabled")

            else:
                return
    state = 1

    def gen_bill(self):
        if self.state == 1:
            strr = self.Scrolledtext1.get('1.0', END)
            self.wel_bill()
            if(cust_name.get()==""):
                messagebox.showerror("Oops!!", "Please enter customer name.", parent=biller)
            elif(cust_num.get()==""):
                messagebox.showerror("Oops!!", "Please enter customer number.", parent=biller)
            elif valid_phone(cust_num.get()) == False:
                messagebox.showerror("Oops!!", "Please enter valid phone number.", parent=biller)
            elif(self.cart.isEmpty()):
                messagebox.showerror("Oops!!", "Please select product.", parent=biller)
            else:

                if strr.find('Total')==-1:
                    self.total_bill()
                    self.gen_bill()
                else:
                    from datetime import date
                    self.button11.configure(state="normal")
                    self.name_message.insert(END, cust_name.get())
                    self.name_message.configure(state="disabled")

                    self.num_message.insert(END, cust_num.get())
                    self.num_message.configure(state="disabled")

                    cust_new_bill.set(random_bill_no(8))

                    self.bill_message.insert(END, cust_new_bill.get())
                    self.bill_message.configure(state="disabled")

                    bill_date.set(str(date.today()))

                    self.bill_date_message.insert(END, bill_date.get())
                    self.bill_date_message.configure(state="disabled")


                    with sqlite3.connect('C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db') as db:
                        cur = db.cursor()
                    my_date = date.today()
                    S = calendar.day_name[my_date.weekday()]
                    insert = ("INSERT INTO bill(Bill_no,date,Customer_Name,Customer_no,bill_details,Employee,Day) VALUES(?,?,?,?,?,?,?)")
                    cur.execute(insert, [cust_new_bill.get(), bill_date.get(), cust_name.get(), cust_num.get(), self.Scrolledtext1.get('1.0', END), username, S])
                    db.commit()

                    for i in self.l_bill:
                        update_qty = "UPDATE raw_inventory SET stock = stock-? WHERE product_name=?"
                        cur.execute(update_qty, [i['quantity'], i['product_name']])
                        db.commit()
                    messagebox.showinfo("Success!!", "Bill Generated", parent=biller)

                    self.state = 0
                    self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")

                    image = Image.open(
                        "C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\bill_template.png")
                    draw = ImageDraw.Draw(image)

                    y = 179

                    font = ImageFont.truetype("arial.ttf", 12)  # Adjust the font and size as needed
                    font1 = ImageFont.truetype("arial.ttf", 10)

                    text_color = (0, 0, 0)

                    text = self.Scrolledtext1.get('1.0', 'end-1c')

                    split_string = text.split('-', 1)

                    if len(split_string) > 1:
                        self.result = '-' + split_string[1]

                    for product in self.l_bill:
                        draw.text((21, y), product["product_name"], fill=text_color, font=font)
                        draw.text((291, y), str(product["quantity"]), fill=text_color, font=font)
                        draw.text((522, y), str(product["mrp"]), fill=text_color, font=font)
                        y += 20

                    text2 = cust_num.get()
                    text3 = cust_name.get()
                    text4 = bill_date.get()
                    self.bill_date = text4
                    text5 = cust_new_bill.get()
                    self.bill_num = text5

                    draw.text((111, 98), text3, fill=text_color, font=font1)
                    draw.text((510, 98), text2, fill=text_color, font=font1)
                    draw.text((463, 123), text4, fill=text_color, font=font1)
                    draw.text((92, 123), text5, fill=text_color, font=font1)

                    result = self.result.replace('\t', '            ')
                    result = result.replace('Subtotal', '     Subtotal')
                    result = result.replace('CGST', '     CGST')
                    result = result.replace('SGST', '     SGST')
                    result = result.replace('Grand Total', '     Grand Total')

                    draw.text((0, y + 30), result, fill=text_color, font=font)

                    output_file = f'C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\bills\\{str(date.today())}_{cust_new_bill.get()}.png'                    # Save the modified image as a new file
                    image.save(output_file)

                    image.close()
                    self.button11.configure(state=ACTIVE)
                    self.anal_up()
                    self.l_bill.clear()
                    return
        else:
            return

    def sun(self):
        self.clear_selection()
        self.clear_bill()
    def  clear_bill(self):
        self.wel_bill()
        self.entry1.configure(state="normal")
        self.entry2.configure(state="normal")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.name_message.configure(state="normal")
        self.num_message.configure(state="normal")
        self.bill_message.configure(state="normal")
        self.bill_date_message.configure(state="normal")
        self.Scrolledtext1.configure(state="normal")
        self.name_message.delete(1.0, END)
        self.num_message.delete(1.0, END)
        self.bill_message.delete(1.0, END)
        self.bill_date_message.delete(1.0, END)
        self.Scrolledtext1.delete(1.0, END)
        self.name_message.configure(state="disabled")
        self.num_message.configure(state="disabled")
        self.bill_message.configure(state="disabled")
        self.bill_date_message.configure(state="disabled")
        self.Scrolledtext1.configure(state="disabled")
        self.cart.remove_items()
        self.state = 1
        self.button7.configure(state=ACTIVE)
        self.button11.configure(state=DISABLED)
        self.l_bill.clear()

    def clear_selection(self):
        self.entry4.delete(0, END)
        self.combo1.configure(state="normal")
        self.combo2.configure(state="normal")
        self.combo3.configure(state="normal")
        self.combo1.delete(0, END)
        self.combo2.delete(0, END)
        self.combo3.delete(0, END)
        self.combo2.configure(state="disabled")
        self.combo3.configure(state="disabled")
        self.entry4.configure(state="disabled")
        try:
            self.qty_label.configure(foreground="#ffffff")
        except AttributeError:
            pass

    def search_bill(self):
        find_bill = "SELECT * FROM bill WHERE bill_no=?"
        cur.execute(find_bill, [cust_search_bill.get().rstrip()])
        results = cur.fetchall()

        if results:
            bill_no = self.entry3.get()
            self.clear_bill()
            self.wel_bill()
            self.entry3.insert(END, bill_no)

            self.button11.configure(state=ACTIVE)
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

            self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
            self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
            self.button7.configure(state=DISABLED)

            self.state = 0

        else:
            messagebox.showerror("Error!!!", "Bill not found.", parent=biller)
            self.entry3.delete(0, END)

    def time(self):
        string = strftime("%H:%m:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


    qr=None

    def qrcode(self):
        root.withdraw()
        self.qr = Toplevel()
        qrobj = QRCode(self.qr)
        self.qr.protocol("WM_DELETE_WINDOW", qrobj.on_closing)
        mainloop()

    def print_bill(self):

        try:
            image_path = f"C:\\Users\\prave\\onedrive\\desktop\\PRAVEENPROJECT\\bills\\{self.bill_date}_{self.bill_num}.png"
            img = Image.open(image_path)
            printer_name = "Canon LBP2900"
            image_width_in_mm = 180
            image_height_in_mm = 297

            # Convert the specified dimensions from millimeters to printer units (1 inch = 25.4 mm)
            image_width_in_printer_units = int(image_width_in_mm * 25.4)
            image_height_in_printer_units = int(image_height_in_mm * 25.4)

            try:
                # Create a Printer DC (Device Context)
                hprinter = win32print.OpenPrinter(printer_name)
                hdc = win32ui.CreateDC()
                hdc.CreatePrinterDC(printer_name)

                # Set up the printer settings for portrait mode
                hdc.StartDoc(image_path)
                hdc.StartPage()

                # Open the PNG image using Pillow
                img = Image.open(image_path)

                # Convert the PIL image to a DIB (Device Independent Bitmap)
                dib = ImageWin.Dib(img)

                # Adjust the x-position to increase the left margin by 10 pixels
                left_margin = 30
                x_position = left_margin

                # BitBlt the image from the DIB to the printer DC, scaling it to the specified dimensions
                dib.draw(hdc.GetHandleOutput(),
                        (x_position, 0, x_position + image_width_in_printer_units, image_height_in_printer_units))

                # End the print job
                hdc.EndPage()
                hdc.EndDoc()

                # Close the printer
                win32print.ClosePrinter(hprinter)
            except Exception as e:
                messagebox.showerror('Oops', 'Cannot identify printer, please ensure proper connection')
            self.sun()

        except:
            messagebox.showerror('Oops', 'Connect printer to print the bill!!!')

class QRCode:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Scanner")
        self.root.geometry("437x382")
        self.root.resizable(0, 0)
        self.root.iconbitmap("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\ICON.ico")

        self.label1 = Label(root)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\Images\\QR WINDOW.png"))
        self.label1.place(x=0, y=0, width=437, height=382)
        self.label1.configure(image=self.img)

        self.cap = cv2.VideoCapture(0)
        self.qr_decoder = cv2.QRCodeDetector()

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 220)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 244)

        self.canvas = tk.Canvas(root, width=self.cap.get(3), height=self.cap.get(4))
        self.canvas.place(x=65, y=23)

        self.entry1 = Entry(root)
        self.entry1.place(x=215, y=282, width=68, height=22)
        self.entry1.configure(background='#ffffff')
        self.entry1.configure(relief='flat')
        self.entry1.configure(font='{Inter Bold} -16')

        self.button1 = Button(root)
        self.button1.place(x=174, y=336, width=72, height=20)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#6DCF4B")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(activeforeground="#ffffff")
        self.button1.configure(background="#6DCF4B")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Submit""")
        self.button1.configure(activeforeground="#000000", command=self.set_quantity)

        self.scan_qr()
        self.message_label = None
        self.scanned_message = None
        self.scanned_messages = set()
        self.last_scan_time = 0
        self.cooldown_duration = 5  # Cooldown duration in seconds

        self.quantity_button = tk.Button(self.root, text="Quantity")
        self.quantity = 1


    def on_closing(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=page2.qr)
        if sure:
            page2.qr.destroy()
            self.cap.release()  # Release the webcam capture
            self.root.destroy()

    def can_scan(self, data):
        current_time = time.time()
        if data in self.scanned_messages and (current_time - self.last_scan_time) < self.cooldown_duration:
            return False
        return True
        
    def scan_qr(self):
        ret, frame = self.cap.read()
        if ret:
            data, bbox, _ = self.qr_decoder.detectAndDecode(frame)
            
            if bbox is not None and len(bbox) > 0:
                self.draw_bbox(frame, bbox)
                
                if data and data != self.scanned_message:
                    self.scanned_message = data
                    self.show_decoded_message(data)
            else:
                self.scanned_message = None

            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        self.root.after(10, self.scan_qr)
        
    def show_decoded_message(self, message):
        if self.message_label is not None:
            self.message_label.destroy()

        self.message_label = tk.Label(self.root, text=message)
        winsound.Beep(800, 500)
        self.add_decoded_message_to_cart(message)
        

    def draw_bbox(self, frame, bbox):
        bbox = bbox[0]  # Extract the array from the nested array
        for i in range(len(bbox)):
            pt1 = tuple(map(int, bbox[i]))
            pt2 = tuple(map(int, bbox[(i+1) % 4]))
            cv2.line(frame, pt1, pt2, color=(0, 255, 0), thickness=2)

    def set_quantity(self):
        try:
            qty = int(self.entry1.get())
            if isinstance(qty, int) and qty > 0:
                page2.Scrolledtext1.configure(state="normal")
                try:
                    ste = page2.l_bill[-1]
                    query = 'SELECT stock, mrp FROM raw_inventory WHERE product_name=?'
                    cur.execute(query, [ste['product_name']])
                    r = cur.fetchall()
                    if r and r[0][0] >= qty:
                        page2.Scrolledtext1.delete('1.0', END)
                        s = page2.l_bill.pop()
                        s['quantity'] = qty
                        s['mrp'] = r[0][1] * qty
                        page2.l_bill.append(s)
                        for i in page2.l_bill:
                            bill_text = "{}\t\t\t\t\t\t\t{}\t\t\t\t\t       \t{}\n".format(i['product_name'], i['quantity'], i['mrp'])
                            page2.Scrolledtext1.insert('insert', bill_text)
                        page2.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Out of stock", "Please check your quantity.")
                except:
                    messagebox.showerror("Oops!", 'Enter a product first!!')
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid quantity.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid quantity (integer).")

    def parse_decoded_message(self, decoded_message):
        decoded_parts = decoded_message.split(',')
        if len(decoded_parts) == 3:
            product_name = decoded_parts[0].strip()
            product_qty = decoded_parts[1].strip()
            sp = int(decoded_parts[2].strip())
            return product_name, product_qty, sp
        else:
            return None, None, None

    def add_decoded_message_to_cart(self, decoded_message):
        product_name, _, sp = self.parse_decoded_message(decoded_message)
        if product_name is not None and sp is not None:
            item = Item(product_name, sp, self.quantity)  # Use the quantity variable
            page2.cart.add_item(item)
            page2.Scrolledtext1.configure(state="normal")
            bill_text = "{}\t\t\t\t\t\t\t{}\t\t\t\t\t       \t{}\n".format(product_name, self.quantity, sp)
            product = {'product_name':product_name, 'quantity': self.quantity, 'mrp': sp}
            page2.l_bill.append(product)
            page2.Scrolledtext1.insert('insert', bill_text)
            page2.Scrolledtext1.configure(state="disabled")
        else:
            messagebox.showerror("Oops!!", "Invalid decoded message format.", parent=biller)


page1 = login_page(root)
root.bind("<Return>", login)
root.mainloop()
