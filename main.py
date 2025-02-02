from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import webbrowser
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Image 1
        img = Image.open("Images\my2.jpg") 
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoi1 = ImageTk.PhotoImage(img)
        lb1 = Label(self.root, image=self.photoi1)
        lb1.place(x=0, y=0, width=500, height=130)

        # Image 2
        img1 = Image.open("Images/face.jpg")  
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoi2 = ImageTk.PhotoImage(img1)
        lb2 = Label(self.root, image=self.photoi2)
        lb2.place(x=500, y=0, width=500, height=130)

        # Image 3
        img2 = Image.open("Images/my1.jpg")  
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoi3 = ImageTk.PhotoImage(img2)
        lb3 = Label(self.root, image=self.photoi3)
        lb3.place(x=1000, y=0, width=550, height=130)

        # Image Background
        bg = Image.open("Images/bg.jpg")  
        bg = bg.resize((1530, 710), Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(bg)
        lb_bg = Label(self.root, image=self.photobg)
        lb_bg.place(x=0, y=130, width=1530, height=710)

        title=Label(lb_bg, text="SMART FACE RECOGNITION SYSTEM SOFTWARE", font=("times new roman",35,"bold"), bg="white", fg="darkblue")
        title.place(x=0, y=0,width=1530, height=45)

        self.time_label = Label(title, font=("times new roman", 15, "bold"), bg="white", fg="blue")
        self.time_label.place(x=0, y=0, width=150, height=50)
        self.update_time() 

        #student detail
        sdetail = Image.open("Images/k.jpg")  
        sdetail = sdetail.resize((220, 220), Image.LANCZOS)
        self.stu_d = ImageTk.PhotoImage(sdetail)
        b1=Button(lb_bg, image=self.stu_d,command=self.student_detail, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1=Button(lb_bg, text="Student Detail",command=self.student_detail, cursor="hand2", font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        #Face Detection detail
        faced = Image.open("Images/ml.jpg") 
        faced = faced.resize((220, 220), Image.LANCZOS)
        self.face_d = ImageTk.PhotoImage(faced)
        b1=Button(lb_bg, image=self.face_d, command=self.face_recognition, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)
        b1_1=Button(lb_bg, text="Face Detact", cursor="hand2", command=self.face_recognition, font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        #Attendence detail
        attend = Image.open("Images/attend.jpg")  
        attend = attend.resize((220, 220), Image.LANCZOS)
        self.attend_l = ImageTk.PhotoImage(attend)
        b1=Button(lb_bg, image=self.attend_l, command=self.attendance_data, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)
        b1_1=Button(lb_bg, text="Attendens", cursor="hand2", command=self.attendance_data, font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        #Help detail
        help = Image.open("Images/help.jpg")  
        help = help.resize((220, 220), Image.LANCZOS)
        self.help_l = ImageTk.PhotoImage(help)
        b1=Button(lb_bg, image=self.help_l, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)
        b1_1=Button(lb_bg, text="Help Desk", cursor="hand2", font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)    

        #Train Data
        traind = Image.open("Images/dt.jpg")  
        traind = traind.resize((220, 220), Image.LANCZOS)
        self.traind_l = ImageTk.PhotoImage(traind)
        b1=Button(lb_bg, image=self.traind_l, command=self.train_data, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)
        b1_1=Button(lb_bg, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=600, width=220, height=40)

        #Photos
        photos = Image.open("Images/pho.WEBP")  
        photos = photos.resize((220, 220), Image.LANCZOS)
        self.photos_l = ImageTk.PhotoImage(photos)
        b1=Button(lb_bg, image=self.photos_l, command=self.open_img, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)
        b1_1=Button(lb_bg, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=600, width=220, height=40)

        #Collage Info
        collage = Image.open("Images/clg.png")
        collage = collage.resize((220, 220), Image.LANCZOS)
        self.collage_l = ImageTk.PhotoImage(collage)
        b1=Button(lb_bg, image=self.collage_l, command=lambda: webbrowser.open("https://www.ganpatuniversity.ac.in/"), cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)
        b1_1=Button(lb_bg, text="College Info.", cursor="hand2", command=lambda: webbrowser.open("https://www.ganpatuniversity.ac.in/"), font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=600, width=220, height=40)

        #Exit
        exit = Image.open("Images/exit.png")  
        exit = exit.resize((220, 220), Image.LANCZOS)
        self.exit_l = ImageTk.PhotoImage(exit)
        b1=Button(lb_bg, image=self.exit_l, command=self.iExit, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)
        b1_1=Button(lb_bg, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=600, width=220, height=40)  

    # ======================== Time ========================
    def update_time(self):
        current_time = strftime('%H:%M:%S %p')
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_time)

    def open_img(self):
        os.startfile("Photos_Data")

    def student_detail(self):
        self.std_window=Toplevel(self.root)
        self.std=Student(self.std_window)

    def train_data(self):
        self.std_window=Toplevel(self.root)
        self.std=Train(self.std_window)

    def face_recognition(self):
        self.std_window=Toplevel(self.root)
        self.std=Face_Recognition(self.std_window)

    def attendance_data(self):
        self.std_window=Toplevel(self.root)
        self.std=Attendance(self.std_window)

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are You Sure Exit This Project",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

