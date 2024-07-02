from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1550x730")  # Adjusted to fit the large background image

        # Image 1
        img = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\facialrecognition.webp")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_1bl = Label(self.root, image=self.photoimg)
        f_1bl.place(x=0, y=0, width=500, height=130)

        # Image 2
        img1 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\facialrecognition.webp")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_1bl1 = Label(self.root, image=self.photoimg1)
        f_1bl1.place(x=500, y=0, width=500, height=130)

        # Image 3
        img2 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\facialrecognition.webp")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_1bl2 = Label(self.root, image=self.photoimg2)
        f_1bl2.place(x=1000, y=0, width=500, height=130)
        
        img3 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\bft.jpg")
        img3 = img3.resize((1550, 600), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1550, height=600)

        # Title
        title_lbl = Label(self.root, text="FACE MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=130, width=1530, height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=523 )
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
