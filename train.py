from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title=Label(self.root,text="TRAIN DATA SET", font=("times new roman",35,"bold"), bg="white", fg="red")
        title.place(x=0, y=0,width=1530, height=45)

        img_top = Image.open("Images/phface12.jpg")  
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.imgl1_top = ImageTk.PhotoImage(img_top)
        lb3 = Label(self.root, image=self.imgl1_top)
        lb3.place(x=0, y=50, width=1530, height=325)

        # Train data button 
        b1_1=Button(self.root, text="TRAIN DATA", command=self.train_classifire, cursor="hand2", font=("times new roman",18,"bold"), bg="red", fg="white")
        b1_1.place(x=0, y=375, width=1530, height=60)

        img_down = Image.open("Images/facere.jpg")  
        img_down = img_down.resize((1530, 325), Image.LANCZOS)
        self.imgl1_down = ImageTk.PhotoImage(img_down)
        lb3 = Label(self.root, image=self.imgl1_down)
        lb3.place(x=0, y=430, width=1530, height=325)


    def train_classifire(self):
        data_dir=("Photos_Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  # convert image to Greyscale
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # Train the Classifire and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifire.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed !")
        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()