from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import pymysql
class Management:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Management ")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Employee Information  ",
                    font=("times new roman",20,"bold"),bg="Green",fg="white",relief=GROOVE,bd=5)
        title.pack(side=TOP,fill=X)
#=============image================================================
        self.camera_icon = ImageTk.PhotoImage(file="images/camera.png")

#=============variable====================================================

        self.Designation_var=StringVar()
        self.Id_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_No_var = StringVar()
        self.DOB_var = StringVar()
        self.DOJ_var = StringVar()
        self.NID_No_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()


        #=====Addp Frame===============================================
        Addp_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="gray")
        Addp_Frame.place(x=20,y=70,width=450,height=580)

        Addp_title = Label(Addp_Frame, text="Add Employee",bg="gray",fg="orange",
                      font=("times new roman",18, "bold"))
        Addp_title.grid(row=0,columnspan=2,pady=10,padx=150)
#============================================================================
        lbl_designation = Label(Addp_Frame, text="Designation",bg="gray",
                      font=("times new roman", 14, "bold"), fg="lightgreen",)
        lbl_designation.grid(row=1,column=0,padx=20,pady=5,sticky="w")

        txt_designation = Entry(Addp_Frame,textvariable=self.Designation_var, bd=2, relief=RIDGE,
                       font=("times new roman", 12,))
        txt_designation.grid(row=1, column=1, padx=25, pady=6, sticky="w")
#=============================================================================
        lbl_Id = Label(Addp_Frame, text="Id",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_Id.grid(row=2, column=0, padx=20, pady=6, sticky="w")

        txt_Id =Entry(Addp_Frame,bd=2,relief=RIDGE,textvariable=self.Id_var,
                       font=("times new roman", 12,))
        txt_Id.grid(row=2, column=1, padx=25, pady=6, sticky="w")
#======================================================================================
        lbl_name = Label(Addp_Frame, text="Name",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_name.grid(row=3, column=0, padx=20, pady=6, sticky="w")

        txt_name = Entry(Addp_Frame, bd=2, relief=RIDGE,textvariable=self.Name_var,
                       font=("times new roman", 12,))
        txt_name.grid(row=3, column=1, padx=25, pady=6, sticky="w")
#========================================================================================
        lbl_email = Label(Addp_Frame, text="Email",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_email.grid(row=4, column=0, padx=20, pady=6, sticky="w")

        txt_email = Entry(Addp_Frame, bd=2, relief=RIDGE,textvariable=self.Email_var,
                       font=("times new roman", 12,))
        txt_email.grid(row=4, column=1, padx=25, pady=6, sticky="w")
# ========================================================================================
        lbl_gender = Label(Addp_Frame, text="Gender",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_gender.grid(row=5, column=0, padx=20, pady=6, sticky="w")

        combo_gender = ttk.Combobox(Addp_Frame,textvariable=self.Gender_var,
                       font=("times new roman", 11,),state='readonly')
        combo_gender['values']=("Male","Female")
        combo_gender.grid(row=5, column=1, padx=25, pady=6, sticky="w")
#=============================================================================
        lbl_contact = Label(Addp_Frame, text="Contact No.",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_contact.grid(row=6, column=0, padx=20, pady=6, sticky="w")

        txt_contact = Entry(Addp_Frame, bd=2, relief=RIDGE,textvariable=self.Contact_No_var,
                       font=("times new roman", 12,))
        txt_contact.grid(row=6, column=1, padx=25, pady=6, sticky="w")
#===============================================================================
        lbl_dbo = Label(Addp_Frame, text="Date Of Birth",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_dbo.grid(row=7, column=0, padx=20, pady=6, sticky="w")

        txt_dbo = Entry(Addp_Frame, bd=2, relief=RIDGE,textvariable=self.DOB_var,
                       font=("times new roman", 12,))
        txt_dbo.grid(row=7, column=1, padx=25, pady=6, sticky="w")
#=================================================================================
        lbl_doj = Label(Addp_Frame, text="Date Of Joining",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_doj.grid(row=8, column=0, padx=20, pady=6, sticky="w")

        txt_doj = Entry(Addp_Frame, bd=2, relief=RIDGE,textvariable=self.DOJ_var,
                       font=("times new roman", 12,))
        txt_doj.grid(row=8, column=1, padx=25, pady=6, sticky="w")
#=================================================================================
        lbl_nid = Label(Addp_Frame, text="NID No.", bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_nid.grid(row=9, column=0, padx=20, pady=6, sticky="w")

        txt_nid = Entry(Addp_Frame, bd=2, relief=RIDGE,textvariable=self.NID_No_var,
                       font=("times new roman", 12,))
        txt_nid.grid(row=9, column=1, padx=25, pady=6, sticky="w")
#==================================================================================
        lbl_address = Label(Addp_Frame, text="Address",bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen" )
        lbl_address.grid(row=10, column=0, padx=20, pady=6, sticky="w")

        self.txt_address = Text(Addp_Frame,width=29,height=3,bd=2,
                       font=("times new roman", 11,))
        self.txt_address.grid(row=10, column=1, padx=20, pady=6, sticky="w")

#=======================Button===================================

        btn_Frame = Frame(Addp_Frame,relief=RIDGE, bg="gray",bd=3,
                       )
        btn_Frame.place(x=5,y=520,width=430,height=45)

        btn_add= Button(btn_Frame, text="Add ",width=10, relief=RIDGE, bg="green", bd=4,command=self.add_emp,
                        font=("times new roman", 10, "bold"),fg="white" ).grid(row=0,column=0,padx=10,pady=5)



        btn_cleare = Button(btn_Frame, text="Cleare", relief=RIDGE, bg="gray", bd=4,width=10,command=self.cleare,
                            font=("times new roman", 10, "bold"),fg="white" ).grid(row=0,column=1,padx=10,pady=5)

        btn_update = Button(btn_Frame, text="Update", relief=RIDGE, bg="gray", bd=4, width=10,command=self.update,
                            font=("times new roman", 10, "bold"),fg="white").grid(row=0, column=2, padx=10, pady=5)

        btn_delete = Button(btn_Frame, text="Delete", relief=RIDGE, bg="red", bd=4,width=10,command=self.delete,
                            font=("times new roman", 10, "bold"),fg="white" ).grid(row=0,column=3,padx=10,pady=5)






        #==========================Detail=============================================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
        Detail_Frame.place(x=500, y=70, width=800, height=400)

        lbl_search=Label(Detail_Frame,text="Search By >",bg="gray",fg="orange",
                         font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,padx=15,pady=5,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by, font=("times new roman", 12,),state='readonly')
        combo_search['values']=("Id","Name","Contact_No")
        combo_search.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        txt_search = Entry(Detail_Frame,width=25,textvariable=self.search_text, font=("times new roman", 12, "bold"),bd=2,relief=RIDGE)
        txt_search.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", relief=RIDGE, bg="green", bd=4, width=15,command=self.search_data,
                            font=("times new roman", 10, "bold"),fg="white").grid(row=0, column=3, padx=10, pady=5)
        showallbtn = Button(Detail_Frame, text="Show All", relief=RIDGE, bg="green", bd=4, width=15,command=self.fetch_data,
                            font=("times new roman", 10, "bold"), fg="white" ).grid(row=0, column=4, padx=10, pady=5)

#==================================Table Frame===============================================================
        Table_Frame = Frame(Detail_Frame, bd=3, relief=RIDGE, bg="white")
        Table_Frame.place(x=10, y=45, width=770, height=340)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Employee_table=ttk.Treeview(Table_Frame,columns=("Designation","Id","Name","Email","Gender","Contact No","D.O.B","D.O.J","NID No","Address")
                                    ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Employee_table.xview)
        scroll_y.config(command=self.Employee_table.yview)

        self.Employee_table.heading("Designation",text="Designation")
        self.Employee_table.heading("Id", text="Id")
        self.Employee_table.heading("Name", text="Name")
        self.Employee_table.heading("Email", text="Email")
        self.Employee_table.heading("Gender", text="Gender")
        self.Employee_table.heading("Contact No", text="Contact No")
        self.Employee_table.heading("D.O.B", text="D.O.B")
        self.Employee_table.heading("D.O.J", text="D.O.J")
        self.Employee_table.heading("NID No", text="NID No")
        self.Employee_table.heading("Address", text="Address")
        self.Employee_table['show']='headings'
        self.Employee_table.pack(fill=BOTH,expand=1)

        self.Employee_table.column("Designation",width=130)
        self.Employee_table.column("Id", width=35)
        self.Employee_table.column("Name", width=150)
        self.Employee_table.column("Email", width=190)
        self.Employee_table.column("Gender", width=50)
        self.Employee_table.column("Contact No", width=80)
        self.Employee_table.column("D.O.B", width=60)
        self.Employee_table.column("D.O.J", width=60)
        self.Employee_table.column("NID No", width=100)
        self.Employee_table.column("Address", width=350)

        self.Employee_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()






    #===========Photo management===================================================
        photo_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
        photo_Frame.place(x=500, y=480, width=440, height=170)

        lbl_photo = Label(photo_Frame, text="Capture Face", bg="gray", fg="orange",
                           font=("times new roman", 14, "bold"))
        lbl_photo.grid(row=0, columnspan=2, padx=30, pady=0, sticky="w")

        photo_add = Button(photo_Frame,height=120 ,width=140, relief=RIDGE, bg="lightgreen", bd=1,image=self.camera_icon,
                          ).grid(row=1, column=0, padx=20, pady=5)

        #photobtn = Button(photo_Frame, text="Add This photos", relief=RIDGE, bg="green", bd=3, width=20,
                            #font=("times new roman", 10, "bold"), fg="white").grid(row=1, column=1, padx=10, pady=10)

    #=================Show Department============================================
        Sdep_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
        Sdep_Frame.place(x=950, y=480, width=350, height=170)

#===================class==================================================
    def add_emp(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
        cur=con.cursor()
        cur.execute("insert into emp_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Designation_var.get(),
                                                                                      self.Id_var.get(),
                                                                                      self.Name_var.get(),
                                                                                      self.Email_var.get(),
                                                                                      self.Gender_var.get(),
                                                                                      self.Contact_No_var.get(),
                                                                                      self.DOB_var.get(),
                                                                                      self.DOJ_var.get(),
                                                                                      self.NID_No_var.get(),
                                                                                      self.txt_address.get('1.0',END),



                                                                                      ))
        con.commit()
        self.fetch_data()
        self.cleare()
        con.close()


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("select * from emp_table")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Employee_table.delete(*self.Employee_table.get_children())
            for row in rows:
                self.Employee_table.insert('',END,values=row)
            con.commit()
            con.close()

    def cleare (self):
        self.Designation_var.set(""),
        self.Id_var.set(""),
        self.Name_var.set(""),
        self.Email_var.set(""),
        self.Gender_var.set(""),
        self.Contact_No_var.set(""),
        self.DOB_var.set(""),
        self.DOJ_var.set(""),
        self.NID_No_var.set(""),
        self.txt_address.delete('1.0', END)


    def get_cursor(self,sh):
        cursor_row=self.Employee_table.focus()
        contents=self.Employee_table.item(cursor_row)
        row=contents['values']
        self.Designation_var.set(row[0]),
        self.Id_var.set(row[1]),
        self.Name_var.set(row[2]),
        self.Email_var.set(row[3]),
        self.Gender_var.set(row[4]),
        self.Contact_No_var.set(row[5]),
        self.DOB_var.set(row[6]),
        self.DOJ_var.set(row[7]),
        self.NID_No_var.set(row[8]),
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[9])

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("update emp_table set Designation=%s,Name=%s,Email=%s,Gender=%s,"
                    "Contact_No=%s,DOB=%s,DOJ=%s,NID_No=%s,Address=%s where Id=%s",
                                                                                    (self.Designation_var.get(),

                                                                                    self.Name_var.get(),
                                                                                    self.Email_var.get(),
                                                                                    self.Gender_var.get(),
                                                                                    self.Contact_No_var.get(),
                                                                                    self.DOB_var.get(),
                                                                                    self.DOJ_var.get(),
                                                                                    self.NID_No_var.get(),
                                                                                    self.txt_address.get('1.0', END),
                                                                                    self.Id_var.get()

                                                                                    ))
        con.commit()
        self.fetch_data()
        self.cleare()
        con.close()

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("delete from emp_table where Id=%s",self.Id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.cleare()


    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("select * from emp_table where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Employee_table.delete(*self.Employee_table.get_children())
            for row in rows:
                self.Employee_table.insert('',END,values=row)
            con.commit()
            con.close()



root=Tk()
ob=Management(root)
root.mainloop()
