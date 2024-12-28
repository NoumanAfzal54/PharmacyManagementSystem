from tkinter import *  # Importing Tkinter
from PIL import Image , ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class PharmacyManagementSystem: 
    def __init__(self, root):  # Constructor(init) its automatically called when a object is created
        self.root = root # root refers as window and self refers as instance of class allowing you to access its attributes and methods
        lbltitle=Label(self.root ,
                        text="PHARMACY MANAGEMENT SYSTEM" ,
                         bd=15 , 
                         relief=RIDGE,
                         bg="white",
                         fg="darkgreen",
                         font=("Times New Roman" , 45 , "bold"),
                         padx=4,
                         pady=4)
        lbltitle.pack(side=TOP,fill=X) #used to place elements inside a window or frame top,left,right,bottom anywhere
        img1 = Image.open("logo.jpg")
        img1 = img1.resize((63,63))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=20,y=20)
        #self.root mae humne button banaya


        #===================Addmedvariable==================
        self.addmed_var = StringVar() #for addding a medicine we are creating a variable
        self.refmed_var=StringVar()#for addding a reference we are creating a variable
        #========================DataFrame======================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1290,height=400)
        
        DataFrameleft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("times new roman",12,"bold"))
        DataFrameleft.place(x=0,y=5,width=900,height=350)
         
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=300,height=350)
        #==================ButtonFrame==============
         
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)
        
        #==================Main Buttons====================
        def add_info_to_main_table():
         if referncecombobox.get() == "" or lotentry.get() == "":
            messagebox.showwarning("Warning","Please fill all the fields")
         else:
          try:
            con = mysql.connector.connect(host="localhost" , username = "root" , password="case1234tor" , database="pharmacymanagementsystem")
            my_cursor = con.cursor()
            query = "Insert into pharmacy(Ref_no,CmpName,TypeMed,medname,LotNo,Issuedate,Expdate,uses,Sideeffect,warning,dosage,Price,product)  Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (referncecombobox.get(),cmpentry.get(),typemedcombobox.get(),lblmednamecombobox.get(),lotentry.get(),lblissuedatentry.get(),lblexpentry.get(),lblusesentry.get(),lblseentry.get(),lblwarningentry.get(),lbldosageentry.get(),lbltpentry.get(),lblprqtentry.get())
            my_cursor.execute(query , values)
            con.commit()
            con.close()
            messagebox.showinfo("Success","Added Successfully")


            #=====================Fetch_query========================

            con = mysql.connector.connect(host="localhost" , username = "root" , password="case1234tor" , database="pharmacymanagementsystem")
            my_cursor = con.cursor()
            query = "Select *from pharmacy"
            my_cursor.execute(query)
            rows = my_cursor.fetchall()
            for row in rows:
                 self.pharmacy_table.insert('','end',values=(row))
            con.commit()
            con.close()   
          except mysql.connector.Error:
            messagebox.showerror("Failed","Values not added in the database")

            #=====================maintableupdate========================

      #   def update_table1():
         
      #       con=mysql.connector.connect(host="localhost" , user = "root" , password = "case1234tor" , database = "pharmacymanagementsystem")
      #       my_cursor = con.cursor()
      #       messagebox.showinfo("Update","Enter lotno to  update credentials")
      #       queries = [
      #       ("UPDATE pharmacy SET Ref_no = %s WHERE LotNo = %s", (ref_no, lot_no)),
      #       ("UPDATE pharmacy SET CmpName = %s WHERE LotNo = %s", (cmp_name, lot_no)),
      #       ("UPDATE pharmacy SET Typemed = %s WHERE LotNo = %s", (typemed, lot_no)),
      #       ("UPDATE pharmacy SET medname = %s WHERE LotNo = %s", (medname, lot_no)),
      #       ("UPDATE pharmacy SET LotNo = %s WHERE LotNo = %s", (new_lotno, lot_no)),
      #       ("UPDATE pharmacy SET Issuedate = %s WHERE LotNo = %s", (issuedate, lot_no)),
      #       ("UPDATE pharmacy SET Expdate = %s WHERE LotNo = %s", (expdate, lot_no)),
      #       ("UPDATE pharmacy SET uses = %s WHERE LotNo = %s", (uses, lot_no)),
      #       ("UPDATE pharmacy SET Sideeffect = %s WHERE LotNo = %s", (sideeffect, lot_no)),
      #       ("UPDATE pharmacy SET warning = %s WHERE LotNo = %s", (warning, lot_no)),
      #       ("UPDATE pharmacy SET dosage = %s WHERE LotNo = %s", (dosage, lot_no)),
      #       ("UPDATE pharmacy SET Price = %s WHERE LotNo = %s", (price, lot_no)),
      #       ("UPDATE pharmacy SET product = %s WHERE LotNo = %s", (product, lot_no)),
      #   ]
      #       values=lotentry.get()
      #       my_cursor.execute(query , values)
      #       con.commit()
      #       con.close()
      #       messagebox.showerror("Success" , "Updated Successfully")

        def deletemed1():
            if referncecombobox.get() == "":
               messagebox.showerror("Error" , "Provide refno for deletion")
            else:   
             try:
              conn=mysql.connector.connect(host = "localhost" ,user="root" , password = "case1234tor" , database="pharmacymanagementsystem")
              cursor=conn.cursor()
              query="delete from pharmacy where Ref_no = %s"
              query1="delete from pharma where Ref_no = %s"
              values=(referncecombobox.get(),)
            #   cursor.execute(query1 , values )
              cursor.execute(query , values) 
              print(f"Attempting to delete Ref:{values}")
              conn.commit()
              messagebox.showinfo("Deleted" , "Values deleted successfully")
             except mysql.connector.Error:
               messagebox.showerror("Error" , "Value not deleted")

        
        def reset():
           cmpentry.delete(0,'end')
           lotentry.delete(0,'end')
           lblissuedatentry.delete(0,"end")
           lblexpentry.delete(0,"end")
           lblusesentry.delete(0,"end")
           lblseentry.delete(0,"end")
           lblwarningentry.delete(0,"end")
           lbldosageentry.delete(0,"end")
           lbltpentry.delete(0,"end")
           lblprqtentry.delete(0,"end")

        def search():
           conn=mysql.connector.connect(host = "localhost" ,user="root" , password = "case1234tor" , database="pharmacymanagementsystem")
           cursor=conn.cursor()
           if txtSearch.get() == "":
             messagebox.showerror("Error","Input data to search")
           try:
              query="select *from pharmacy where Ref_no = %s"
              values = (txtSearch.get(),)
              cursor.execute(query , values)
              rows = cursor.fetchall()
              self.pharmacy_table.delete(*self.pharmacy_table.get_children())

              for i in rows:
                self.pharmacy_table.insert('',"end",values=i)

              conn.commit()
              conn.close()

           except mysql.connector.Error as e:
               print(f"Error {e}")

        def show():
         try:
            conn=mysql.connector.connect(host = "localhost" ,user="root" , password = "case1234tor" , database="pharmacymanagementsystem")
            cursor=conn.cursor()
            query="select *from pharmacy"
            cursor.execute(query)
            rows = cursor.fetchall()

            for i in rows:
                self.pharmacy_table.insert('',"end",values=i)

            conn.commit()
            conn.close()

         except mysql.connector.Error as e:
               print(f"Error {e}")
           
        def exit():
         self.root.destroy()
         print("Exiting the system")

         

 




        btnAddData=Button(ButtonFrame,text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen", fg="white",width=11,command=add_info_to_main_table)
        btnAddData.grid(row=0,column=0) 

        btnUpdateMedicine=Button(ButtonFrame,text="Update",font=("arial",12,"bold"),bg="darkgreen", fg="white",width=9)
        btnUpdateMedicine.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,text="Delete",font=("arial",12,"bold"),bg="Red", fg="white",width=9,command=deletemed1)
        btnDeleteMed.grid(row=0,column=2) 

        btnResetMed=Button(ButtonFrame,text="Reset",font=("arial",12,"bold"),bg="darkgreen", fg="white",width=9,command=reset)
        btnResetMed.grid(row=0,column=3) 

        btnExitMed=Button(ButtonFrame,text="Exit",font=("arial",12,"bold"),bg="darkgreen", fg="white",width=9,command=exit)
        btnExitMed.grid(row=0,column=4) 

        lblSearch=Label(ButtonFrame,font=("arial" , 17 , "bold"),text="Search by",padx=2,bg="red",fg="white",width=9)
        lblSearch.grid(row=0 , column=5 , sticky=W)

        search_combo=ttk.Combobox(ButtonFrame ,width=12,font=("arial" , 13 , "bold"),state="readonly")
        search_combo["values"]=("Ref" , "Medicinename" , "Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame , bd=3,relief=RIDGE,width=15)
        txtSearch.grid(row=0,column=7)

        searchbutton=Button(ButtonFrame ,text="Search",width=14,font=("arial" , 13 , "bold"),bg="darkgreen", fg="white",command=search)
        searchbutton.grid(row=0,column=8)

        showall=Button(ButtonFrame ,text="Show",width=14,font=("arial" , 13 , "bold"),bg="darkgreen", fg="white",command=show)
        showall.grid(row=0,column=9)

        #==========label and entry===================
         
        lblrefno=Label(DataFrameleft ,text="Refrence No",width=14,font=("arial" , 12 , "bold"))
        lblrefno.grid(row=0,column=0,sticky=W)

        referncecombobox=ttk.Combobox(DataFrameleft , font=("arial" , 12 , "bold") ,state="readonly" , width=27)
        

        query="select Ref from pharma"
        con=mysql.connector.connect(host="localhost" , username="root" , password="case1234tor" , database="pharmacymanagementsystem") #these four parameters are must
        my_cursor=con.cursor()
        query="select Ref from pharma"
        my_cursor.execute(query)
        row=my_cursor.fetchall()

        
        referncecombobox['values']=row
        referncecombobox.grid(row=0,column=1)
        referncecombobox.current(0)

        lblcomname=Label(DataFrameleft,text="Company Name" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lblcomname.grid(row=1,column= 0,sticky=W)

        cmpentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        cmpentry.grid(row=1,column=1)

        lbltypemed=Label(DataFrameleft ,text="Type of medicine",width=14,font=("arial" , 12 , "bold"),padx=2 , pady=6)
        lbltypemed.grid(row=2,column=0,sticky=W)

        typemedcombobox=ttk.Combobox(DataFrameleft , font=("arial" , 12 , "bold") ,state="readonly" , width=27)
        typemedcombobox['values']=["Tablet" , "Liquid" , "Capsules" ,"Topical Medicines" , "Drops" , "Inhales" , "Injection"]
        typemedcombobox.grid(row=2,column=1)
        typemedcombobox.current(0)

        query="select medname from pharma"
        con=mysql.connector.connect(host="localhost" , username="root" , password="case1234tor" , database="pharmacymanagementsystem") #these four parameters are must
        my_cursor=con.cursor()
        my_cursor.execute(query)
        row=my_cursor.fetchall()

        lblmedname=Label(DataFrameleft ,text="Medicine Name",width=14,font=("arial" , 12 , "bold"),padx=2 , pady=6)
        lblmedname.grid(row=3,column=0,sticky=W)

        lblmednamecombobox=ttk.Combobox(DataFrameleft , font=("arial" , 12 , "bold") ,state="readonly" , width=27)
        lblmednamecombobox['values']=row
        lblmednamecombobox.grid(row=3,column=1)
        lblmednamecombobox.current(0)


        lbllot=Label(DataFrameleft,text="Lot No" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lbllot.grid(row=4,column= 0,sticky=W)

        lotentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lotentry.grid(row=4,column=1) 
        
        lblissuedate=Label(DataFrameleft,text="Issue Date" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lblissuedate.grid(row=5,column= 0,sticky=W)

        lblissuedatentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lblissuedatentry.grid(row=5,column=1)

        lblexp=Label(DataFrameleft,text="Exp Date" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lblexp.grid(row=6,column= 0,sticky=W)

        lblexpentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lblexpentry.grid(row=6,column=1)

        lbluses=Label(DataFrameleft,text="Uses" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lbluses.grid(row=7,column= 0,sticky=W)

        lblusesentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lblusesentry.grid(row=7,column=1)

        lblse=Label(DataFrameleft,text="Side Effect" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lblse.grid(row=8,column= 0,sticky=W)

        lblseentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lblseentry.grid(row=8,column=1)


        lblwarning=Label(DataFrameleft,text="Prec&Warning" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lblwarning.grid(row=0,column= 2,sticky=W)

        lblwarningentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lblwarningentry.grid(row=0,column=3)


        lbldosage=Label(DataFrameleft,text="Dosage" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lbldosage.grid(row=1,column= 2,sticky=W)

        lbldosageentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lbldosageentry.grid(row=1,column=3)

        lbltp=Label(DataFrameleft,text="Tablet Price" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lbltp.grid(row=2,column= 2,sticky=W)

        lbltpentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lbltpentry.grid(row=2,column=3)

        lblprqt=Label(DataFrameleft,text="Product QT" , font=("arial" , 12 , "bold"),width=14,padx=2 , pady=6)
        lblprqt.grid(row=3,column= 2,sticky=W)

        lblprqtentry=Entry(DataFrameleft ,bd=3 , relief="ridge" , width=40)
        lblprqtentry.grid(row=3,column=3)


        #================Images==============

        lblsafe=Label(DataFrameleft,text="Stay Home Stay Safe" , font=("times new roman",   15,"bold"),width=16 , bg="white" , fg="red")
        lblsafe.place(x=590,y=150)

        img2=Image.open("img2.jpeg")
        img2=img2.resize((150,150))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(self.root , image=self.photoimg2,borderwidth=0)
        b2.place(x=500,y=340)

        img3=Image.open("img3.jpeg")
        img3=img3.resize((150,150))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(self.root , image=self.photoimg3,borderwidth=0)
        b3.place(x=640,y=340)

        img4=Image.open("img4.jpeg")
        img4=img4.resize((135,150))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b4=Button(self.root , image=self.photoimg4,borderwidth=0)
        b4.place(x=790,y=340)

        #====================Add Medicine Functionality Declaration==============

        def addMed():
            try:
             con=mysql.connector.connect(host="localhost" , username="root" , password="case1234tor" , database="pharmacymanagementsystem") #these four parameters are must
             my_cursor=con.cursor() #creating a cursor that points to location
             sql_query = "INSERT INTO pharma (Ref, medname) VALUES (%s, %s)"             
             values = (lblrefnumberbox.get() ,lblmedicinename1.get())
             my_cursor.execute(sql_query , values)
             con.commit()
             messagebox.showinfo("Success", "Medicine Added")
             lblrefnumberbox.delete(0 , "end")
             lblmedicinename1.delete(0 , "end") #0 specifies the staring point of data and end the last point of data


             #===============Fetching Query============
             fetch_query="select Ref , medname from pharma"
             my_cursor.execute(fetch_query)
             rows = my_cursor.fetchall()
             for row in rows:
                 self.medicine_table.insert('','end',values=(row))
            except mysql.connector.Error as err:
               if err.errno == 1062:
                  messagebox.showwarning("Duplicate","This item already exists")
               else:
                 print(f"Error: {err}")
                 
                #=================UpdateData==========================
        def update_data():
            if lblmedicinename1.get() == "" and lblrefnumberbox.get() == "":
               messagebox.showerror("Error" , "Fill in the fields")
            else:
             try:
              con=mysql.connector.connect(
                 host = "localhost",
                 user = "root",
                 password = "case1234tor",
                 database = "pharmacymanagementsystem"
              )    
              cursor = con.cursor()
              messagebox.showinfo("Update","Enter the data to update")
              query = "update pharma set medname = %s where Ref = %s" 
              values = (lblmedicinename1.get(), lblrefnumberbox.get()) 
              cursor.execute(query , values)
              con.commit()
              messagebox.showinfo("Updated" , "Values updated successfully")
              lblrefnumberbox.delete(0,"end")
              lblmedicinename1.delete(0,"end")
             except mysql.connector.Error:
               messagebox.showerror("Error" , "Value is not updated")
       

             #=================Deletemed==========================

        def deletemed():
            if lblrefnumberbox.get() == "":
               messagebox.showerror("Error" , "Provide refno for deletion")
            else:   
             try:
              conn=mysql.connector.connect(host = "localhost" ,user="root" , password = "case1234tor" , database="pharmacymanagementsystem")
              cursor=conn.cursor()
              query="delete from pharma where Ref = %s"
              values=(lblrefnumberbox.get(),)
              cursor.execute(query , values) 
              print(f"Attempting to delete Ref:{values}")
              conn.commit()
              messagebox.showinfo("Deleted" , "Values deleted successfully")
              lblrefnumberbox.delete(0,"end")
             except mysql.connector.Error:
               messagebox.showerror("Error" , "Value not deleted")

                #=================Refresh========================== 
        def reload():
           obj=PharmacyManagementSystem(root)

        #====================Medicine Add Department==============

        img5=Image.open("img5.jpeg")
        img5=img5.resize((200,100))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b5=Button(self.root , image=self.photoimg5,borderwidth=0)
        b5.place(x=960,y=160)

        lblrefnumber = Label(DataFrameRight,text="Ref no",font=("arial" , 12 , "bold"),padx=2,pady=6)
        lblrefnumber.place(x=0,y=100)

        lblrefnumberbox=Entry(DataFrameRight,bd=3 , width=20 ,textvariable=self.refmed_var ,relief="ridge")
        lblrefnumberbox.place(x=100,y=100)
        

        lblmedicinename = Label(DataFrameRight,text="Med name",font=("arial" , 12 , "bold"))
        lblmedicinename.place(x=0,y=130)

        lblmedicinename1=Entry(DataFrameRight,bd=3 , width=20 ,textvariable=self.addmed_var, relief="ridge")
        lblmedicinename1.place(x=100,y=130)

        sideframe=Frame(DataFrameRight ,bd=4 , relief="solid" , bg="white",)
        sideframe.place(x=0,y=170,height=140,width=200)

        sc_x=Scrollbar(sideframe,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=Scrollbar(sideframe,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(sideframe,columns=("ref" , "medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table['show']="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=70)
        self.medicine_table.column("medname",width=100)
        

        #=============Medicine Add buttons=========================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=205,y=180,width=60,height=130)


        btnAddmed=Button(down_frame,text="ADD",font=("arial" , 12 , "bold"),bg="green",fg="white",width=5,command=addMed)
        # fetch_data()
        btnAddmed.grid(row=0,column=0)

        btnupdatemed=Button(down_frame,text="UPD",font=("arial" , 12 , "bold"),bg="purple",fg="white",width=5,command=update_data)
        btnupdatemed.grid(row=1,column=0)

        btndeletemed=Button(down_frame,text="Del",font=("arial" , 12 , "bold"),bg="red",fg="white",width=5,command=deletemed)
        btndeletemed.grid(row=2,column=0)

        btnclearmed=Button(down_frame,text="Rfs",font=("arial" , 12 , "bold"),bg="orange",fg="white",width=5,command=reload)
        btnclearmed.grid(row=3,column=0)


        #============================Frame Details========================
        Framedetails=Frame(self.root ,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=570,width=1300,height=120)

        scroll_x=Scrollbar(Framedetails,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y=Scrollbar(Framedetails,orient=VERTICAL)
        scroll_y.pack(side=LEFT , fill=Y)

        self.pharmacy_table = ttk.Treeview(Framedetails , columns=("reg" , "Company Name" , "Type" , "Tablename" , "Lot No" , "Issuedate" , "Expdate" , "Uses" , "SideEffect" , "Warning" , "Dosage" , "Price" , "Productqt" ), xscrollcommand=sc_x , yscrollcommand=sc_y)
        
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=LEFT , fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
 
        self.pharmacy_table["show"]="headings"
        self.pharmacy_table.heading("reg" , text="Refernce no")
        self.pharmacy_table.heading("Company Name" , text="Company name")
        self.pharmacy_table.heading("Type" , text="Type of medicine")
        self.pharmacy_table.heading("Tablename" , text="Tablet name")
        self.pharmacy_table.heading("Lot No" , text="Lot no")
        self.pharmacy_table.heading("Issuedate" , text="Issue date")
        self.pharmacy_table.heading("Expdate" , text="Exp date")
        self.pharmacy_table.heading("Uses" , text="Uses")
        self.pharmacy_table.heading("SideEffect" , text="Side effect")
        self.pharmacy_table.heading("Warning" , text="Prec&warning")
        self.pharmacy_table.heading("Dosage" , text="Dosage")
        self.pharmacy_table.heading("Price" , text="Price")
        self.pharmacy_table.heading("Productqt" , text="Product Qts")

        self.pharmacy_table.pack(fill=BOTH,expand=1)
        self.pharmacy_table.column("reg" , width=100)
        

