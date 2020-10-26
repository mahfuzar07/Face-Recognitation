from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #=====Image============
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="images/download.png")
        #======variables=========
        self.uname=StringVar()
        self.pass_=StringVar()


        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title=Label(self.root,text="Advance GUI Face Recognition Attendence System",font=("times new roman",40,"bold"),bg="red",fg="white",bd=10)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=450,y=120)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=1,columnspan=2 ,pady=0)
        txtlbl = Label(Login_Frame,text="Admin Login",width=13, bd=5,bg="gray",font=("times new roman", 40, "bold"),fg="orange").grid(row=0, columnspan=2, pady=10)

        lbluser=Label(Login_Frame,text="Username",compound=LEFT,
                      font=("times new roman", 20, "bold")).grid(row=2,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=2, column=1, padx=20)

        lblpass = Label(Login_Frame, text="Password",compound=LEFT,
                        font=("times new roman", 20, "bold")).grid(row=3, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, relief=GROOVE,textvariable=self.pass_, font=("", 15)).grid(row=3, column=1, padx=20)



        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,
                       font=("times new roman",14,"bold"),bg="green",fg="white").grid(row=4,column=1,pady=10)


    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        elif self.uname.get()=="shovon" and self.pass_.get()=="12345":
            messagebox.showinfo("Login Successfull",f"Welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid username or password")










root=Tk()
obj=Login_System(root)
root.mainloop()