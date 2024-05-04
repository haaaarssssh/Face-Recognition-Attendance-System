








from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import pandas as pd
import os



class Excel:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Get Attendance File")
        self.root.configure(background='lightblue')

        self.var_startdate = StringVar()
        self.var_enddate = StringVar()
        self.var_department = StringVar()
        self.var_division = StringVar()
        self.var_teacher = StringVar()
        self.var_subject = StringVar()

        centre_lbl = Label(self.root, text="Attendance Files", font=('Quicksand', 36), fg='black', bg='lightblue')
        centre_lbl.pack(pady=40)

        main_frame = Frame(self.root, bd=2, background='#58a4b0')
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=500, height=400)



        dep_label = Label(main_frame, text="Department", font=('Quicksand', 12), background='#58a4b0', foreground='white')
        dep_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        dep_combo = ttk.Combobox(main_frame, textvariable=self.var_department, font=('Quicksand', 12, 'italic'), width=17, state='readonly')
        dep_combo['values'] = ('Select', "Computer", "IT", 'Civil', 'Mechanical')
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        div_label = Label(main_frame, text="Class Division", font=('Quicksand', 12), background='#58a4b0', foreground='white')
        div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        div_combo = ttk.Combobox(main_frame, textvariable=self.var_division, font=('Quicksand', 12, 'italic'), width=17, state='readonly')
        div_combo['values'] = ('Select Division', "A", "B", "C", "D")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        teahername_label = Label(main_frame, text="Teacher Name", font=('Quicksand', 12), background='#58a4b0', foreground='white')
        teahername_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        teahername_entry = Entry(main_frame, textvariable=self.var_teacher, width=20, font=('Quicksand', 12, 'italic'))
        teahername_entry.grid(row=2, column=1, padx=10, stick=W)

        subject_label = Label(main_frame, text="Subject", font=('Quicksand', 12), background='#58a4b0', foreground='white')
        subject_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        subject_entry = Entry(main_frame, textvariable=self.var_subject, width=20, font=('Quicksand', 12, 'italic'))
        subject_entry.grid(row=3, column=1, padx=10, stick=W)

        start_date_label = Label(main_frame, text="Start Date (in DD/MM/YYYY)", font=('Quicksand', 12), background='#58a4b0', foreground='white')
        start_date_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        start_date = Entry(main_frame, textvariable=self.var_startdate, width=20, font=('Quicksand', 12, 'italic'))
        start_date.grid(row=4, column=1, padx=10, stick=W)

        end_end_label = Label(main_frame, text="END Date (in DD/MM/YYYY)", font=('Quicksand', 12), background='#58a4b0', foreground='white')
        end_end_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        end_date = Entry(main_frame, textvariable=self.var_enddate, width=20, font=('Quicksand', 12, 'italic'))
        end_date.grid(row=5, column=1, padx=10, stick=W)

        gen_csv = Button(main_frame, command=self.req_file, text="Download Excel", font=('Quicksand', 12), bg="black", fg='white', width=15)
        gen_csv.grid(row=6, columnspan=2, pady=30)

        back_button_2 = Button(self.root,command=self.exit,text="Back",cursor="hand2",font=('Quicksand',15),bg='Black',fg='white')
        back_button_2.place(relx=0.1, rely=0.9, anchor='center',width=220,height=40)



   


    def req_file(self):
        # Read the CSV file
        df = pd.read_csv('atd.csv')
        
        # Convert 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
        
        # Group by specified columns and take the first occurrence of each group
        df_grouped = df.groupby(["Student ID", "Name", "Department", "Semester", "Division", "Teacher", "Subject", "Date"]).first().reset_index()
        
        # Pivot the dataframe to get attendance in date-wise columns
        new_df = df_grouped.pivot_table(index=["Student ID", "Name"], 
                                        columns='Date', 
                                        values='Attendance', 
                                        aggfunc='first').reset_index()
        
        # Convert 'Date' columns to string format in desired format
        new_df.columns = [col.strftime('%d-%B-%Y') if isinstance(col, pd.Timestamp) else col for col in new_df.columns]
        
        # Fill NaN values with 'Absent'
        new_df.fillna('Absent', inplace=True)

        date_columns = new_df.columns[2:]  # Exclude 'Student ID' and 'Name' columns
        new_df['Percentage Attendance'] = ((new_df[date_columns] == 'Present').sum(axis=1) / len(date_columns)) * 100
    

        if not os.path.exists('Attendance_Sheets'):
            os.makedirs('Attendance_Sheets')
    
    # Constructing the file path
        file_path = os.path.join('Attendance_Sheets', 
                                f"{self.var_teacher.get()}_{self.var_department.get()}_{self.var_division.get()}_{self.var_subject.get()}_"
                                f"{self.var_startdate.get().replace('/', '-')}_{self.var_enddate.get().replace('/', '-')}.xlsx")
            
        # Constructing the file name
        # file_name = (f"{self.var_teacher.get()}_{self.var_department.get()}_{self.var_division.get()}_{self.var_subject.get()}_"
        #             f"{self.var_startdate.get().replace('/', '-')}_{self.var_enddate.get().replace('/', '-')}.xlsx")
        
        # Export to Excel
        new_df.to_excel(file_path, index=False)
        messagebox.showinfo("Generated","Attendance Excel Generation is Successfully Done")


# Assuming this is a method in a class, we need to handle the 'self' parameter appropriately


# Assuming this is a method in a class, we need to handle the 'self' parameter appropriately

    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Excel(root)
    root.mainloop()