from tkinter import *
from attendance import Attendance2
from attendance_files import Excel


class ChooseOperations:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Login')
        self.root.configure(background='lightblue')

        name_lbl=Label(self.root,text="Choose Operation",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        take_attendance_btn = Button(self.root,text="Take Attendance",command=self.take_attendance,font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        take_attendance_btn.place(relx = 0.4,rely=0.4)

        generate_files_btn = Button(self.root,text="Generate Attendance Files",command=self.gen_files,font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        generate_files_btn.place(relx = 0.4,rely=0.5)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)

    def exit(self):
        self.root.destroy()


    def gen_files(self):
        self.new_window = Toplevel(self.root)
        self.app = Excel(self.new_window)

    def take_attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance2(self.new_window)

if __name__ =="__main__":
    root=Tk()

    app = ChooseOperations(root)
    root.configure(bg='lightblue')
    root.mainloop()