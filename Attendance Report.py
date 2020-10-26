from tkinter import *
from tkinter import ttk

import pymysql
class Report:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance Report ")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Attendance Report  ",
                    font=("times new roman",20,"bold"),bg="Green",fg="white",relief=GROOVE,bd=5)
        title.pack(side=TOP,fill=X)


#=============variable====================================================

        self.Designation_var=StringVar()
        self.Id_var = StringVar()
        self.Name_var = StringVar()
        self.Attendance_Status_var = StringVar()
        self.Date_var = StringVar()
        self.Time_var = StringVar()


        self.search_by = StringVar()
        self.search_text = StringVar()


        #=====Att Frame===============================================
        at_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="gray")
        at_Frame.place(x=20,y=70,width=400,height=280)

        at_title = Label(at_Frame, text="Manage Attendance",bg="gray",fg="orange",
                      font=("times new roman",18, "bold"))
        at_title.grid(row=0,columnspan=2,pady=10,padx=100)
#============================excle frame================================================
        ex_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
        ex_Frame.place(x=20, y=355, width=400, height=290)

        ex_title = Label(ex_Frame, text="Export in Excel File", bg="gray", fg="orange",
                         font=("times new roman", 18, "bold"))
        ex_title.grid(row=0, columnspan=2, pady=10, padx=5)

        lbl_date = Label(ex_Frame, text="Date (dd/mm/yyyy)", bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_date.grid(row=1, column=0, padx=10, pady=6, sticky="w")

        txt_date = Entry(ex_Frame, bd=2, relief=RIDGE, textvariable=self.Date_var,
                         font=("times new roman", 12,))
        txt_date.grid(row=1, column=1, padx=15, pady=6, sticky="w")

        btn_cleare = Button(ex_Frame, text="Export as Current", width=15,
                         font=("times new roman", 12, "bold"), bg="green", fg="white").grid(row=2, column=0,padx=5, pady=5)
        btn_update = Button(ex_Frame, text="Export as Enters", width=15,
                            font=("times new roman", 12, "bold"), bg="green", fg="white").grid(row=2, column=1,padx=1, pady=5)
        btn_update = Button(ex_Frame, text="Delete Attendance Report", width=20,
                            font=("times new roman", 12, "bold"), bg="Red", fg="white").grid(row=3, columnspan=2, padx=1,
                                                                                               pady=5)




        # =============================================================================
        lbl_Id = Label(at_Frame, text="Id", bg="gray",
                       font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_Id.grid(row=1, column=0, padx=10, pady=6, sticky="w")

        txt_Id = Entry(at_Frame, bd=2, relief=RIDGE, textvariable=self.Id_var,
                       font=("times new roman", 12,))
        txt_Id.grid(row=1, column=1, padx=15, pady=6, sticky="w")
        # ======================================================================================
        lbl_name = Label(at_Frame, text="Name", bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_name.grid(row=2, column=0, padx=10, pady=6, sticky="w")

        txt_name = Entry(at_Frame, bd=2, relief=RIDGE, textvariable=self.Name_var,
                         font=("times new roman", 12,))
        txt_name.grid(row=2, column=1, padx=15, pady=6, sticky="w")
        # ========================================================================================
        lbl_date = Label(at_Frame, text="Date (dd/mm/yyyy)", bg="gray",
                         font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_date.grid(row=3, column=0, padx=10, pady=6, sticky="w")

        txt_date = Entry(at_Frame, bd=2, relief=RIDGE, textvariable=self.Date_var,
                         font=("times new roman", 12,))
        txt_date.grid(row=3, column=1, padx=15, pady=6, sticky="w")

#==========================================================================================================
        lbl_Attendance = Label(at_Frame, text="Attendance Status", bg="gray",
                           font=("times new roman", 14, "bold"), fg="lightgreen", )
        lbl_Attendance.grid(row=4, column=0, padx=10, pady=6, sticky="w")

        combo_Attendance = ttk.Combobox(at_Frame, textvariable=self.Attendance_Status_var,
                                    font=("times new roman", 11,), state='readonly')
        combo_Attendance['values'] = ("Present", "Absent")
        combo_Attendance.grid(row=4, column=1, padx=15, pady=6, sticky="w")
        # =============================================================================





#=======================Button===================================

        ebtnat_Frame = Frame(at_Frame,relief=RIDGE, bg="gray",bd=3,
                       )
        ebtnat_Frame.place(x=15,y=220,width=360,height=45)

        #btn_add= Button(btn_Frame, text="Add ",width=10, relief=RIDGE, bg="green", bd=4,command=self.add_emp,
                        #font=("times new roman", 10, "bold"),fg="white" ).grid(row=0,column=0,padx=10,pady=5)



        btn_cleare = Button(ebtnat_Frame, text="Cleare", relief=RIDGE, bg="green", bd=4,width=10,command=self.cleare,
                            font=("times new roman", 10, "bold"),fg="white" ).grid(row=0,column=1,padx=25,pady=5)

        btn_update = Button(ebtnat_Frame, text="Update", relief=RIDGE, bg="green", bd=4, width=10,command=self.update,
                            font=("times new roman", 10, "bold"),fg="white").grid(row=0, column=2, padx=100, pady=5)

       # btn_delete = Button(btn_Frame, text="Delete", relief=RIDGE, bg="red", bd=4,width=10,command=self.delete,
                            #font=("times new roman", 10, "bold"),fg="white" ).grid(row=0,column=3,padx=10,pady=5)






        #==========================Detail=============================================
        Detailat_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
        Detailat_Frame.place(x=450, y=70, width=870, height=580)

        lbl_search=Label(Detailat_Frame,text="Search By >",bg="gray",fg="orange",
                         font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,padx=15,pady=5,sticky="w")

        combo_search=ttk.Combobox(Detailat_Frame,width=10,textvariable=self.search_by, font=("times new roman", 12,),state='readonly')
        combo_search['values']=("Id","Name","Contact_No")
        combo_search.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        txt_search = Entry(Detailat_Frame,width=25,textvariable=self.search_text, font=("times new roman", 12, "bold"),bd=2,relief=RIDGE)
        txt_search.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        Searchbtn = Button(Detailat_Frame, text="Search", relief=RIDGE, bg="green", bd=4, width=15,command=self.search_data,
                            font=("times new roman", 10, "bold"),fg="white").grid(row=0, column=3, padx=10, pady=5)
        showallbtn = Button(Detailat_Frame, text="Show All", relief=RIDGE, bg="green", bd=4, width=15,command=self.fetch_data,
                            font=("times new roman", 10, "bold"), fg="white" ).grid(row=0, column=4, padx=10, pady=5)

#==================================Table Frame===============================================================
        Table_Frame = Frame(Detailat_Frame, bd=3, relief=RIDGE, bg="white")
        Table_Frame.place(x=10, y=45, width=840, height=525)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.report_table=ttk.Treeview(Table_Frame,columns=("Designation","Id","Name","Attendance_Status","Date","Time")
                                    ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.report_table.xview)
        scroll_y.config(command=self.report_table.yview)

        self.report_table.heading("Designation",text="Designation")
        self.report_table.heading("Id", text="Id")
        self.report_table.heading("Name", text="Name")
        self.report_table.heading("Attendance_Status", text="Attendance_Status")
        self.report_table.heading("Date", text="Date")
        self.report_table.heading("Time", text="time")

        self.report_table['show']='headings'
        self.report_table.pack(fill=BOTH,expand=1)

        self.report_table.column("Designation",width=130)
        self.report_table.column("Id", width=35)
        self.report_table.column("Name", width=150)
        self.report_table.column("Attendance_Status", width=190)
        self.report_table.column("Date", width=50)
        self.report_table.column("Time", width=80)


        self.report_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()





#===================class==================================================
    def add_emp(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
        cur=con.cursor()
        cur.execute("insert into rep_table values(%s,%s,%s,%s,%s,%s)",(self.Designation_var.get(),
                                                                                      self.Id_var.get(),
                                                                                      self.Name_var.get(),
                                                                                      self.Attendance_Status_var.get(),
                                                                                      self.Date_var.get(),
                                                                                      self.Time_var.get(),

                                                                                      ))
        con.commit()
        self.fetch_data()
        self.cleare()
        con.close()


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("select * from rep_table")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.report_table.delete(*self.report_table.get_children())
            for row in rows:
                self.report_table.insert('',END,values=row)
            con.commit()
            con.close()

    def cleare (self):
        self.Designation_var.set(""),
        self.Id_var.set(""),
        self.Name_var.set(""),
        self.Attendance_Status_var.set(""),
        self.Date_var.set(""),
        self.Time_var.set(""),



    def get_cursor(self,sh):
        cursor_row=self.report_table.focus()
        contents=self.report_table.item(cursor_row)
        row=contents['values']

        self.Id_var.set(row[1]),
        self.Name_var.set(row[2]),
        self.Date_var.set(row[4]),
        self.Attendance_Status_var.set(row[3]),




    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("update rep_table set Designation=%s,Name=%s,Attendance_Status=%s,"" where Id=%s",
                                                                                    (self.Designation_var.get(),

                                                                                    self.Name_var.get(),
                                                                                    self.Attendance_Status_var.get(),
                                                                                    self.Date_var.get(),
                                                                                    self.Time_var.get(),
                                                                                    self.Id_var.get()

                                                                                    ))
        con.commit()
        self.fetch_data()
        self.cleare()
        con.close()

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("delete from rep_table where Id=%s",self.Id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.cleare()


    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee")
        cur = con.cursor()
        cur.execute("select * from rep_table where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.report_table.delete(*self.report_table.get_children())
            for row in rows:
                self.report_table.insert('',END,values=row)
            con.commit()
            con.close()



root=Tk()
ob=Report(root)
root.mainloop()
