import cv2
import tkinter as tk
from PIL import Image, ImageTk


class QRScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Scanner")
        
        self.cap = cv2.VideoCapture(0)
        self.qr_decoder = cv2.QRCodeDetector()
        
        self.canvas = tk.Canvas(root, width=self.cap.get(3), height=self.cap.get(4))
        self.canvas.pack()
        
        self.scan_qr()
        self.message_label = None
        
    def scan_qr(self):
        ret, frame = self.cap.read()
        if ret:
            data, bbox, _ = self.qr_decoder.detectAndDecode(frame)
            
            if bbox is not None and len(bbox) > 0:
                self.draw_bbox(frame, bbox)
                
                if data:
                    self.show_decoded_message(data)
                
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        self.root.after(10, self.scan_qr)
        
    def show_decoded_message(self, message):
        if self.message_label is not None:
            self.message_label.destroy()
            
        self.message_label = tk.Label(self.root, text="Decoded Message: " + message)
        self.message_label.pack()
        l = list(message)
        print(l)
        
    def draw_bbox(self, frame, bbox):
        bbox = bbox[0]  # Extract the array from the nested array
        for i in range(len(bbox)):
            pt1 = tuple(map(int, bbox[i]))
            pt2 = tuple(map(int, bbox[(i+1) % 4]))
            cv2.line(frame, pt1, pt2, color=(0, 255, 0), thickness=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRScannerApp(root)
    root.mainloop()
