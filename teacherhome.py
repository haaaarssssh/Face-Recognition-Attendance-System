from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from attendance_files import Excel
from attendance import Attendance2
from teacherlogin import Login
from studentlogin import Studentlogin
from teacherlogin import Login
from teacherlogincred_copy import Teachercred,Attendance2

from tkinter import Tk

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Attendance")
        

        name_lbl=Label(self.root,text="TEACHER PAGE",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        #Add
        add_button = Image.open(r"images\plus.png")
        add_button = add_button.resize((220,220))
        self.photoadd_button = ImageTk.PhotoImage(add_button)

        add_button_1= Button(self.root,image = self.photoadd_button,command=self.student_details,cursor="hand2")
        add_button_1.place(relx=0.20, rely=0.5, anchor='center',width=220,height=220)

        add_button_2 = Button(self.root,text="LOGIN",command=self.student_details,cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        add_button_2.place(relx=0.20, rely=0.62, anchor='center',width=220,height=40)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Teachercred(self.new_window)


if __name__ == "__main__":
    root = Tk()  # Create a single instance of Tk

    # Instantiate Attendance
    attendance = Attendance(root)

    # After the Attendance instance is created, create the Teachercred instance
    root2 = Tk()  # No need to create a new instance, reuse the existing one
    teacher_cred_app = Teachercred(root2)

    # After the Teachercred instance is created, create the Attendance2 instance
    root3 = Tk()  # Create another instance of Tk for Attendance2
    attendance_app = Attendance2(root3, teacher_cred_app)
    root3.configure(bg='lightblue')

    # Call mainloop once after all instances are created
    root.mainloop()
    root2.mainloop()
    root3.mainloop()
