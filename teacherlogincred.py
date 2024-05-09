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
from teacher_reg import Teacherregistry
import tkinter as tk


class Teachercred:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Login')
        self.root.configure(background='lightblue')

        # Teacher ID Label
        label_teacher_id = tk.Label(root, text="Teacher ID",background='lightblue',foreground='black', font=('Quicksand', 12))
        label_teacher_id.place(relx = 0.45,rely = 0.2)

        # Teacher ID Entry
        entry_teacher_id = tk.Entry(root, font=('Quicksand', 12))
        entry_teacher_id.place(relx = 0.45,rely = 0.225)

        # Password Label
        label_password = tk.Label(root,background='lightblue',foreground='black', text="Password", font=('Quicksand', 12))
        label_password.place(relx = 0.45,rely = 0.3)

        # Password Entry
        entry_password = tk.Entry(root, show="*", font=('Quicksand', 12))
        entry_password.place(relx = 0.45,rely = 0.325)

        # Login Button
        btn_login = tk.Button(root, text="Login", command=self.login, font=('Quicksand', 12),bg="deep sky blue",fg='white', width=19)
        btn_login.place(relx = 0.45,rely = 0.5)



    def login(self):
        teacher_id = self.entry_teacher_id.get()
        password = self.entry_password.get()

        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='your_password', database='your_database')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM teacher WHERE teacher_id = %s AND password = %s", (teacher_id, password))
            teacher_data = cursor.fetchone()

            if teacher_data:
                messagebox.showinfo("Login Successful", "Welcome, Teacher!")
                # Add your logic for teacher login here
            else:
                messagebox.showerror("Login Failed", "Invalid Teacher ID or Password")

            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

       

if __name__ =="__main__":
    root=Tk()

    app = Teachercred(root)
    root.configure(bg='lightblue')
    root.mainloop()