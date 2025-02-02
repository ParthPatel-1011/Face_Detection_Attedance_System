from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ==================== variables ======================
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        img1 = Image.open("Images/stud.jpg")  
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoi1 = ImageTk.PhotoImage(img1)
        lb1 = Label(self.root, image=self.photoi1)
        lb1.place(x=0, y=0, width=800, height=200)

        img2 = Image.open("Images/stu.jpg")  
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoi2 = ImageTk.PhotoImage(img2)
        lb2 = Label(self.root, image=self.photoi2)
        lb2.place(x=800, y=0, width=800, height=200)

        # bg image
        # Image Background
        bg = Image.open("Images/bg.jpg")  
        bg = bg.resize((1530, 710), Image.LANCZOS)
        self.photobg = ImageTk.PhotoImage(bg)
        lb_bg = Label(self.root, image=self.photobg)
        lb_bg.place(x=0, y=200, width=1530, height=710)

        # title 
        title=Label(lb_bg, text="ATTENDANCE MANAGMENT SYSTEM", font=("times new roman",35,"bold"), bg="white", fg="darkblue")
        title.place(x=0, y=0,width=1530, height=45)

        main_frame = Frame(lb_bg,bd=2,bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # left frame
        left_f=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Detail", font=("times new roman",12,"bold"))
        left_f.place(x=10, y=10, width=730, height=580)

        imgl1 = Image.open("Images/stud.jpg")  
        imgl1 = imgl1.resize((720, 130), Image.LANCZOS)
        self.imgl1_l = ImageTk.PhotoImage(imgl1)
        lb3 = Label(left_f, image=self.imgl1_l)
        lb3.place(x=5, y=0, width=720, height=130)

        leftin_frame = Frame(left_f,bd=2,bg="white", relief=RIDGE)
        leftin_frame.place(x=5, y=135, width=720, height=370)        

        # labeled entry 

        #attendence ID
        attendence_Id_l = Label(leftin_frame, text="Attendance ID :", font=("times new roman",13,"bold"), bg="white")
        attendence_Id_l.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        attendence_Id_entry = ttk.Entry(leftin_frame, width=20, textvariable=self.var_attend_id, font=("times new roman",13,"bold"))
        attendence_Id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Roll
        rolllb = Label(leftin_frame, text="Roll :", font=("times new roman",13,"bold"), bg="white")
        rolllb.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        rolllb = ttk.Entry(leftin_frame, width=20, textvariable=self.var_attend_roll, font=("times new roman",13,"bold"))
        rolllb.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # name
        name_lb = Label(leftin_frame, text="Name :", font=("times new roman",13,"bold"), bg="white")
        name_lb.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        name_lb = ttk.Entry(leftin_frame, width=20, textvariable=self.var_attend_name, font=("times new roman",13,"bold"))
        name_lb.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Department
        dep_lb = Label(leftin_frame, text="Department :", font=("times new roman",13,"bold"), bg="white")
        dep_lb.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        dep_lb = ttk.Entry(leftin_frame, width=20, textvariable=self.var_attend_dep, font=("times new roman",13,"bold"))
        dep_lb.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Time
        time_lb = Label(leftin_frame, text="Time :", font=("times new roman",13,"bold"), bg="white")
        time_lb.grid(row=2, column=0, padx=10,pady=5, sticky=W)

        time_lb = ttk.Entry(leftin_frame, width=20, textvariable=self.var_attend_time, font=("times new roman",13,"bold"))
        time_lb.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Date
        date_lb = Label(leftin_frame, text="Date :", font=("times new roman",13,"bold"), bg="white")
        date_lb.grid(row=2, column=2, padx=10,pady=5, sticky=W)

        date_lb = ttk.Entry(leftin_frame, width=20, textvariable=self.var_attend_date, font=("times new roman",13,"bold"))
        date_lb.grid(row=2, column=3, padx=5, pady=5, sticky=W)

         # Attendance
        attend_label = Label(leftin_frame, text="Attendance Status", font=("times new roman",13,"bold"), bg="white")
        attend_label.grid(row=3, column=0, padx=5, sticky=W)
        self.attend_combo = ttk.Combobox(leftin_frame, textvariable=self.var_attend_attendance, font=("times new roman",13,"bold"))
        self.attend_combo["values"] = ["Status", "Present", "Absent"]
        self.attend_combo.current(0)
        self.attend_combo.grid(row=3, column=1,padx=5, pady=8,  sticky=W)

        #  Button frame 
        btn_frame = Frame(leftin_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=290, width=720, height=35)

        import_btn = Button(btn_frame, text="Import CSV", width=17, command=self.importcsv, font=("times new roman",13,"bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", width=17, command=self.exportcsv, font=("times new roman",13,"bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=17, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_Data,font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        

        # Right frame
        right_f=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Detail", font=("times new roman",12,"bold"))
        right_f.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(right_f, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        # ====== scroll bar ===========
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendreporttable = ttk.Treeview(table_frame, columns=("ID", "Roll", "Name","Department","Date","Time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendreporttable.xview)
        scroll_y.config(command=self.attendreporttable.yview)

        self.attendreporttable.heading("ID",text="Attendance ID")
        self.attendreporttable.heading("Roll",text="RollNo")
        self.attendreporttable.heading("Name",text="Name")
        self.attendreporttable.heading("Department",text="Department")
        self.attendreporttable.heading("Time",text="Time")
        self.attendreporttable.heading("Date",text="Date")
        self.attendreporttable.heading("attendance",text="Attendance")

        self.attendreporttable["show"]="headings"

        self.attendreporttable.column("ID",width=100)
        self.attendreporttable.column("Roll",width=100)
        self.attendreporttable.column("Name",width=100)
        self.attendreporttable.column("Department",width=100)
        self.attendreporttable.column("Time",width=100)
        self.attendreporttable.column("Date",width=100)
        self.attendreporttable.column("attendance",width=100)

        self.attendreporttable.pack(fill=BOTH,expand=1)

        self.attendreporttable.bind("<ButtonRelease>",self.get_cursor)

    # =================== Fatch Data =================

    def fetchdata(self,rows):
        self.attendreporttable.delete(*self.attendreporttable.get_children())
        for i in rows:
            self.attendreporttable.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], parent=self.root)
        with open(fln) as myfile:
            csvreader=csv.reader(myfile,delimiter=",")
            for i in csvreader:
                mydata.append(i)
            self.fetchdata(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Data Missing", "Data Not Found")
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exported to "+os.path.basename(fln)+" successfuly")

        except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.attendreporttable.focus()
        content=self.attendreporttable.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_date.set(rows[4])
        self.var_attend_time.set(rows[5])
        self.var_attend_attendance.set(rows[6])
    
    def reset_Data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()