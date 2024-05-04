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



class Attendance2:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Face Recognition")
        self.root.configure(background='lightblue')

        self.var_div = StringVar()
        self.var_semester = StringVar()
        self.var_teacher = StringVar()
        self.var_subject = StringVar()

        name_lbl=Label(self.root,text="Take Attendance ",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')


        teacher_label=Label(self.root,text="Teacher Name",font=('Quicksand',12),background='lightblue',foreground='black')
        teacher_label.place(relx = 0.35,rely = 0.1)

        teacher_entry=ttk.Entry(self.root,textvariable=self.var_teacher,width=60,font=('Quicksand',12,'italic'))
        teacher_entry.place(relx = 0.35,rely = 0.125)

        dpt_label=Label(self.root,text="Department",font=('Quicksand',12),background='lightblue',foreground='black')
        dpt_label.place(relx = 0.35,rely = 0.2)

        dpt_entry=ttk.Entry(self.root,width=60,font=('Quicksand',12,'italic'))
        dpt_entry.place(relx = 0.35,rely = 0.225)

        div_label=Label(self.root,text="Division",font=('Quicksand',12),background='lightblue',foreground='black')
        div_label.place(relx = 0.35,rely = 0.3)

        div_entry=ttk.Entry(self.root,textvariable=self.var_div,width=60,font=('Quicksand',12,'italic'))
        div_entry.place(relx = 0.35,rely = 0.325)

        semester_label=Label(self.root,text="Semester",font=('Quicksand',12),background='lightblue',foreground='black')
        semester_label.place(relx = 0.35,rely = 0.4)

        semester_entry=ttk.Entry(self.root,textvariable=self.var_semester,width=60,font=('Quicksand',12,'italic'))
        semester_entry.place(relx = 0.35,rely = 0.425)
        
        subject_label=Label(self.root,text="Subject",font=('Quicksand',12),background='lightblue',foreground='black')
        subject_label.place(relx = 0.35,rely = 0.5)

        subject_entry=ttk.Entry(self.root,textvariable=self.var_subject,width=60,font=('Quicksand',12,'italic'))
        subject_entry.place(relx = 0.35,rely = 0.525)

        take_photo_btn = Button(self.root,command=self.photo_atd,text="Upload A Photo",font=('Quicksand',12),bg="deep sky blue",fg='white', width=30)
        take_photo_btn.place(relx = 0.35,rely = 0.6)

        take_photo_btn = Button(self.root,command=self.video_atd,text="Upload A Video",font=('Quicksand',12),bg="deep sky blue",fg='white', width=30)
        take_photo_btn.place(relx = 0.49,rely = 0.6)

        open_cam = Button(self.root,command=self.face_recog,text="Video Camera",font=('Quicksand',12),bg="deep sky blue",fg='white', width=60)
        open_cam.place(relx = 0.35,rely = 0.63)

        take_attendance_btn = Button(self.root,command=self.face_recog,text="Take Attendance",font=('Quicksand',12),bg="green",fg='white', width=60)
        take_attendance_btn.place(relx = 0.35,rely = 0.7)

        back_button_2 = Button(self.root,command=self.exit,text="Back",cursor="hand2",font=('Quicksand',15),bg='Black',fg='white')
        back_button_2.place(relx=0.1, rely=0.9, anchor='center',width=220,height=40)



    def mark_attendance(self, i, r, n, d):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dString = now.strftime("%H:%M:%S")

        # Check if the file is empty to add the header
        if os.path.getsize("atd.csv") == 0:
            with open("atd.csv", "a", newline="\n") as f:
                writer = csv.writer(f)
                writer.writerow(["Student ID", "Roll", "Name", "Department","Semester","Division","Teacher","Subject", "Time", "Date", "Attendance"])
        
        # Write attendance data
        with open("atd.csv", "a", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow([i, r, n, d,self.var_semester.get(),self.var_div.get(),self.var_teacher.get(),self.var_subject.get(), dString, d1, "Present",])


    def generate_excel(self):
        df = pd.read_csv("atd.csv")
        df.to_excel("attendance.xlsx", index=False)

    def face_recog(self):
    
        def fetch_student_details(id, my_cursor):
            fields = ['Name', 'Roll', 'department', 'student_id']
            details = {}
            for field in fields:
                query = f"select {field} from student where student_id={id}"
                my_cursor.execute(query)
                result = my_cursor.fetchone()
                details[field] = '+'.join(result) if result else ''
            return details

        def draw_boundary(img, classifier, scalefactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            bgr_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

            features = classifier.detect_faces(bgr_image)
            coord = []

            for feature in features:
                if len(feature['box']) == 4:
                    x, y, w, h = feature['box']
                    cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(host='localhost', username='root', password='Harsh@2402', database='face_recognizer')
                    my_cursor = conn.cursor()

                    details = fetch_student_details(id, my_cursor)
                    n = details['Name']
                    r = details['Roll']
                    d = details['department']
                    i = details['student_id']

                    if confidence > 77:
                        cv2.putText(img, f'Name: {n}', (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Roll: {r}', (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Department: {d}', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Student ID: {i}', (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, 'Unknown Face', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]

            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), 'Face', clf)
            return img 

        facecascade = MTCNN()
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r'C:\Users\haaaa\OneDrive\Desktop\Attendance\Attendance App\classifier1.xml')

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognise(img, clf, facecascade)
            cv2.imshow("Welcome To Face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

        # Generate Excel file after processing all faces
        #self.generate_excel()



    def photo_atd(self):
        def fetch_student_details(id, my_cursor):
            fields = ['Name', 'Roll', 'department', 'student_id']
            details = {}
            for field in fields:
                query = f"select {field} from student where student_id={id}"
                my_cursor.execute(query)
                result = my_cursor.fetchone()
                details[field] = '+'.join(result) if result else ''
            return details

        def draw_boundary(img, classifier, scalefactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            bgr_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

            features = classifier.detect_faces(bgr_image)
            coord = []

            for feature in features:
                if len(feature['box']) == 4:
                    x, y, w, h = feature['box']
                    cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(host='localhost', username='root', password='Harsh@2402', database='face_recognizer')
                    my_cursor = conn.cursor()

                    details = fetch_student_details(id, my_cursor)
                    n = details['Name']
                    r = details['Roll']
                    d = details['department']
                    i = details['student_id']

                    if confidence > 77:
                        cv2.putText(img, f'Name: {n}', (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Roll: {r}', (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Department: {d}', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Student ID: {i}', (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, 'Unknown Face', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]

            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), 'Face', clf)
            return img 

        facecascade = MTCNN()
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r'C:\Users\haaaa\OneDrive\Desktop\Attendance\Attendance App\classifier1.xml')
        file_path = filedialog.askopenfilename(initialdir=r"C:\Users\haaaa\OneDrive\Desktop", title="Select an Image", filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])
        img = cv2.imread(file_path)

        if img is None:
            print("Error reading image!")
        else:
            # Process the image for face recognition
            img = recognise(img, clf, facecascade)

            # Display the processed image
            cv2.imshow("Face Recognition", img)
            cv2.waitKey(0)  # Wait for a key press to close the window
            cv2.destroyAllWindows()

        # Generate Excel file after processing all faces
        #self.generate_excel()


    def destroy(self):
        self.root.destroy()


    def video_atd(self):
        def fetch_student_details(id, my_cursor):
            fields = ['Name', 'Roll', 'department', 'student_id']
            details = {}
            for field in fields:
                query = f"select {field} from student where student_id={id}"
                my_cursor.execute(query)
                result = my_cursor.fetchone()
                details[field] = '+'.join(result) if result else ''
            return details

        def draw_boundary(img, classifier, scalefactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            bgr_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

            features = classifier.detect_faces(bgr_image)
            coord = []

            for feature in features:
                if len(feature['box']) == 4:
                    x, y, w, h = feature['box']
                    cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(host='localhost', username='root', password='Harsh@2402', database='face_recognizer')
                    my_cursor = conn.cursor()

                    details = fetch_student_details(id, my_cursor)
                    n = details['Name']
                    r = details['Roll']
                    d = details['department']
                    i = details['student_id']

                    if confidence > 77:
                        cv2.putText(img, f'Name: {n}', (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Roll: {r}', (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Department: {d}', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        cv2.putText(img, f'Student ID: {i}', (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                        self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, 'Unknown Face', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]

            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), 'Face', clf)
            return img 

        facecascade = MTCNN()
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r'C:\Users\haaaa\OneDrive\Desktop\Attendance\Attendance App\classifier1.xml')
        file_path = filedialog.askopenfilename(initialdir=r"C:\Users\haaaa\OneDrive\Desktop", title="Select a Video", filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))

        cap = cv2.VideoCapture(file_path)

        if not cap.isOpened():
            print("Error opening video!")
            exit()

        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            # Check if frame is read successfully (end of video or error)
            if not ret:
                print("No more frames to read or error!")
                break

            # Process the frame for face recognition
            frame = recognise(frame, clf, facecascade)  # Assuming 'recognise' function exists

            # Display the processed frame
            cv2.imshow("Face Recognition in Video", frame)

            # Exit loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release video capture and close windows
        cap.release()
        cv2.destroyAllWindows()

        # Generate Excel file after processing all faces
        #self.generate_excel()


    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = Attendance2(root)
    root.mainloop()


    





