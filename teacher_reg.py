from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from attendance_files import Excel
from attendance import Attendance2


class Teacherregistry:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Teacher Registration")

        #variables
        self.var

        name_lbl=Label(self.root,text="TEACHER REGISTRATION",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        main_frame =  Frame(self.root,bd=2,background='#58a4b0')
        main_frame.place(relx=0.5,rely=0.5,anchor='center',width=1900,height=700)
  
        #left
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Teacher Details", font=('Quicksand',12,'bold'),background='#d8dbe2')
        left_frame.place(relx=0.01,y=10,width=920,height=670)

        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Teacher", font=('Quicksand',12,'bold'),background='#d8dbe2')
        right_frame.place(relx=0.5,y=10,width=920,height=670)

#teache_id,name,branch,semester,subject,password
        teacher_id_label=Label(left_frame,text="Teacher ID",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        teacher_id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        teacher_id_entry = ttk.Entry(left_frame,width=60,font=('Quicksand',12,'italic'))
        teacher_id_entry.grid(row=0,column=1,padx=10,sticky=W)

        name_label=Label(left_frame,text="Name",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        name_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        name_entry = ttk.Entry(left_frame,width=60,font=('Quicksand',12,'italic'))
        name_entry.grid(row=2,column=1,padx=10,sticky=W)

        branch_label=Label(left_frame,text="Branch",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        branch_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        branch_entry = ttk.Entry(left_frame,width=60,font=('Quicksand',12,'italic'))
        branch_entry.grid(row=4,column=1,padx=10,sticky=W)

        semester_label=Label(left_frame,text="Semester",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        semester_label.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        semester_entry = ttk.Entry(left_frame,width=60,font=('Quicksand',12,'italic'))
        semester_entry.grid(row=6,column=1,padx=10,sticky=W)

        subject_label=Label(left_frame,text="Subject",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        subject_label.grid(row=8,column=0,padx=10,pady=10,sticky=W)

        subject_entry = ttk.Entry(left_frame,width=60,font=('Quicksand',12,'italic'))
        subject_entry.grid(row=8,column=1,padx=10,sticky=W)

        password_label=Label(left_frame,text="Password",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        password_label.grid(row=10,column=0,padx=10,pady=10,sticky=W)

        password_entry = ttk.Entry(left_frame,show='*',width=60,font=('Quicksand',12,'italic'))
        password_entry.grid(row=10,column=1,padx=10,sticky=W)

        
        button1_frame = LabelFrame(left_frame,bd=2)
        button1_frame.place(relx=0.1,rely=0.6,width=728,height=35)

        save_btn = Button(button1_frame,text="Save",font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        save_btn.grid(row=0,column=0)

        update_btn = Button(button1_frame,text="Update",font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(button1_frame,text="Delete",font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(button1_frame,text="Reset",font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        reset_btn.grid(row=0,column=3)
        

if __name__ =="__main__":
    root=Tk()

    app = Teacherregistry(root)
    root.configure(bg='lightblue')
    root.mainloop()