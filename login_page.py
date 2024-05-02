from tkinter import ttk,filedialog
import tkinter as tk
from tkcalendar import DateEntry
import mysql.connector
import customtkinter as ctk
from tkinter import messagebox as ms
import re,uuid
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from datetime import date,datetime,timedelta
# from index import balance_sheet
# from customtkinter import CustomTkinter
from PIL import Image
# from smtplib import SMTP_SSL as smtp
import smtplib as smtp
from email.mime.text import MIMEText

access_list =["AddNew","All","dateWise","monthwise","individual","all_Emp","remove","balanceSheet","accessGiver"]




class admin_class:
    def __init__(self,fr,sign,email=None) -> None:
        self.fr = fr
        self.sign = sign
        self.email = email
    def check(self,x):
        if x==access_list[0]:
            admin_class(self.fr,self.sign,self.email).AddNew()
        
        elif x==access_list[1]:
            admin_class(self.fr,self.sign,self.email).All()
        
        elif x==access_list[2]:
            admin_class(self.fr,self.sign,self.email).dateWise()

        elif x==access_list[3]:
            admin_class(self.fr,self.sign,self.email).monthwise()

        elif x==access_list[4]:
            admin_class(self.fr,self.sign,self.email).individual()

        elif x==access_list[5]:
            admin_class(self.fr,self.sign,self.email).all_Emp()

        elif x==access_list[6]:
            admin_class(self.fr,self.sign,self.email).remove()

        elif x==access_list[7]:
            admin_class(self.fr,self.sign,self.email).balanceSheet()
        
        elif x==access_list[8]:
            admin_class(self.fr,self.sign,self.email).accessGiver()
    def AddNew(self):
        self.addNew_btn = ctk.CTkButton(self.fr,text="Add New",width=150,command=lambda:Reg_click(Tr=self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.addNew_btn.place(x=75,y=50)

    def All(self):
        self.addNew_btn = ctk.CTkButton(self.fr,text="Add New",width=150,command=lambda:Reg_click(Tr=self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.addNew_btn.place(x=75,y=50)

        self.dateWise_btn = ctk.CTkButton(self.fr,text="Date wise",width=150,command=lambda:dateWise(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.dateWise_btn.place(x=75,y=85)

        self.monthWise_btn = ctk.CTkButton(self.fr,text="Month wise",width=150,command=lambda : monthWise(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.monthWise_btn.place(x=75,y=120)

        self.Indi_btn = ctk.CTkButton(self.fr,text="Individual",width=150,command=lambda : Idiv_click(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.Indi_btn.place(x=75,y=155)

        self.all_Emp_btn = ctk.CTkButton(self.fr,text="All Emploies",width=150,command=lambda :All_Emp_click(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.all_Emp_btn.place(x=75,y=190)

        self.remove_btn = ctk.CTkButton(self.fr,text="Remove",width=150,command=lambda :Remove_click(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.remove_btn.place(x=75,y=225)
        
        self.bln_sheet_btn = ctk.CTkButton(self.fr,text="Balance Sheet",width=150,command=lambda: balance_sheet(self.fr,win,back,sign=self.sign,email=self.email),corner_radius=100)
        self.bln_sheet_btn.place(x=230,y=50)

        self.access_btn = ctk.CTkButton(self.fr,text="Access Giver",width=150,command=lambda : access_giver(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.access_btn.place(x=230,y=85)
    
    def dateWise(self):
        self.dateWise_btn = ctk.CTkButton(self.fr,text="Date wise",width=150,command=lambda:dateWise(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.dateWise_btn.place(x=75,y=85)

    def monthwise(self):
        self.monthWise_btn = ctk.CTkButton(self.fr,text="Month wise",width=150,command=lambda : monthWise(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.monthWise_btn.place(x=75,y=120)

    def individual(self):
        self.Indi_btn = ctk.CTkButton(self.fr,text="Individual",width=150,command=lambda : Idiv_click(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.Indi_btn.place(x=75,y=155)

    def all_Emp(self):
        self.all_Emp_btn = ctk.CTkButton(self.fr,text="All Emploies",width=150,command=lambda :All_Emp_click(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.all_Emp_btn.place(x=75,y=190)

    def remove(self):
        self.remove_btn = ctk.CTkButton(self.fr,text="Remove",width=150,command=lambda :Remove_click(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.remove_btn.place(x=75,y=225)

    def balanceSheet(self):
        self.bln_sheet_btn = ctk.CTkButton(self.fr,text="Balance Sheet",width=150,command=lambda: balance_sheet(self.fr,win,back,sign=self.sign,email=self.email),corner_radius=100)
        self.bln_sheet_btn.place(x=230,y=50)
    
    def accessGiver(self):
        self.access_btn = ctk.CTkButton(self.fr,text="Access Giver",width=150,command=lambda : access_giver(self.fr,sign=self.sign,email=self.email),corner_radius=100)
        self.access_btn.place(x=230,y=85)




# conn = mysql.connector.connect(host='localhost',username='root',password = "password0304@" ,database = 'new_database1')
# my_cursor = conn.cursor(buffered=True)
conn =None
my_cursor = None

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")
win = ctk.CTk()
win.geometry('500x400')
win.title('ITX Solution')
# win.iconbitmap(r"C:\Users\MINI\Downloads\logo2.ico")

p = ctk.CTkImage(dark_image=Image.open("logo.png"),size=(100,50))
# p.place(x=180,y=2)
ctk.CTkLabel(win,text="",image=p,text_color="#d9ffe3",font=("sans-serif",30)).pack()

obj_list =[]

status_list = ['Check In','Check Out']

def year_list():
    query="SELECT DISTINCT YEAR(Date) FROM data"
    my_cursor.execute(query)
    temp_list = []
    for row in my_cursor:
        for i in range(len(row)):
            temp_list.append(row[i])

    return temp_list



#########################log iN page
#########################log iN page


def check_email_pass(_email,_password):
        query = "SELECT email,password,designation FROM users"
        my_cursor.execute(query)
        for row in my_cursor:
            if _email==row[0]:
                if _password==row[1]:
                    return row[2]
        conn.commit()
        return False

def check_status(_ID,_status):
    

    query = "SELECT * FROM data"
    my_cursor.execute(query)
    
    for i in my_cursor:
        
        if str(date.today().strftime('%Y-%#m-%#d')) == i[0]:
            
            if _ID in i:
                if _status in i:
                    return [True,i[1]]
    return [False,'-']

def check_In_status(_Id):
    query = "SELECT Date,ID,Status FROM data"
    my_cursor.execute(query)
    
    for i in my_cursor:
        if str(date.today().strftime('%Y-%#m-%#d')) == i[0]:
            
            if _Id in i:
                    return i[2]
    return False


def add_status(ID_var,status_var,name):
    ID =ID_var
    status =status_var.get()
    
    if status =="":
        ms.showerror("Error","Please fill all the fields:")
    else:
        
                
        if check_status(ID,status)[0]:
            ms.showerror("Error",f"you are already {status}")
            status_var.set('')
        else:
            if status == status_list[1]:
                if check_In_status(ID) == status_list[0]:
                    Date = date.today()
                    Time =datetime.now().strftime("%H:%M:%S")
                    
                    query ='INSERT INTO data(Date,Time,ID,Name,Status) VALUES(%s,%s,%s,%s,%s)'
                    value =(Date,Time,ID,name,status)

                    my_cursor.execute(query,value)

                    conn.commit()
                    
                    ms.showinfo('Message',f"Successfully {status}")
                    status_var.set('')
                    
                                             
                else:
                    ms.showerror("Error","First you will check in than check out")
            else:
                Date = date.today()
                Time =datetime.now().strftime("%H:%M:%S")
                
                query ='INSERT INTO data(Date,Time,ID,Name,Status) VALUES(%s,%s,%s,%s,%s)'
                value =(Date,Time,ID,name,status)

                my_cursor.execute(query,value)

                conn.commit()
                
                ms.showinfo('Message',f"Successfully {status}")
                status_var.set('')



def get_data(email):

    query = f"SELECT * FROM users WHERE email='{email}'"
    my_cursor.execute(query)
    print("hassam")
    for row in my_cursor:
        print(row)
        return row





def In_out_cr(frame,email):

    frame.destroy()

    win.geometry('500x400')
    in_out_frame= ctk.CTkFrame(win)
    in_out_frame.pack(padx=30,pady=60,fill='both',expand = True)

    side_fr = ctk.CTkFrame(in_out_frame,width=115,height=278)
    side_fr.place(x=0,y=0)


    back_btn = ctk.CTkButton(side_fr,text="back",width=10,command=lambda : back(in_out_frame,sign="employ",email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    tup = get_data(email)
    print(tup)
    name_lab =ctk.CTkLabel(in_out_frame,text=f"Name: {tup[1]} {tup[2]}")
    name_lab.place(x=125,y=50)

    email_lab =ctk.CTkLabel(in_out_frame,text=f"Email: {tup[3]}")
    email_lab.place(x=125,y=75)

    num_lab =ctk.CTkLabel(in_out_frame,text=f"Number: {tup[4]}")
    num_lab.place(x=125,y=100)

    Dob_lab =ctk.CTkLabel(in_out_frame,text=f"Birth Date: {tup[6]}")
    Dob_lab.place(x=125,y=125)

    check_in_lab =ctk.CTkLabel(in_out_frame,text=f"Check In: {check_status(tup[0],status_list[0])[1]}")
    check_in_lab.place(x=125,y=150)

    check_out_lab =ctk.CTkLabel(in_out_frame,text=f"Check Out: {check_status(tup[0],status_list[1])[1]}")
    check_out_lab.place(x=125,y=175)


    st_lab = ctk.CTkLabel(side_fr,text="Status:")
    st_lab.place(x=5,y=135)

    #Combobox
    status_var = tk.StringVar()
    
    status_obj = ctk.CTkComboBox(side_fr,width=100,state='readonly',values=status_list,variable=status_var)
    status_obj.place(x=5,y=160)

    Ent_btn = ctk.CTkButton(side_fr,text="Enter",width=100,command =lambda : add_status(tup[0],status_var,tup[1]),corner_radius=50)
    Ent_btn.place(x=5,y=200)

dic_for_month ={
"Jan":1,
"Feb":2,
"March":3,
"Apr":4,
"May":5,
'Jun':6,
"Jul":7,
"Aug":8,
"Sept":9,
"Oct":10,
"Nov":11,
"Dec":12
}

def check_ID(_ID):
    


    query = "SELECT id, f_name FROM users"
    my_cursor.execute(query)
    temp_tu = my_cursor
    # print(temp_tu)
    for i in my_cursor:
        print(i)
        if _ID in i:
            
            return [True,i[1]]





def print_table(ID,MON,YEAR):
    
    
    query = f"SELECT * FROM data WHERE ID ='{ID}' AND MONTH(Date) = '{dic_for_month[MON]}' AND YEAR(Date) = '{YEAR}'"
    my_cursor.execute(query)
        
    data =[['Date','Time',"ID","Name","Status"]]
    for row in my_cursor:
        temp_list =[]
        for col in row:
            temp_list.append(col)
        data.append(temp_list)

    saveas = filedialog.asksaveasfile(mode='w',title="Save File",defaultextension="pdf")
    if not saveas:
        return
    print(saveas.name)

    pdf_canvas = canvas.Canvas(saveas.name, pagesize=letter)
    table = Table(data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch],hAlign=5,vAlign=5)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 1), (1, 1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 14),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 12),
        ("ALIGN", (0, 1), (1, 1), "CENTER"),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 8),
    ]))
    
    table_width, table_height = table.wrapOn(pdf_canvas, 0, 0)

    # Define the x and y coordinates for the table
    x = (letter[0] - table_width) / 2
    y = (letter[1] - table_height) / 2

    print(x,y)

            # Place the table at the specified coordinates
    table_pos = table.drawOn(pdf_canvas, x, y)
    print(table_pos)        
            
    pdf_canvas.save()

def Today_hrs(ID):
    search_date = date.today().strftime("%Y-%#m-%#d")
    query = f"SELECT * FROM data WHERE ID ='{ID}' AND Date ='{search_date}'"
    my_cursor.execute(query)
    print(date.today().strftime("%Y-%#m-%#d"))  ### something wrong here
    h1,m1,s1="","",""
    h2,m2,s2 = "","",""
    a,b=0,0
    for row in my_cursor:
        print(row)
        if status_list[0] in row:
            h1,m1,s1 =row[1].split(":")
            a = 1
        elif status_list[1] in row:
            h2,m2,s2 = row[1].split(":")
            b = 1

    if a ==1 and b==1:

        p = timedelta(hours=0,minutes=0,seconds=0)
        p = timedelta(hours=int(h2),minutes=int(m2),seconds=int(s2))-timedelta(hours=int(h1),minutes=int(m1),seconds=int(s1))
        return p





def mon_table(fr,_id,_mon,_year):
    ID =_id
    MON = _mon.get()
    YEAR = _year.get()

    if MON=='' or YEAR=='':
        ms.showerror('Error',"Please fill the all fields:")
    else:
       
        column =['Date','Time',"ID","Name","Status"]

        Tr_frame = ctk.CTkFrame(fr)
        Tr_frame.place(x=125,y=40)

        win.geometry('700x400')##################################### win geometry

        T_hrs_lab = ctk.CTkLabel(fr,text=f"Today's hours:{Today_hrs(ID)}")
        T_hrs_lab.place(x=350,y=5)

        prt_btn = ctk.CTkButton(fr,text="Print",width=100,command=lambda:print_table(ID,MON,YEAR),corner_radius=100)
        prt_btn.place(x=500,y=5)

        query = f"SELECT * FROM data WHERE ID ='{ID}' AND MONTH(Date) = '{dic_for_month[MON]}' AND YEAR(Date) = '{YEAR}'"
        my_cursor.execute(query)

        tree_check_hour = ttk.Treeview(Tr_frame,height=7,columns=column,show="headings")

        tree_check_hour.heading(column[0],text='Date')
        tree_check_hour.heading(column[1],text='Time')
        tree_check_hour.heading(column[2],text='ID')
        tree_check_hour.heading(column[3],text='Name')
        tree_check_hour.heading(column[4],text='Status')

        tree_check_hour.column(column[0],width=75,anchor=tk.CENTER)
        tree_check_hour.column(column[1],width=75,anchor=tk.CENTER)
        tree_check_hour.column(column[2],width=75,anchor=tk.CENTER)
        tree_check_hour.column(column[3],width=125,anchor=tk.CENTER)
        tree_check_hour.column(column[4],width=110,anchor=tk.CENTER)
        
        for _row in my_cursor:
                tree_check_hour.insert('',tk.END,values=_row)

        tree_check_hour.grid(row=0,column=0,sticky='nsew')

        scl_bar = ttk.Scrollbar(Tr_frame,orient='vertical') ### scroll bar
        scl_bar.grid(row=0,column=1,sticky='ns')

        scl_bar.configure(command=tree_check_hour.yview)
        tree_check_hour.configure(yscrollcommand=scl_bar.set)

        conn.commit()

    _mon.set("")
    _year.set("")




def Id_giver(_email):
    query = f"SELECT id FROM users WHERE email ='{_email}'"
    my_cursor.execute(query)
    
    for row in my_cursor:
        return row[0]



def Hrs_click(fr,email):
    fr.destroy()

    win.geometry('500x400')
    Id_month_frame = ctk.CTkFrame(win,height=80,width=495,border_width=2)
    # Id_month_frame.place(x=0,y=0,bordermode='outside')
    Id_month_frame.pack(padx=30,pady=60,fill='both',expand = True)

    side_fr = ctk.CTkFrame(Id_month_frame,width=115,height=278)
    side_fr.place(x=0,y=0)

    back_btn = ctk.CTkButton(side_fr,text="back",width=10,command=lambda : back(Id_month_frame,sign="employ",email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    mon_Id_mon = ctk.CTkLabel(side_fr,text="Select Month:")# Select month label in check hour
    mon_Id_mon.place(x=5,y=90)

    year_Id_mon = ctk.CTkLabel(side_fr,text="Select year:")# Select year label in check hour
    year_Id_mon.place(x=5,y=140)

    hours_Id_mon = ctk.CTkLabel(side_fr,text="Total hours:")# total hour label in check hour
    hours_Id_mon.place(x=150,y=5)
    
    mon_id_Month_var = tk.StringVar()
    com_Id_mon = ttk.Combobox(side_fr,width=15,textvariable=mon_id_Month_var,values=[a for a in dic_for_month],
        state='readonly',background="#73eb83") # for Month:
    com_Id_mon.place(x=5,y=115)

    mon_id_Year_var = tk.StringVar()
    com_y_Id_mon = ttk.Combobox(side_fr,width=15,textvariable=mon_id_Year_var,values=year_list(),
        state='readonly') # for year:
    com_y_Id_mon.place(x=5,y=165)

    btn_Id_mon = ctk.CTkButton(side_fr,width=100,text="Enter",command =lambda:mon_table(Id_month_frame,Id_giver(email),mon_id_Month_var,mon_id_Year_var))
    btn_Id_mon.place(x=5,y=205)




def check_access(id):
    query = f"SELECT * FROM access_table WHERE emp_id = '{id}'"
    my_cursor.execute(query)
    temp_list=[]
    for row in my_cursor:
        temp_list.append(row[1])
    if len(temp_list)>0:
        return temp_list
    return False






def access_click(fr,tmp_lst,sign,email):
    fr.destroy()

    access_fr = ctk.CTkFrame(win)
    access_fr.pack(padx=30,pady=60,fill='both',expand = True)
    
    back_btn = ctk.CTkButton(access_fr,text="back",width=10,command=lambda : back(access_fr,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    for a in tmp_lst:
        admin_class(access_fr,sign,email).check(a)







def after_logIn(fr,email,sign="employ"):

    fr.destroy()

    win.geometry('500x400')
    user_fr = ctk.CTkFrame(win)
    user_fr.pack(padx=30,pady=60,fill='both',expand = True)
    
    back_btn = ctk.CTkButton(user_fr,text="back",width=10,command=lambda : back(user_fr,"LogIn"),corner_radius=100)
    back_btn.place(x=5,y=5)

    user_lab = ctk.CTkLabel(user_fr,text="USER PANEL",font=("helvetica",18),text_color="#d9ffe3")
    user_lab.place(x=100,y=45)

    InOut_btn = ctk.CTkButton(user_fr,text="IN/OUT",width=200,command=lambda:In_out_cr(user_fr,email),corner_radius=100)
    InOut_btn.place(x=100,y=145)

    Hrs_btn = ctk.CTkButton(user_fr,text="Check Hrs",width=200,command=lambda:Hrs_click(user_fr,email),corner_radius=100)
    Hrs_btn.place(x=100,y=180)

    if check_access(Id_giver(email)):
        print("access button created")
        access_btn = ctk.CTkButton(user_fr,text="Access",width=200,corner_radius=100,
            command=lambda:access_click(user_fr,check_access(Id_giver(email)),sign,email))
        access_btn.place(x=100,y=215)





################################## admin function
################################## admin function






def dateWise(fr,sign,email):
    fr.destroy()

    win.geometry('500x400')
    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    side_fr = ctk.CTkFrame(frame,width=115,height=278)
    side_fr.place(x=0,y=0)

    
    back_btn = ctk.CTkButton(side_fr,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    cal1 = DateEntry(side_fr,selectmode = "day",state='readonly',width = 13,
            borderwidth = 2,
            year = 2023,
            background = 'sea green')
    cal1.place(x=5,y=100)
    
    
    def enter_click():
        sel_date = cal1.get_date()
        query = "SELECT * FROM data"
        my_cursor.execute(query)

        win.geometry('700x400')
        sub_status_frame = ctk.CTkFrame(frame)
        sub_status_frame.place(x=120,y=50)

        column =['Date','Time',"ID","Name","Status"]

        sub_sub_status_Tr = ttk.Treeview(sub_status_frame,columns=column,show="headings",)

        sub_sub_status_Tr.heading(column[0],text='Date')
        sub_sub_status_Tr.heading(column[1],text='Time')
        sub_sub_status_Tr.heading(column[2],text='ID')
        sub_sub_status_Tr.heading(column[3],text='Name')
        sub_sub_status_Tr.heading(column[4],text='Status')

        sub_sub_status_Tr.column(column[0],width=75,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[1],width=75,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[2],width=75,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[3],width=150,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[4],width=125,anchor=tk.CENTER)

        
        for _row in my_cursor:
            if _row[0]==sel_date.strftime('%Y-%#m-%#d'):
                sub_sub_status_Tr.insert('',tk.END,values=_row)

        

        sub_sub_status_Tr.grid(row=0,column=0,sticky='nsew')

        scl_bar = ttk.Scrollbar(sub_status_frame,orient='vertical') ### scroll bar
        scl_bar.grid(row=0,column=1,sticky='ns')

        scl_bar.configure(command=sub_sub_status_Tr.yview)
        sub_sub_status_Tr.configure(yscrollcommand=scl_bar.set)

    enter_btn = ctk.CTkButton(side_fr,text="Enter",width=100,command=enter_click,corner_radius=100)
    enter_btn.place(x=5,y=125)

def curr_bal():
    rec_Am=0
    exp=0
    query = f"SELECT SUM(amount) FROM coming_Am"
    my_cursor.execute(query)
    conn.commit()

    for row in my_cursor:
        rec_Am = row[0]

    query = f"SELECT SUM(amount) FROM EXPENDITURE"
    my_cursor.execute(query)
    conn.commit()

    for row in my_cursor:
        exp = row[0]
    
    return rec_Am - exp
    
def Rec_Am_table(fr):

    query = f"SELECT * FROM coming_Am"
    my_cursor.execute(query)
    conn.commit()
    ctk.CTkLabel(fr,text="Recieved Amount",text_color="#d9ffe3",font =("san-seirf",24,'underline')).place(x=75,y=5)

    sub_frame = ctk.CTkFrame(fr)
    sub_frame.place(x=0,y=65)
    Attribute = ["Date","Description","Amount"]
    tree_obj = ttk.Treeview(sub_frame,columns=Attribute,show=["headings"])
    

    tree_obj.heading(Attribute[0],text="Date")
    tree_obj.heading(Attribute[1],text="Description")
    tree_obj.heading(Attribute[2],text="Amount")


    tree_obj.column(Attribute[0],width=75,anchor=tk.CENTER)
    tree_obj.column(Attribute[1],width=220,anchor=tk.CENTER)
    tree_obj.column(Attribute[2],width=120,anchor=tk.CENTER)


    for row in my_cursor:
        tree_obj.insert('',tk.END,values=row)

    tree_obj.grid(row=0,column=0,sticky='nsew')

    scl_bar = ttk.Scrollbar(sub_frame,orient='vertical') ### scroll bar
    scl_bar.grid(row=0,column=1,sticky='ns')

    scl_bar.configure(command=tree_obj.yview)
    tree_obj.configure(yscrollcommand=scl_bar.set)


    query = f"SELECT SUM(amount) FROM coming_Am"
    my_cursor.execute(query)
    conn.commit()
    temp =0
    for row in my_cursor:
        temp = row[0]

    tree_obj.insert("",tk.END,values=["Total","",temp])

    return tree_obj

def expense_table(fr):

    query = f"SELECT * FROM EXPENDITURE"
    my_cursor.execute(query)
    conn.commit()
    ctk.CTkLabel(fr,text="Expense",text_color="#d9ffe3",font =("san-seirf",24,'underline')).place(x=450,y=5)

    sub_frame = ctk.CTkFrame(fr)
    sub_frame.place(x=450,y=65)
    Attribute = ["Date","Description","Amount"]
    tree_obj = ttk.Treeview(sub_frame,columns=Attribute,show=["headings"])
    

    tree_obj.heading(Attribute[0],text="Date")
    tree_obj.heading(Attribute[1],text="Description")
    tree_obj.heading(Attribute[2],text="Amount")


    tree_obj.column(Attribute[0],width=75,anchor=tk.CENTER)
    tree_obj.column(Attribute[1],width=220,anchor=tk.CENTER)
    tree_obj.column(Attribute[2],width=120,anchor=tk.CENTER)


    for row in my_cursor:
        tree_obj.insert('',tk.END,values=row)

    tree_obj.grid(row=0,column=0,sticky='nsew')

    scl_bar = ttk.Scrollbar(sub_frame,orient='vertical') ### scroll bar
    scl_bar.grid(row=0,column=1,sticky='ns')

    scl_bar.configure(command=tree_obj.yview)
    tree_obj.configure(yscrollcommand=scl_bar.set)

    query = f"SELECT SUM(amount) FROM EXPENDITURE"
    my_cursor.execute(query)
    conn.commit()
    temp =0
    for row in my_cursor:
        temp = row[0]

    tree_obj.insert("",tk.END,values=["Total","",temp])

    return tree_obj



def balance_sheet(fr,win,back,sign,email):
    fr.destroy()
    
    win.geometry("950x500")

    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=30,fill='both',expand = True)

    back_btn = ctk.CTkButton(frame,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    curr_obj1 =[]

    def curr_label():
        if curr_obj1:
            try:
                curr_obj1[0].destroy()
                curr_obj1.clear()
            except:
                print("error")
        curr_frame = ctk.CTkFrame(frame)
        curr_frame.place(x=620,y=300)
        ctk.CTkLabel(curr_frame,text=f"Current balance {curr_bal()}",text_color="#d9ffe3",font =("san-seirf",18)).pack(fill="both",expand=True)
        curr_obj1.append(curr_frame) 
    
    curr_label()

    ########### calling tree

    Rec_Am_table(frame)
    expense_table(frame)

    date_obj = DateEntry(frame,height=20)
    date_obj.place(x=25,y=300)
    
    combo_list = ["Expense","Income"]
    
    combo = ctk.CTkComboBox(frame,values=combo_list)
    combo.place(x=25,y=340)

    Descrip_Ent = ctk.CTkEntry(frame,placeholder_text="description")
    Descrip_Ent.place(x=130,y=300)

    Amount_Ent = ctk.CTkEntry(frame,placeholder_text="Amount")
    Amount_Ent.place(x=280,y=300)

    def Add_click():
        check =combo.get()
        date1 = date_obj.get_date()
        desc = Descrip_Ent.get()
        Am = Amount_Ent.get()

        if date1 =="" or desc =="" or Am =="" or check=="":
            ms.showerror("Error","Please Fill the Entry box:")
            return
        else:
            try:
                int(Am)
            except ValueError as er:
                ms.showerror("Error",er)
                return
        
        if check==combo_list[1]:
            query = f"INSERT INTO coming_Am(date,Description,amount) VALUE(%s,%s,%s)"
            value =(date1,desc,Am)
            my_cursor.execute(query,value)
            conn.commit()
            Rec_Am_table(frame)
            curr_label()
        elif check ==combo_list[0]:
            query = f"INSERT INTO EXPENDITURE(date,Description,amount) VALUE(%s,%s,%s)"
            value =(date1,desc,Am)
            my_cursor.execute(query,value)
            conn.commit()
            expense_table(frame)
            curr_label()

        combo.set("")
        Descrip_Ent.setvar("")
        Amount_Ent.setvar("")

    Add_btn = ctk.CTkButton(frame,text="Add",width=10,command=Add_click,corner_radius=100)
    Add_btn.place(x=170,y=340)


def monthWise(fr,sign,email):
    fr.destroy()

    win.geometry('500x400')
    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    side_fr = ctk.CTkFrame(frame,width=115,height=278)
    side_fr.place(x=0,y=0)

    back_btn = ctk.CTkButton(side_fr,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)


    mon_var =tk.StringVar()
    mon = ttk.Combobox(side_fr,width=15,textvariable=mon_var,values=[a for a in dic_for_month],
        state='readonly') # for Month:
    mon.place(x=5,y=100)

    Year_var = tk.StringVar()
    year = ttk.Combobox(side_fr,width=15,textvariable=Year_var,values=year_list(),
        state='readonly') # for year:
    year.place(x=5,y=135)

    def select_click():
        Month = mon_var.get()
        _Year = Year_var.get()

        if Month =="" or _Year =="":
            ms.showerror("Error","Please select the year and month both")
            return
        mon_var.set("")
        Year_var.set("")

        query = f"SELECT * FROM data WHERE MONTH(Date) = '{dic_for_month[Month]}' AND YEAR(Date) = '{_Year}'"
        my_cursor.execute(query)

        win.geometry('700x400')
        sub_status_frame = ctk.CTkFrame(frame)
        sub_status_frame.place(x=120,y=50)

        column =['Date','Time',"ID","Name","Status"]

        sub_sub_status_Tr = ttk.Treeview(sub_status_frame,columns=column,show="headings")

        sub_sub_status_Tr.heading(column[0],text='Date')
        sub_sub_status_Tr.heading(column[1],text='Time')
        sub_sub_status_Tr.heading(column[2],text='ID')
        sub_sub_status_Tr.heading(column[3],text='Name')
        sub_sub_status_Tr.heading(column[4],text='Status')

        sub_sub_status_Tr.column(column[0],width=75,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[1],width=75,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[2],width=75,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[3],width=150,anchor=tk.CENTER)
        sub_sub_status_Tr.column(column[4],width=125,anchor=tk.CENTER)

        
        for _row in my_cursor:
            sub_sub_status_Tr.insert('',tk.END,values=_row)

        

        sub_sub_status_Tr.grid(row=0,column=0,sticky='nsew')

        scl_bar = ttk.Scrollbar(sub_status_frame,orient='vertical') ### scroll bar
        scl_bar.grid(row=0,column=1,sticky='ns')

        scl_bar.configure(command=sub_sub_status_Tr.yview)
        sub_sub_status_Tr.configure(yscrollcommand=scl_bar.set)



    select_btn = ctk.CTkButton(side_fr,width=100,text="Select",command =lambda:select_click(),corner_radius=100)
    select_btn.place(x=5,y=170)

def create_list():
    query = "SELECT id,f_name,l_name FROM users"
    my_cursor.execute(query)

    temp_list =[]
    for row in my_cursor:
        temp_list.append(f"{row[1]} {row[2]} {row[0]}")
    conn.commit()
    return temp_list

def fetch_ID(F,L):
    query = f"SELECT id FROM users WHERE f_name ='{F}' AND l_name= '{L}'"
    my_cursor.execute(query)
    for row in my_cursor:
        return row

def Idiv_click(fr,sign,email):
    fr.destroy()

    win.geometry('500x400')
    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    side_fr = ctk.CTkFrame(frame,width=115,height=278)
    side_fr.place(x=0,y=0)

    back_btn = ctk.CTkButton(side_fr,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    st_combo = ttk.Combobox(side_fr,width=10 ,values=create_list(),state="readonly")
    st_combo.place(x=5,y=75)
        

    com_mon = ttk.Combobox(side_fr,width=10,values=[a for a in dic_for_month],
        state='readonly') # for Month:
    com_mon.place(x=5,y=110)

    com_year = ttk.Combobox(side_fr,width=10,values=year_list(),
        state='readonly') # for year:
    com_year.place(x=5,y=145)

    def select_click():
        name = st_combo.get()
        Month = com_mon.get()
        _Year = com_year.get()



        if name ==""or Month=='' or _Year=="":
                ms.showerror("Error","Please select the name of users:")
        else:
            lst1 = name.split()
            f_name= lst1[0]
            l_name = lst1[1]
            
            query = f"SELECT * FROM data WHERE ID='{fetch_ID(f_name,l_name)[0]}' AND MONTH(Date) = '{dic_for_month[Month]}' AND YEAR(Date) = '{_Year}'"
            my_cursor.execute(query)

        
            win.geometry('700x400')
            sub_status_frame = ctk.CTkFrame(frame)
            sub_status_frame.place(x=120,y=50)

            column =['Date','Time',"ID","Name","Status"]

            sub_sub_status_Tr = ttk.Treeview(sub_status_frame,columns=column,show="headings",)

            sub_sub_status_Tr.heading(column[0],text='Date')
            sub_sub_status_Tr.heading(column[1],text='Time')
            sub_sub_status_Tr.heading(column[2],text='ID')
            sub_sub_status_Tr.heading(column[3],text='Name')
            sub_sub_status_Tr.heading(column[4],text='Status')

            sub_sub_status_Tr.column(column[0],width=75,anchor=tk.CENTER)
            sub_sub_status_Tr.column(column[1],width=75,anchor=tk.CENTER)
            sub_sub_status_Tr.column(column[2],width=75,anchor=tk.CENTER)
            sub_sub_status_Tr.column(column[3],width=150,anchor=tk.CENTER)
            sub_sub_status_Tr.column(column[4],width=125,anchor=tk.CENTER)

            
            for _row in my_cursor:
                sub_sub_status_Tr.insert('',tk.END,values=_row)


            sub_sub_status_Tr.grid(row=0,column=0,sticky='nsew')

            scl_bar = ttk.Scrollbar(sub_status_frame,orient='vertical') ### scroll bar
            scl_bar.grid(row=0,column=1,sticky='ns')

            scl_bar.configure(command=sub_sub_status_Tr.yview)
            sub_sub_status_Tr.configure(yscrollcommand=scl_bar.set)

    select_btn = ctk.CTkButton(side_fr,width=50,text="Select",command =lambda:select_click(),corner_radius=100)
    select_btn.place(x=5,y=180)


def All_Emp_click(fr,sign,email):
    fr.destroy()
        
    win.geometry('800x400')
    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    back_btn = ctk.CTkButton(frame,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)
    
    big_frame = ctk.CTkFrame(frame)
    big_frame.place(x=0,y=50)
    
    columnEmp =['id', 'f_name', 'l_name', 'email', 'p_num', 'gender','birth_date']
    
    query = "SELECT * FROM users"
    my_cursor.execute(query)

    Employ_tree = ttk.Treeview(big_frame,height=7,columns=columnEmp,show="headings")
    Employ_tree.heading(columnEmp[0],text='ID')
    Employ_tree.heading(columnEmp[1],text='F_Name')
    Employ_tree.heading(columnEmp[2],text='L_name')
    Employ_tree.heading(columnEmp[3],text='Email')
    Employ_tree.heading(columnEmp[4],text='Number')
    Employ_tree.heading(columnEmp[5],text='Gender')
    Employ_tree.heading(columnEmp[6],text='Birth Date')

    Employ_tree.column(columnEmp[0],width=75,anchor=tk.CENTER)
    Employ_tree.column(columnEmp[1],width=75,anchor=tk.CENTER)
    Employ_tree.column(columnEmp[2],width=75,anchor=tk.CENTER)
    Employ_tree.column(columnEmp[3],width=150,anchor=tk.CENTER)
    Employ_tree.column(columnEmp[4],width=125,anchor=tk.CENTER)
    Employ_tree.column(columnEmp[5],width=100,anchor=tk.CENTER)
    Employ_tree.column(columnEmp[6],width=100,anchor=tk.CENTER)
    
    for _row in my_cursor:
        Employ_tree.insert('',tk.END,values=_row)

    

    Employ_tree.grid(row=0,column=0,sticky='nsew')

    scl_bar = ttk.Scrollbar(big_frame,orient='vertical') ### scroll bar
    scl_bar.grid(row=0,column=1,sticky='ns')

    scl_bar.configure(command=Employ_tree.yview)
    Employ_tree.configure(yscrollcommand=scl_bar.set)






def Remove_click(fr,sign,email):

    fr.destroy()
    win.geometry('500x400')
    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    back_btn = ctk.CTkButton(frame,text="back",width=20,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    st_combo = ttk.Combobox(frame,width=18 ,values=create_list(),state="readonly")
    st_combo.place(x=150,y=75)

    def del_btn_click(): #Delete button woring
        name = st_combo.get()

        if name=="":
            ms.showerror('Error',"please Select One:")
            return

        f_name,l_name,_id =name.split()

        query = f"DELETE FROM users WHERE id = '{_id}'"
        my_cursor.execute(query)
        ms.showinfo("inform",f"{name} Removed Successfully")
        st_combo.set("")
        conn.commit()
        
    rem_btn = ctk.CTkButton(frame,text="Remove",command=del_btn_click,corner_radius=100)
    rem_btn.place(x=150,y=110)





def show_click(fr,sign,email):
    fr.destroy()

    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=30,fill='both',expand = True)
    win.geometry('500x400')

    back_btn = ctk.CTkButton(frame,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    big_frame = ctk.CTkFrame(frame)
    big_frame.place(x=0,y=50)
    
    columnEmp =["Name","Access"]
    
    query = "SELECT DISTINCT emp_id FROM access_table"
    my_cursor.execute(query)

    id_lst = []
    for row in my_cursor:
        for i in range(len(row)):
            id_lst.append(row[i])
    access_lst = []
    for a in id_lst:
        access_lst.append(check_access(a))
    
    name_lst = []

    for i in id_lst:
        query = f"SELECT id,f_name,l_name FROM users WHERE id ='{i}'"
        my_cursor.execute(query)
        for row in my_cursor:
            name_lst.append(f"{row[1]} {row[2]} {row[0]}")
    complete_lst =[]
    for i in range(len(name_lst)):
        complete_lst.append([name_lst[i],access_lst[i]])

    Employ_tree = ttk.Treeview(big_frame,height=7,columns=columnEmp,show="headings")
    Employ_tree.heading(columnEmp[0],text='Name')
    Employ_tree.heading(columnEmp[1],text='Access')
    
    Employ_tree.column(columnEmp[0],width=150,anchor=tk.CENTER)
    Employ_tree.column(columnEmp[1],width=200,anchor=tk.CENTER)

    
    for _row in complete_lst:
        Employ_tree.insert('',tk.END,values=_row)

    

    Employ_tree.grid(row=0,column=0,sticky='nsew')

    scl_bar = ttk.Scrollbar(big_frame,orient='vertical') ### scroll bar
    scl_bar.grid(row=0,column=1,sticky='ns')

    scl_bar.configure(command=Employ_tree.yview)
    Employ_tree.configure(yscrollcommand=scl_bar.set)

    def callback(event):
        item = event.widget.focus()
        values = event.widget.item(item)["values"]
        print(values)
        if values=="":
            ms.showerror("Error","Select Correct line")
            return
        id = values[0].split()[2]
        print(id)
        query = f"DELETE FROM access_table WHERE emp_id = '{id}'"
        my_cursor.execute(query)

        ms.showinfo("Inform","Successfully deleted")
        

    Employ_tree.bind("<<TreeviewSelect>>", callback)



def access_giver(fr,sign,email):
    fr.destroy()

    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    back_btn = ctk.CTkButton(frame,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)
    
    sub_frame = ctk.CTkFrame(frame,height=300)
    sub_frame.place(x=5,y=50)

    name_lab = ctk.CTkLabel(sub_frame,text="Name:")
    name_lab.grid(row=0,column=0)

    access_lab = ctk.CTkLabel(sub_frame,text="Access:")
    access_lab.grid(row=1,column=0)

    employee_names = ttk.Combobox(sub_frame,values=create_list(),width=15,state="readonly")
    employee_names.grid(row=0,column=1,padx=5)

    accessess = ttk.Combobox(sub_frame,width=15,state="readonly",values=access_list)
    accessess.grid(row=1,column=1,padx=5)
 
    name_var = tk.StringVar()
    name_ent = ctk.CTkEntry(sub_frame,textvariable=name_var,state="readonly",width=116)
    name_ent.grid(row=0,column=2)

    access_var = tk.StringVar()
    access_ent = ctk.CTkEntry(sub_frame,textvariable=access_var,state="readonly",width=116)
    access_ent.grid(row=1,column=2)

    def emp_select(event):
        name_var.set(employee_names.get())

    employee_names.bind("<<ComboboxSelected>>",emp_select)

    def access_select(event):
        access_var.set(accessess.get())

    accessess.bind("<<ComboboxSelected>>",access_select)

    def Okay_click():
        name = name_var.get()
        access = access_var.get()
        if name=="" or access=="":
            ms.showerror("Error","select both name and access:")
            return
        _list = name.split()
        id = _list[2]
        query = "INSERT INTO access_table(emp_id,access) VALUE(%s,%s)"
        value = (id,access)
        my_cursor.execute(query,value)
        conn.commit()

        name_var.set("")
        access_var.set("")
        employee_names.set('')
        accessess.set('')



        ms.showinfo('inform','Successfully Done')
        
    okay_btn = ctk.CTkButton(sub_frame,text="Okay",width=100,command=lambda : Okay_click(),corner_radius=100)
    okay_btn.grid(row = 2)
    Show_btn = ctk.CTkButton(sub_frame,text="SHOW",width=100,command=lambda : show_click(frame,sign,email),corner_radius=100)
    Show_btn.grid(row = 3,pady=5)



def admin_logIn(fr,sign="admin"):

    fr.destroy()
    win.geometry('500x400')
    admin_fr = ctk.CTkFrame(win)
    admin_fr.pack(padx=30,pady=30,fill='both',expand = True)
    
    back_btn = ctk.CTkButton(admin_fr,text="back",width=10,command=lambda : back(admin_fr,"LogIn"),corner_radius=100)
    back_btn.place(x=5,y=5)

    admin_lab = ctk.CTkLabel(admin_fr,text="ADMIN PANEL",font=("helvetica",18),text_color="#d9ffe3")
    admin_lab.place(x=100,y=25)

    p = admin_class(admin_fr,sign).All()
    





def logIn_click(fr,logIn_email_Ent,logIn_pass_Ent):
    email= logIn_email_Ent.get()
    pass_var =logIn_pass_Ent.get()
    logIn_email_Ent.delete(0,tk.END)
    logIn_pass_Ent.delete(0,tk.END)

    if email==""or pass_var=="":
        ms.showerror("Error","email or password is empty")
        return
    
    check =check_email_pass(email,pass_var)
    if check=="employ":
        after_logIn(fr,email)

    elif check=="admin":
        admin_logIn(fr)

    else:
        ms.showerror('Error',"you entered wrong email or password")








def password_create(fr,sys_code,user_Entry,email):
    if user_Entry=="":
        ms.showerror("Error","Please Enter the code :")
        return
    elif sys_code!=user_Entry:
        ms.showerror("Error","You Entered wrong code:")
        return
    fr.destroy()
    win.geometry('500x400')
    frame = ctk.CTkFrame(win,height=300,width=300,border_width=1,bg_color="#8cbdab")
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    pass_label = ctk.CTkLabel(frame,text="Enter password:",font=("sans-serif",18))
    pass_label.pack(pady=10)
            
    pass_Ent = ctk.CTkEntry(frame,width=200,placeholder_text='password',font=("helvetica",16,"italic"),show="*")
    pass_Ent.pack(pady=10)
    re_pass_Ent = ctk.CTkEntry(frame,width=200,placeholder_text='re-enter password',font=("helvetica",16,"italic"),show="*")
    re_pass_Ent.pack(pady=10)

    def set_pass():
        if pass_Ent.get()=="" or re_pass_Ent.get()=="":
            ms.showerror("Error","please enter password:")
            return
        elif pass_Ent.get()!= re_pass_Ent.get():
            ms.showerror("Error","Please Enter Same password in Re-enter password:")
            return
        query=f"UPDATE users SET password='{pass_Ent.get()}' WHERE email='{email}'"
        my_cursor.execute(query)
        conn.commit()
        ms.showinfo("password changed","Successfully Done")
        logIn(frame)
    
    okay_btn = ctk.CTkButton(frame,text="Okay",command =lambda : set_pass(),corner_radius=50)
    okay_btn.pack(pady=10)









def sent_mail(fr,email):
    if email=="":
            ms.showerror("Error","Please enter email:")
            return
    query = f"SELECT email FROM users WHERE email = '{email}'"
    my_cursor.execute(query)
    mail =""
    for row in my_cursor:
        mail=row[0]
    if mail=="":
        ms.showerror("Error","Your email is not exists in data:")
        return
    
    SMTPserver = 'smtp.world4you.com'
    sender =     'office@itx-solution.com'

    # USERNAME = "hassamghori722@gmail.com"
    PASSWORD = "Cph181ko!!"

    code = uuid.uuid4().hex[:4]
    message = MIMEText(f"your four alpha numeric code is:{code}")
    message["subject"] = "ITX Solutions"
    message["from"] = sender
    
    conn = smtp.SMTP(SMTPserver,587,timeout=60)
    conn.starttls()
    conn.set_debuglevel(1)
    conn.login(sender, PASSWORD)
    try:
    
        conn.sendmail(sender,email,message.as_string())
    except:
        ms.showerror("Error","Error")
    finally:
        conn.quit()

    fr.destroy()
    win.geometry('500x400')
    frame = ctk.CTkFrame(win,height=300,width=300,border_width=1,bg_color="#8cbdab")
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    # back_btn = ctk.CTkButton(frame,text="back",width=10,command=lambda : back(frame,"LogIn"),corner_radius=100)
    # back_btn.place(x=5,y=5)

    code_label = ctk.CTkLabel(frame,text="Enter Confirmation Code Here:",font=("sans-serif",18))
    code_label.pack(pady=10)
            
    code_Ent = ctk.CTkEntry(frame,width=200,placeholder_text='code',font=("helvetica",16,"italic"))
    code_Ent.pack(pady=10)
    # email_Ent.bind("<Return>",command=lambda event : check_email(email_Ent.get()))

    
    okay_btn = ctk.CTkButton(frame,text="Okay",command =lambda : password_create(frame,code,code_Ent.get(),email),corner_radius=50)
    okay_btn.pack(pady=10)
    Resend_btn = ctk.CTkButton(frame,text="Resend",command =lambda : sent_mail(frame,email),corner_radius=50)
    Resend_btn.pack(pady=10)
    




        

def forgot_pass(fr):

    fr.destroy()
    win.geometry('500x400')
    frame = ctk.CTkFrame(win,height=300,width=300,border_width=1,bg_color="#8cbdab")
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    back_btn = ctk.CTkButton(frame,text="back",width=10,command=lambda : back(frame,"LogIn"),corner_radius=100)
    back_btn.place(x=5,y=5)

    forgot_pass_label = ctk.CTkLabel(frame,text="Forgot Password",font=("sans-serif",24))
    forgot_pass_label.pack(pady=10)
            
    email_Ent = ctk.CTkEntry(frame,width=200,placeholder_text='email',font=("helvetica",16,"italic"))
    email_Ent.pack(pady=10)
    # email_Ent.bind("<Return>",command=lambda event : check_email(email_Ent.get()))

    okay_btn = ctk.CTkButton(frame,text="Okay",command =lambda : sent_mail(frame,email_Ent.get()),corner_radius=50)
    okay_btn.pack(pady=10)
    # okay_btn.bind()












def logIn(fr=None):
    if fr!=None:
        fr.destroy()

    win.geometry('500x400')
    logIn = ctk.CTkFrame(win,height=300,width=300,border_width=1,bg_color="#8cbdab")
    logIn.pack(padx=30,pady=30,fill='both',expand = True)

    logIn_email_label = ctk.CTkLabel(logIn,text="Log In",font=("sans-serif",24))
    logIn_email_label.pack(pady=10)

    logIn_email_Ent = ctk.CTkEntry(logIn,width=200,placeholder_text='email',font=("helvetica",16,"italic"))
    logIn_email_Ent.pack(pady=10)
    logIn_email_Ent.focus_force()

    logIn_pass_Ent = ctk.CTkEntry(logIn,width=200,placeholder_text='password',font=("helvetica",16,"italic"),show="*")
    logIn_pass_Ent.pack()
    

    logIn_btn = ctk.CTkButton(logIn,text="Log In",command =lambda:logIn_click(logIn,logIn_email_Ent,logIn_pass_Ent),corner_radius=50)
    logIn_btn.pack(pady=10)

    def on_enter_press(event):
        logIn_btn.invoke()
    logIn_btn.bind("<Return>",on_enter_press)

    Reg_btn = ctk.CTkButton(logIn,text="Sign Up",command= lambda:Reg_click(logIn,sign="LogIn"),corner_radius=50)
    Reg_btn.pack()

    forgot_pass_label = ctk.CTkLabel(logIn,text="forgot password",font=("sans-serif",12,'underline'),cursor ="hand2")
    forgot_pass_label.place(x=195,y=205)

    forgot_pass_label.bind("<Button-1>",command=lambda event :forgot_pass(logIn))

    obj_list.append(logIn)




######################################### Sign UP working
######################################### Sign UP working

def back(frame,sign,email=None):

    if sign=="employ":
        after_logIn(frame,email)
    elif sign=="LogIn":
        logIn(frame)
    elif sign=="admin":
        admin_logIn(frame)






def Reg_click(Tr,sign,email=None):

    Tr.destroy()

    win.geometry('500x540')
    user_frame = ctk.CTkFrame(win,border_width=1,width=500,height=800)
    user_frame.pack(padx=30,pady=60,fill='both',expand = True)
    # user_frame.place(x=30,y=30)
    #
    back_btn = ctk.CTkButton(user_frame,text="back",width=10,command=lambda : back(user_frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)
    
    #  labels
    

    sign_up_label=ctk.CTkLabel(user_frame,text="Sign_Up",font=("helvetica",24))
    sign_up_label.grid(row=0,column=0,columnspan=2,pady=10,padx=10,sticky='e')

    label_obj_list = []
    labels_list= ["First Name:","Last Name:","Email:","Phone Number:","Gender:","Birth Date:"]
    label_row=1
    for i in labels_list:
        a=ctk.CTkLabel(user_frame,text=i,font=("helvetica",16))
        a.grid(row=label_row,column=0,sticky=tk.W,pady=5,padx=5)
        label_row+=1
        label_obj_list.append(a)


    pass_label=ctk.CTkLabel(user_frame,text="Password:",font=("helvetica",16))
    pass_label.grid(row=7,column=0,sticky=tk.W,pady=5,padx=5)

    cnf_pass_label=ctk.CTkLabel(user_frame,text="confirm Password:",font=("helvetica",16))
    cnf_pass_label.grid(row=8,column=0,sticky=tk.W,pady=5,padx=5)


    # Entries
    entry_obj_var_list =[]
    entry_obj_list= []
    for i in range(4):
        b=tk.StringVar()
        a=ctk.CTkEntry(user_frame,textvariable=b)
        a.grid(row=i+1,column=1,columnspan=2)
        entry_obj_list.append(a)
        entry_obj_var_list.append(b)

    pass_Ent=ctk.CTkEntry(user_frame,placeholder_text="password",show="*",font=("helvetica",16,"italic"))
    pass_Ent.grid(row=7,column=1,columnspan=2)

    cnf_pass_ENT=ctk.CTkEntry(user_frame,placeholder_text="password",show="*",font=("helvetica",16,"italic"))
    cnf_pass_ENT.grid(row=8,column=1,columnspan=2)

    #Radio Buttons
    gen_var = tk.StringVar()
    male = ctk.CTkRadioButton(user_frame,text="Male",value="Male",variable=gen_var)
    male.grid(row=5,column=1,sticky=tk.W)

    Female = ctk.CTkRadioButton(user_frame,text="Female",value="Female",variable=gen_var)
    Female.grid(row=5,column=2,sticky=tk.W)

    # birth date

    birth_date_obj = DateEntry(user_frame,width= 17,year=2000,state='readonly',background="sea green")
    birth_date_obj.grid(row=6,column=1,columnspan=2)

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def check(email):
 
        # pass the regular expression
        # and the string into the fullmatch() method
        if(re.fullmatch(regex, email)):
            print("Valid Email")
            return True
    
        else:
            print("Invalid Email")
            return False
        
    def user_check(_email,_num):
        query = "SELECT email, p_num FROM users"
        my_cursor.execute(query)
        for row in my_cursor:
            if _email==row[0] or _num ==row[1]:
                return True
        return False

   


    def Add_Btn_click():
        f_name = entry_obj_var_list[0].get()
        l_name = entry_obj_var_list[1].get()
        email = entry_obj_var_list[2].get()
        p_num= entry_obj_var_list[3].get()
        gender= gen_var.get()
        B_Date = birth_date_obj.get_date()
        password=pass_Ent.get()
        cnf_password =cnf_pass_ENT.get()

        if f_name==''or l_name==""or B_Date=="" or email=='' or p_num ==''or gender=="" or password=='' or cnf_password=="":
            ms.showerror("Error","Please! fill the All fields")
        else:
            try:
                int(p_num)
                if len(p_num)!=11:
                    raise ValueError
                elif check(email):
                    try:
                        password == cnf_password
                    except:
                        ms.showerror('Error',"password is not same:")
                        return
                    try:
                        if user_check(email,p_num):
                            ms.showerror("Message","You are already added")
                        else:
                            
                                ID = uuid.uuid4().hex[:4]
                                query ='INSERT INTO users(id, f_name, l_name, email, p_num, gender,birth_date,password,designation) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                value =(str(ID),f_name.upper(),l_name.upper(),email,p_num,gender,B_Date,password,"employ")

                                my_cursor.execute(query,value)

                                conn.commit()
                                # conn.close()

                                ms.showinfo("Message",f"you are Successfully added\nYour ID is {ID}")
                                entry_obj_list[0].delete(0,tk.END)
                                entry_obj_list[1].delete(0,tk.END)
                                entry_obj_list[2].delete(0,tk.END)
                                entry_obj_list[3].delete(0,tk.END)
                                birth_date_obj.delete(0,tk.END)
                                pass_Ent.delete(0,tk.END)
                                cnf_pass_ENT.delete(0,tk.END)
                                gen_var.set("")
                                
                                

                    except ValueError as err:
                        ms.showerror("Error",f"your error is {err}")

                    
                else:
                    ms.showerror("Error","please enter Correct Email")


            except ValueError:
                ms.showerror("Error","you enter wrong phone number")

    Add_Btn = ctk.CTkButton(user_frame,text="Add",command =Add_Btn_click,corner_radius=100)
    Add_Btn.place(x=60,y=380)


    
logIn()

win.mainloop()