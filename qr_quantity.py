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


class QRCode:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Scanner")
        self.root.geometry("800x600")
        self.root.iconbitmap("plogo37_1.ico")

        self.cap = cv2.VideoCapture(0)
        self.qr_decoder = cv2.QRCodeDetector()

        self.canvas = tk.Canvas(root, width=self.cap.get(3), height=self.cap.get(4))
        self.canvas.pack()

        self.scan_qr()
        self.message_label = None
        self.scanned_message = None
        self.scanned_messages = set()
        self.last_scan_time = 0
        self.cooldown_duration = 5  # Cooldown duration in seconds

        self.quantity_button = tk.Button(self.root, text="Quantity", command=self.create_quantity_input)
        self.quantity_button.pack()

    def create_quantity_input(self):
                # Create a new window for quantity input
        self.quantity_window = tk.Toplevel(self.root)
        self.quantity_window.title("Enter Quantity")

                # Create labels and entry field for quantity input
        quantity_label = tk.Label(self.quantity_window, text="Enter Quantity:")
        quantity_label.pack()

        self.quantity_entry = tk.Entry(self.quantity_window)
        self.quantity_entry.pack()

        submit_button = tk.Button(self.quantity_window, text="Submit", command=self.set_quantity)
        submit_button.pack()

    def set_quantity(self):
                # Get the quantity entered in the entry field and update the quantity variable
        try:
            self.quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid quantity.")
        else:
            self.quantity_window.destroy()  # Close the quantity input window

    def add_decoded_message_to_cart(self, decoded_message):
        product_name, _, sp = self.parse_decoded_message(decoded_message)
        if product_name is not None and sp is not None:
            item = Item(product_name, sp, self.quantity)  # Use the quantity variable
            page2.cart.add_item(item)
            page2.Scrolledtext1.configure(state="normal")
            bill_text = "{}\t\t\t\t\t\t\t{}\t\t\t\t\t       \t{}\n".format(product_name, self.quantity, sp)
            page2.Scrolledtext1.insert('insert', bill_text)
            page2.Scrolledtext1.configure(state="disabled")
        else:
            messagebox.showerror("Oops!!", "Invalid decoded message format.", parent=biller)

    def on_closing(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=page1)
        if sure == True:
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
        self.message_label.pack()
        winsound.Beep(800, 500)
        self.add_decoded_message_to_cart(message)

    def draw_bbox(self, frame, bbox):
        bbox = bbox[0]  # Extract the array from the nested array
        for i in range(len(bbox)):
            pt1 = tuple(map(int, bbox[i]))
            pt2 = tuple(map(int, bbox[(i + 1) % 4]))
            cv2.line(frame, pt1, pt2, color=(0, 255, 0), thickness=2)

    def parse_decoded_message(self, decoded_message):
        decoded_parts = decoded_message.split(',')
        if len(decoded_parts) == 3:
            product_name = decoded_parts[0].strip()
            product_qty = decoded_parts[1].strip()
            sp = int(decoded_parts[2].strip())
            return product_name, product_qty, sp
        else:
            return None, None, None


root = Tk()
page1 = QRCode(root)
root.mainloop()
