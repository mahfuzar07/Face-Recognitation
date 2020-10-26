from tkinter import *
from PIL import ImageTk
class After_login:
    def __init__(self,root):
        self.root=root
        self.root.title("Feature")
        self.root.geometry("1350x700+0+0")

#==================images===============================================
        self.emp_icon = ImageTk.PhotoImage(file="images/emp.png")
        self.train_icon = ImageTk.PhotoImage(file="images/train.png")
        self.report_icon = ImageTk.PhotoImage(file="images/report.png")
        self.about_icon = ImageTk.PhotoImage(file="images/about.jpg")
        self.Exit_icon = ImageTk.PhotoImage(file="images/Exit.png")


#=================================================================================================
        title = Label(self.root, text="Advance GUI Face Recognition Attendence System",
                      font=("times new roman", 40, "bold"), bg="lightgreen", fg="orange", bd=10)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=450, y=120)
#============================Feature==============================================
        Feature_Frame = Frame(self.root, bd=1, relief=RIDGE, bg="gray")
        Feature_Frame.place(x=75, y=100, width=1200, height=580)

#=============================Employee Section=============================================
        photo_Frame = Frame(Feature_Frame, bd=4, relief=RIDGE, bg="gray")
        photo_Frame.place(x=50, y=50, width=300, height=220)

        lbl_photo = Label(photo_Frame, text="Employee Management", bg="gray", fg="orange",
                           font=("times new roman", 18, "bold"))
        lbl_photo.grid(row=0, columnspan=2, padx=25, pady=0, sticky="w")

        emp_btn = Button(photo_Frame,height=160 ,width=250, relief=GROOVE, bg="gray", bd=2,image=self.emp_icon,command=self.root
                          ).grid(row=1, column=0, padx=20, pady=5)

#=======================Train System==============================

        photo_Frame = Frame(Feature_Frame, bd=4, relief=RIDGE, bg="gray")
        photo_Frame.place(x=450, y=50, width=300, height=220)

        lbl_photo = Label(photo_Frame, text="Train system", bg="gray", fg="orange",
                          font=("times new roman", 18, "bold"))
        lbl_photo.grid(row=0, columnspan=2, padx=80, pady=0, sticky="w")

        train_btn = Button(photo_Frame, height=160, width=250, relief=GROOVE, bg="gray", bd=2,image=self.train_icon,
                           ).grid(row=1, column=0, padx=20, pady=5)
#=========================Attendance Report==============================

        photo_Frame = Frame(Feature_Frame, bd=4, relief=RIDGE, bg="gray")
        photo_Frame.place(x=850, y=50, width=300, height=220)

        lbl_photo = Label(photo_Frame, text="Attendance Report", bg="gray", fg="orange",
                          font=("times new roman", 18, "bold"))
        lbl_photo.grid(row=0, columnspan=2, padx=40, pady=0, sticky="w")

        report_btn = Button(photo_Frame, height=160, width=250, relief=GROOVE, bg="gray", bd=2,image=self.report_icon
                           ).grid(row=1, column=0, padx=20, pady=5)
#=============================================================
        photo_Frame = Frame(Feature_Frame, bd=4, relief=RIDGE, bg="gray")
        photo_Frame.place(x=50, y=300, width=300, height=220)

        lbl_photo = Label(photo_Frame, text="Employee Management", bg="gray", fg="orange",
                          font=("times new roman", 18, "bold"))
        lbl_photo.grid(row=0, columnspan=2, padx=20, pady=0, sticky="w")

        photo_add = Button(photo_Frame, height=160, width=250, relief=GROOVE, bg="gray", bd=2,image=self.train_icon
                           ).grid(row=1, column=0, padx=20, pady=5)
#============================About System======================================
        photo_Frame = Frame(Feature_Frame, bd=4, relief=RIDGE, bg="gray")
        photo_Frame.place(x=450, y=300, width=300, height=220)

        lbl_photo = Label(photo_Frame, text="About", bg="gray", fg="orange",
                          font=("times new roman", 18, "bold"))
        lbl_photo.grid(row=0, columnspan=2, padx=120, pady=0, sticky="w")

        about_btn = Button(photo_Frame, height=160, width=250, relief=GROOVE, bg="gray", bd=2,image=self.about_icon
                           ).grid(row=1, column=0, padx=20, pady=5)


#=============================Exit==========================================

        photo_Frame = Frame(Feature_Frame, bd=4, relief=RIDGE, bg="gray")
        photo_Frame.place(x=850, y=300, width=300, height=220)

        lbl_photo = Label(photo_Frame, text="Exit", bg="gray", fg="orange",
                          font=("times new roman", 18, "bold"))
        lbl_photo.grid(row=0, columnspan=2, padx=120, pady=0, sticky="w")

        exit_btn = Button(photo_Frame, height=150, width=250, relief=GROOVE, bg="red", bd=2,image=self.Exit_icon
                           ).grid(row=1, column=0, padx=20, pady=5)









root = Tk()
obj = After_login(root)
root.mainloop()