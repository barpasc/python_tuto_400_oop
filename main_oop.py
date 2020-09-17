#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk #GUI package
from tkinter import messagebox as msg
from classdb_oop import Database

# Instanciate databse object
db = Database('courses.db')

class Application(tk.Frame):
    """docstring for ."""

    def __init__(self, parent):
        super(Application, self).__init__(parent)
        self.parent = parent
        parent.title('Courses selections')
        #parent.geometry("700x350")
        parent.geometry('500x320+0+0') #Width x Height
        # Create widgets/grid
        self.create_widgets()
        self.selected_item = 0

    def create_widgets(self):
        ### FIRST NAME LABEL + ENTRY
        self.firstName_txt = tk.StringVar()
        self.firstName_lbl = tk.Label(self.parent, text='First Name', font=('bold'))
        self.firstName_lbl.place(x=20,y=10)
        self.firstName_entry = tk.Entry(self.parent, textvariable=self.firstName_txt)
        self.firstName_entry.place(x=120,y=10)

        ### LAST NAME LABEL + ENTRY
        self.lastName_txt = tk.StringVar()
        self.lastName_lbl = tk.Label(self.parent, text='Last Name', font=('bold'))
        self.lastName_lbl.place(x=20,y=40)
        self.lastName_entry = tk.Entry(self.parent, textvariable=self.lastName_txt)
        self.lastName_entry.place(x=120,y=40)

        ### AGE LABLE + ENTRY
        self.age_txt = tk.StringVar()
        self.age_lbl = tk.Label(self.parent, text='Age', font=('bold'))
        self.age_lbl.place(x=20,y=70)
        self.age_entry = tk.Entry(self.parent, textvariable=self.age_txt)
        self.age_entry.place(x=120,y=70)

        ### GENDER RADIO BTN
        self.gender_lbl = tk.Label(self.parent, text='Gender')
        self.gender_lbl.place(x=325,y=10)
        self.genderframe = tk.Frame(self.parent, relief="sunken", borderwidth = 1)
        self.rBtnGender = tk.IntVar()
        self.r1=tk.Radiobutton(self.genderframe, text='Male', variable=self.rBtnGender, value=1).pack(anchor=tk.W)
        self.r2=tk.Radiobutton(self.genderframe, text='Female', variable=self.rBtnGender, value=2).pack(anchor=tk.W)
        self.genderframe.place(x=325, y=35)

        ### COURSES LISTBOX
        self.Courses_lbl = tk.Label(self.parent, text='Course applied for', wraplength=90)
        self.Courses_lbl.place(x=20,y=150)
        self.coursesLBX = tk.Listbox(self.parent, width=27, height=7)
        self.coursesLBX.place(x=120, y=120)

        self.coursesList = ["Quality Management (Adv.)",
                            "Financial Management (Adv.)",
                            "Project Management (Adv.)",
                            "Project Management (Int.)"]

        for idx, item in enumerate(self.coursesList):
            self.coursesLBX.insert(tk.END, item)

        ### FORM BUTTONS
        self.btnFrame = tk.Frame(self.parent)
        self.btn_Prereq = tk.Button(self.btnFrame, text='Prerequisites', width=10, command=self.prereq).pack()
        self.btn_Save2db = tk.Button(self.btnFrame, text='Save to db', width=10, command=self.save2db).pack()
        self.btn_Clr = tk.Button(self.btnFrame, text='Clear fields', width=10, command=self.clearf).pack()
        self.btn_OpenDb = tk.Button(self.btnFrame, text='Open db', width=10, command=self.open_db).pack()
        self.btnFrame.place(x=350, y =120)

        ### PART TIME
        self.ptime_lbl = tk.Label(self.parent, text='')
        self.chkBtnPTime = tk.IntVar()
        self.chkbx_PTime = tk.Checkbutton(self.parent, text='Part time course', variable=self.chkBtnPTime, offvalue=0, onvalue=1)
        self.chkbx_PTime.place(x=20,y=290)


    def prereq(self):
        self.boo = 1

        if self.firstName_txt.get() == "":
            msg.showwarning("Missing information", "First name info missing")
            boo = 0
        elif self.lastName_txt.get() == "":
            msg.showwarning("Missing information", "Last name info missing")
            boo = 0
        elif self.age_txt.get() == "":
            msg.showwarning("Missing information", "Age info missing")
            boo = 0
        elif self.rBtnGender.get() == 0:
            msg.showwarning("Missing information", "Gender info missing")
            boo = 0

        if self.boo == 1:
            self.fname = self.firstName_txt.get()
            self.lname = self.lastName_txt.get()
            self.age = int(self.age_txt.get())

            self.selectedCourse = self.coursesLBX.get(self.coursesLBX.curselection())

            if self.age < 21:
                msg.showwarning("Invalid Age", "Invalid Age, you are not eligible")
                return
            elif self.age >= 21:
                pass

            ### SELECTED COURSE
            if self.selectedCourse == "Quality Management (Adv.)":
                self.prereq = "The prereq for this course is Quality Management (Int)."
                self.flag = 1
            elif self.selectedCourse == "Financial Management (Adv.)":
                self.prereq = "The prereq for this course is Financial Management (Bas)."
                self.flag= 1
            elif self.selectedCourse == "Project Management (Adv.)":
                self.prereq = "The prereq for this course is Project Management (Int)."
                self.flag = 0
            else:
                self.prereq = "The prereq for this course is Project Management (Bas)."
                self.flag = 0

            ### PART TIME
            if self.chkBtnPTime.get() == 1 and self.flag == 0:
                self.str2 = "\nThis course is not available part time."
            elif self.chkBtnPTime.get() == 1 and self.flag == 1:
                self.str2 = "\nThis course is available part time."
            else:
                self.str2 = ""

            self.result = self.prereq + self.str2
            msg.showinfo('Form info', self.result)


    def save2db(self):
        try:
            db.insert(self.fname, self.lname, self.age)
            msg.showinfo('DB action', "Selection inserted into db")
        except:
            msg.showinfo("Form submission failed", "Plz check ur input")

    def clearf(self):
        self.firstName_entry.delete(0, tk.END)
        self.lastName_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.coursesLBX.select_clear(self.coursesLBX.curselection())
        self.rBtnGender = 0
        self.chkBtnPTime = 0

    def open_db(self):
        self.parent.geometry('730x320+0+0')
        self.DbContent_lbl = tk.Label(self.parent, text='Course records')
        self.DbContent_lbl.place(x=480,y=10)
        self.DbContentLBX = tk.Listbox(self.parent, width=27, height=7)
        self.DbContentLBX.place(x=480, y=35)
        self.DbContentLBX.delete(0, tk.END)

        for row in db.fetch():
            self.DbContentLBX.insert(tk.END,row)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
