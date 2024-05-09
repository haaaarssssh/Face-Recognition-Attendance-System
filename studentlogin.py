from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk,filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from mtcnn import MTCNN
import csv
import pandas as pd
from student import Student



class Studentlogin:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Login')
        self.root.configure(background='lightblue')

        name_lbl=Label(self.root,text="Student Sign Up / Login",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        student_register_btn = Button(self.root,command=self.register,text="Student Registration",font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        student_register_btn.place(relx = 0.4,rely=0.4)

        student_login_btn = Button(self.root,command=self.login,text="Student Login",font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        student_login_btn.place(relx = 0.4,rely=0.5)

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def login(self):
        pass

if __name__ =="__main__":
    root=Tk()

    app = Studentlogin(root)
    root.configure(bg='lightblue')
    root.mainloop()