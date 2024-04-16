from tkinter import RIDGE, W, Button, Entry, Frame, Image, Label, LabelFrame, Tk
from tkinter import ttk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ==============variables================
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


        # heading
        title_lbl = Label(text="Student Attendance System", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        
        self.create_left_frame()
        self.create_right_frame()

        

    def create_left_frame(self):
    # left label frame
        Left_frame = LabelFrame(self.root, borderwidth=2, bg="white", relief="ridge",
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=30, y=60, width=750, height=710)

        # current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=10, width=735, height=200)

        # Department
        dep_label = Label(current_course_frame, text="Department:", font=("times new roman", 15, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=20, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=4, pady=30, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Courses:", font=("times new roman", 15, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"),
                                    width=20, state="readonly")
        course_combo["values"] = ("Select Course", "AIML", "CTIS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=4, pady=30, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year:", font=("times new roman", 15, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=20, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"),
                                  width=20, state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=4, pady=30, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester:", font=("times new roman", 15, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        searchsemester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                            font=("times new roman", 12, "bold"), width=20, state="readonly")
        searchsemester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "3rd Semester",
                                          "4th Semester", "5th Semester", "6th Semester")
        searchsemester_combo.current(0)
        searchsemester_combo.grid(row=1, column=3, padx=4, pady=30, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Student Class Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=220, width=735, height=450)

        # Student ID
        studentId_label = Label(class_Student_frame, text="StudentId:", font=("times new roman", 15, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_std_id,
                                    font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 15, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_std_name,
                                      font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 15, "bold"),
                                 bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_div,
                                    font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No.
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 15, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_roll,
                                  font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 15, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender,
                                            font=("times new roman", 12, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date Of Birth
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 15, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_dob,
                               font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # E-mail
        email_label = Label(class_Student_frame, text="E-mail:", font=("times new roman", 15, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_email,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No.
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 15, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_phone,
                                 font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 15, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_address,
                                   font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 15, "bold"),
                               bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_teacher,
                                   font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio button
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample",
                                     value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample",
                                     value="No")
        radiobtn2.grid(row=6, column=1)

          # button frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=240, width=715, height=60)

        save_btn = Button(btn_frame, text="SAVE", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="UPDATE", width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white", command=self.update_data)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="DELETE",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="RESET",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

    # ButtonFrame1
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=280, width=715, height=35)

        add_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="ADD PHOTO SAMPLE", width=35, font=("times new roman", 13, "bold"),
                               bg="blue", fg="white")
        add_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1,command=self.update_data, text="UPDATE PHOTO SAMPLE", width=35, font=("times new roman", 13, "bold"),
                                  bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

    def create_right_frame(self):
        # Right label frame
        right_frame = LabelFrame(self.root, borderwidth=2, bg="white", relief="ridge",
                                  text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=790, y=60, width=720, height=710)

        # ========Search System==========

        Search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                   font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=180, width=710, height=80)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red",
                               fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=16, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=13, font=("times new roman", 12, "bold"), bg="blue",
                              fg="white")
        search_btn.grid(row=0, column=3, padx=6)

        showAll_btn = Button(Search_frame, text="Show All", width=13, font=("times new roman", 12, "bold"), bg="blue",
                               fg="white")
        showAll_btn.grid(row=0, column=4)

        # =============table frame===============
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=270, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          column=("dep", "course", "year", "sem", "id", "name", "div", "roll",
                                                  "gender", "dob", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="E-mail")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSample")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)  # Adjusted width for Division
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)  # Adjusted width for Email
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ====================Function declaration=====================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="systemattendance")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student (Department, Course, Year, Semester, Student_Id, Name, Division, RollNo, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ", (
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
                    self.var_radio1.get(),
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    #=============Fetch Data=================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="systemattendance")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()
    
    # ==============get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
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
    
     # update_function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
           messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update the details?", parent=self.root)
                if Update:
                   conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="systemattendance")
                   my_cursor = conn.cursor()
                   # Ensure that all placeholders (%s) are properly mapped to the values passed to execute
                   my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, RollNo=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", (
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
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details completed successfully.",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)       

    # delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this detail?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="systemattendance")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)      

    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            # If no faces are detected, return None
            if len(faces) == 0:
                return None
            # Crop all faces found
            for (x, y, w, h) in faces:
                cropped_face = img[y:y+h, x:x+w]
            return cropped_face

        cap = cv2.VideoCapture(0)
        img_id = 0

        while True:
            ret, frame = cap.read()
            if face_cropped(frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                # Save the captured face in the dataset folder with a unique identifier
                file_path = f"data/User_{self.var_std_id.get()}_{img_id}.jpg"
                cv2.imwrite(file_path, face)
                # Display the cropped face in the window
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 13 or img_id == 100:  # 13 is the Enter Key
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Generating dataset completed")

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
     root = Tk()
     obj = Student(root)
     root.mainloop()