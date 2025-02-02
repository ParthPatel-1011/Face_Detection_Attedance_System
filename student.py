from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


        # Image 1
        img = Image.open("Images/stu.jpg") 
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoi1 = ImageTk.PhotoImage(img)
        lb1 = Label(self.root, image=self.photoi1)
        lb1.place(x=0, y=0, width=500, height=130)

        # Image 2
        img1 = Image.open("Images/student11.jpeg")  
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoi2 = ImageTk.PhotoImage(img1)
        lb2 = Label(self.root, image=self.photoi2)
        lb2.place(x=500, y=0, width=500, height=130)

        # Image 3
        img2 = Image.open("Images/stud.jpg")  
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

        title=Label(lb_bg, text="STUDENT MANAGMENT SYSTEM", font=("times new roman",35,"bold"), bg="white", fg="darkblue")
        title.place(x=0, y=0,width=1530, height=45)

        main_frame = Frame(lb_bg,bd=2,bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # left frame
        left_f=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Detail", font=("times new roman",12,"bold"))
        left_f.place(x=10, y=10, width=720, height=580)

        imgl1 = Image.open("Images/stud.jpg")  
        imgl1 = imgl1.resize((710, 130), Image.LANCZOS)
        self.imgl1_l = ImageTk.PhotoImage(imgl1)
        lb3 = Label(left_f, image=self.imgl1_l)
        lb3.place(x=5, y=0, width=710, height=130)


        # current cource Information
        course_l=LabelFrame(left_f, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        course_l.place(x=5, y=135, width=710, height=115)

        # Department
        dep_label = Label(course_l, text="Department", font=("times new roman",13,"bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(course_l,textvariable=self.var_dep , font=("times new roman",13,"bold"),state="read only")
        dep_combo["values"] = ["Select Department","Computer", "IT", "Civil", "Marin"]
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W) 

        # Course
        Cour_label = Label(course_l, text="Course", font=("times new roman",13,"bold"), bg="white")
        Cour_label.grid(row=0, column=3, padx=10, sticky=W)
        Cour_combo = ttk.Combobox(course_l,textvariable=self.var_course, font=("times new roman",13,"bold"),state="read only")
        Cour_combo["values"] = ["Select Course","FE", "SE", "TE", "BE"]
        Cour_combo.current(0)
        Cour_combo.grid(row=0, column=4, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(course_l, text="Year", font=("times new roman",13,"bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(course_l, textvariable=self.var_year, font=("times new roman",13,"bold"),state="read only")
        year_combo["values"] = ["Select Year","2020-21", "2021-22", "2022-23", "2023-24"]
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W) 

        # Semester
        sem_label = Label(course_l, text="Semester", font=("times new roman",13,"bold"), bg="white")
        sem_label.grid(row=1, column=3, padx=10, sticky=W)
        sem_combo = ttk.Combobox(course_l,textvariable=self.var_semester, font=("times new roman",13,"bold"),state="read only")
        sem_combo["values"] = ["Select Semester","Semester 1", "Semester 2", "Semester 3", "Semester 4"]
        sem_combo.current(0)
        sem_combo.grid(row=1, column=4, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_l=LabelFrame(left_f, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        class_student_l.place(x=5, y=250, width=710, height=300)

        # Student ID
        StufdentId_l = Label(class_student_l, text="Student ID :", font=("times new roman",13,"bold"), bg="white")
        StufdentId_l.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        StufdentId_entry = ttk.Entry(class_student_l, width=20,textvariable=self.var_std_id, font=("times new roman",13,"bold"))
        StufdentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

         # Student Name
        Stufdentname_l = Label(class_student_l, text="Student Name :", font=("times new roman",13,"bold"), bg="white")
        Stufdentname_l.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        Stufdentname_entry = ttk.Entry(class_student_l, width=20,textvariable=self.var_std_name, font=("times new roman",13,"bold"))
        Stufdentname_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

         # Class Division
        Classd_l = Label(class_student_l, text="Class Division :", font=("times new roman",13,"bold"), bg="white")
        Classd_l.grid(row=1, column=0, padx=10,pady=5, sticky=W)
        classd_combo = ttk.Combobox(class_student_l,width=18,textvariable=self.var_div, font=("times new roman",13,"bold"),state="read only")
        classd_combo["values"] = ["A","B","C","D"]
        classd_combo.current(0)
        classd_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Roll no
        rillno_l = Label(class_student_l, text="Roll Number :", font=("times new roman",13,"bold"), bg="white")
        rillno_l.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        rillno_entry = ttk.Entry(class_student_l, width=20,textvariable=self.var_roll, font=("times new roman",13,"bold"))
        rillno_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        gender_l = Label(class_student_l, text="Gender :", font=("times new roman",13,"bold"), bg="white")
        gender_l.grid(row=2, column=0, padx=10,pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_l,width=18,textvariable=self.var_gender, font=("times new roman",13,"bold"),state="read only")
        gender_combo["values"] = ["Male","Female", "Other"]
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

         # DOB
        dob_l = Label(class_student_l, text="DOB :", font=("times new roman",13,"bold"), bg="white")
        dob_l.grid(row=2, column=2, padx=10,pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_l, width=20, textvariable=self.var_dob, font=("times new roman",13,"bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        email_l = Label(class_student_l, text="E-mail :", font=("times new roman",13,"bold"), bg="white")
        email_l.grid(row=3, column=0, padx=10,pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_l, width=20, textvariable=self.var_email, font=("times new roman",13,"bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone Number
        phone_l = Label(class_student_l, text="Phone Number :", font=("times new roman",13,"bold"), bg="white")
        phone_l.grid(row=3, column=2, padx=10,pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_l, width=20, textvariable=self.var_phone, font=("times new roman",13,"bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

         # Address
        address_l = Label(class_student_l, text="Address :", font=("times new roman",13,"bold"), bg="white")
        address_l.grid(row=4, column=0, padx=10,pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_l, width=20, textvariable=self.var_address, font=("times new roman",13,"bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher Name
        teacher_l = Label(class_student_l, text="Teacher Name :", font=("times new roman",13,"bold"), bg="white")
        teacher_l.grid(row=4, column=2, padx=10,pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_l, width=20, textvariable=self.var_teacher, font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # Radiobuttons
        self.var_radio1 = StringVar()
        rbtn1 = ttk.Radiobutton(class_student_l, variable=self.var_radio1, text="Tack photo sample",value="Yes")
        rbtn1.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        rbtn2 = ttk.Radiobutton(class_student_l, variable=self.var_radio1, text="No photo sample", value="No")
        rbtn2.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        # button Frame
        btn_frame = Frame(class_student_l, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=3, y=200, width=700, height=35)

        save_btn = Button(btn_frame, text="Save", width=17, command=self.add_data, font=("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=17, command=self.update_data, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=17, command=self.delet_data, font=("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_data, font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Photo Button Frame
        phote_btn_frame = Frame(class_student_l, bd=2, relief=RIDGE, bg="white")
        phote_btn_frame.place(x=3, y=235, width=700, height=35)

        tack_photo_btn = Button(phote_btn_frame, text="Tack Photo Sample", width=35, command=self.genrate_dataset, font=("times new roman",13,"bold"), bg="blue", fg="white")
        tack_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(phote_btn_frame, text="Update Photo Sample", width=34, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)


        # Right frame
        right_f=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Detail", font=("times new roman",12,"bold"))
        right_f.place(x=750, y=10, width=720, height=580)

        imgr1 = Image.open("Images/stud.jpg")  
        imgr1 = imgl1.resize((710, 130), Image.LANCZOS)
        self.imgr1_l = ImageTk.PhotoImage(imgr1)
        lbr1 = Label(right_f, image=self.imgr1_l)
        lbr1.place(x=5, y=0, width=710, height=130)

        # ============= Search System ====================
        search_frame=LabelFrame(right_f, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        search_frame.place(x=5, y=135, width=710, height=70) 

        searchbar_l = Label(search_frame, text="Search By :", font=("times new roman",15,"bold"), bg="black", fg="white")
        searchbar_l.grid(row=0, column=0, padx=10,pady=5, sticky=W)
        searchbar_combo = ttk.Combobox(search_frame, font=("times new roman",15,"bold"),state="read only",width=13)
        searchbar_combo["values"] = ["Select","Roll_No","Phone_No"]
        searchbar_combo.current(0)
        searchbar_combo.grid(row=0, column=1, padx=1, pady=10   , sticky=W)

        search_entry = ttk.Entry(search_frame, width=13, font=("times new roman",15,"bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=("times new roman",15,"bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3,padx=5)

        showAll_btn = Button(search_frame, text="Show All", width=10, font=("times new roman",15,"bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4,padx=5)

        # ======================= table frame ==============================
        table_f = Frame(right_f, bd=2, bg="white", relief=RIDGE)
        table_f.place(x=5, y=210, width=710, height=340)

        scroll_x = ttk.Scrollbar(table_f,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_f,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_f, columns=("dep", "course", "year","sem","id","name","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Tracher")
        self.student_table.heading("photo",text="PhotoSampleStatus")


        # self.student_table.column("dep", width=100)
        # self.student_table.column("course", width=100)
        # self.student_table.column("year", width=100)
        # self.student_table.column("sem", width=100)
        # self.student_table.column("id", width=100)
        # self.student_table.column("name", width=100)
        # self.student_table.column("div", width=100)
        # self.student_table.column("dob", width=100)
        # self.student_table.column("email", width=100)
        # self.student_table.column("phone", width=100)
        # self.student_table.column("address", width=100)
        # self.student_table.column("teacher", width=100)
        # self.student_table.column("photo", width=100)

        columns = ["dep", "course", "year", "sem", "id", "name", "div", "dob", "email", "phone", "address", "teacher", "photo"]

        for col in columns:
            self.student_table.column(col, width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # ======================== Function Decration ===============================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="mysql@1011",database="face_recognition")
                crs = conn.cursor()
                crs.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_teacher.get(),
                                                                                                    self.var_radio1.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "Student Details Has Been Added Successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    # ================ fetch data ======================
    def fetch_data(self):

            conn = mysql.connector.connect(host="localhost",username="root",password="mysql@1011",database="face_recognition")
            crs = conn.cursor()
            crs.execute("select * from student")
            data=crs.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)                
                conn.commit()
            conn.close()

    # ============================ Get cursor ===========================
    def get_cursor(self,event=""):
        cur_focus=self.student_table.focus()
        content=self.student_table.item(cur_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    # ============ uodate Data ===================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                updatem=messagebox.askyesno("Update","Do You Want To Update This Student Details")
                if updatem>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="mysql@1011",database="face_recognition")
                    crs = conn.cursor()
                    crs.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_std_id.get()
                                                                                                    ))
                else:
                    if not updatem:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    # ================ Delet Data ====================
    def delet_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be Required")
        else:
            try:
                deletem=messagebox.askyesno("Delete","Do You Want To Delete This Student Details")
                if deletem>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="mysql@1011",database="face_recognition")
                    crs = conn.cursor()
                    crs.execute("DELETE FROM student WHERE Student_id = %s",(self.var_std_id.get(),))
                else:
                    if not deletem:
                        return
                messagebox.showinfo("Success","Student Details Successfully Deleted",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    # ================== Reset Data =======================
    def reset_data(self):
        self.var_dep.set("Select department")
        self.var_course.set("Select course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    # ===============================  Generate Dataset or Tack Photo Sample ================
    def genrate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else :
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="mysql@1011",database="face_recognition")
                crs = conn.cursor()
                crs.execute("select * from student")
                myresult=crs.fetchall()
                id=self.var_std_id.get()
    
                crs.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_std_id.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ============ load data on face frontals  from opencv ============
                face_classifire=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifire.detectMultiScale(grey,1.3,5)
                    # scalling factor = 1.3
                    # Minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    return None
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_RGB2GRAY)
                        photo_path="Photos_Data/user."+str(id)+"."+str(img_id)+".jpg"

                        cv2.imwrite(photo_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Genrating data set Completed !!!!!")

            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

            

                        




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
