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



class Login:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Student Login')
        self.root.configure(background='lightblue')

if __name__ =="__main__":
    root=Tk()

    app = Login(root)
    root.configure(bg='lightblue')
    root.mainloop()