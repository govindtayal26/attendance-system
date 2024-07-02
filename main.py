from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from  student import student

class FaceRecognitionSystem:
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

        # Background Image
        img3 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\bft.jpg")
        img3 = img3.resize((1550, 600), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1550, height=600)

        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=130, width=1530, height=45)
        
        # Correcting references for images
        img4 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\student.jpeg")
        img4 = img4.resize((220, 170), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 =Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150, y=75, width=220, height=170)
        b11 =Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b11.place(x=150, y=245, width=220, height=30)
        
        img5 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\face.jpg")
        img5 = img5.resize((220, 170), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 =Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=450, y=75, width=220, height=170)
        b12 =Button(bg_img,text="Face Dectector",cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b12.place(x=450, y=245, width=220, height=30)
        
        img6 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\attendance.jpg")
        img6 = img6.resize((220, 170), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 =Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=750, y=75, width=220, height=170)
        b13 =Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b13.place(x=750, y=245, width=220, height=30)
        
        img7 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\help.webp")
        img7 = img7.resize((220, 170), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 =Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1050, y=75, width=220, height=170)
        b14 =Button(bg_img,text="Help desk",cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b14.place(x=1050, y=245, width=220, height=30)
        
        img8 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\train.jpeg")
        img8 = img8.resize((220, 170), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 =Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=150, y=350, width=220, height=170)
        b15 =Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b15.place(x=150, y=520, width=220, height=30)
        
        img9 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\photo.jpeg")
        img9 = img9.resize((220,170), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 =Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=450, y=350, width=220, height=170)
        b16 =Button(bg_img,text="photes",cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b16.place(x=450, y=520, width=220, height=30)
        
        img10 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\developer.jpeg")
        img10 = img10.resize((220, 170), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 =Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=750, y=350, width=220, height=170)
        b17 =Button(bg_img,text="Developer",cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b17.place(x=750, y=520, width=220, height=30)
        
        img11 = Image.open(r"C:\Users\radhi\OneDrive\Documents\Desktop\attendence system\images\exit.jpeg")
        img11 = img11.resize((220, 170), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 =Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=1050, y=350, width=220, height=170)
        b18 =Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b18.place(x=1050, y=520, width=220, height=30)
        
        
        
    def student_details(self):
        self.new_window =Toplevel(self.root)
        self.app=student(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
