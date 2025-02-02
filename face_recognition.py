from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"), bg="white", fg="darkblue")
        title.place(x=0, y=0,width=1530, height=45)

        img_main = Image.open("Images/kl.png")  
        img_main = img_main.resize((1530, 745), Image.LANCZOS)
        self.imgl1_main = ImageTk.PhotoImage(img_main)
        lb3 = Label(self.root, image=self.imgl1_main)  # Use self.root as the parent
        lb3.place(x=0, y=45, width=1530, height=745)

        bu1 = Button(lb3, text="Face Recognition", cursor="hand2",command=self.face_recog, font=("times new roman",15,"bold"), bg="darkblue", fg="white", bd=0)
        bu1.place(x=663, y=550, width=220, height=40)

    # ======================= Mark Attendance ===========================
    def mark_attendance(self,i,r,n,d):
        with open("attend.csv","r+",newline="\n") as f:
            myDataLisy=f.readlines()
            name_list=[]
            for line in myDataLisy:
                entry=line.split((","))
                name_list.append(entry[0])
            if (i not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{d1},{dtString},Present")
            


    # ================= Face Recognition =======================
    def face_recog(self):
        def draw_boundray(img, classifire, scaleFactor, minNeighbors, color, text, clf):
            grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifire.detectMultiScale(grey_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(grey_image[y:y+h, x:x+w])
                confidence = (100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="mysql@1011", database="face_recognition")
                crs = conn.cursor()

                # Fetch ID
                crs.execute("select Student_id from student where Student_id=" + str(id))
                i = crs.fetchone()
                i = "+".join(i) if i else "Unknown"  # Handle None case

                # Fetch Name
                crs.execute("select Name from student where Student_id=" + str(id))
                n = crs.fetchone()
                n = "+".join(n) if n else "Unknown"  # Handle None case

                # Fetch Roll
                crs.execute("select Roll from student where Student_id=" + str(id))
                r = crs.fetchone()
                r = "+".join(r) if r else "Unknown"  # Handle None case

                # Fetch Department
                crs.execute("select Dep from student where Student_id=" + str(id))
                d = crs.fetchone()
                d = "+".join(d) if d else "Unknown"  # Handle None case

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifire.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()