

import tkinter as tk
from tkinter import ttk,filedialog
from tkinter import messagebox as ms
from csv import DictWriter as Dw
from csv import DictReader as Dr
from csv import reader
import os,re,uuid
from datetime import date,datetime,timedelta
from tkcalendar import DateEntry
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle


# conn = mysql.connector.connect(host='localhost',username='root',password = "password0304@" ,database = 'new_database1')
# my_cursor = conn.cursor(buffered=True)
my_cursor = None

# cursor = cnx.cursor(buffered=True)

# my_cursor.execute("SELECT id FROM users")

# if '8e9c' in my_cursor:
#     print(True)


# conn.commit()
# conn.close()



win = tk.Tk()
win.title("Time Management System:")
win.geometry("500x300")
# win.resizable(0,0)

#creating Note book and adding Pages:
nb = ttk.Notebook(win)
nb.pack(expand=True,fill='both')

new_user = ttk.Frame(nb)
In_out = ttk.Frame(nb)
Admin = ttk.Frame(nb)
check_hours = ttk.Frame(nb)

nb.add(new_user,text="New_User")
nb.add(In_out,text="IN/OUT")
nb.add(Admin,text="Admin")
nb.add(check_hours,text="Check Hours")

def handle_tab_click(event):
    # Get the index of the selected tab
    tab_index = event.widget.index('current')
    print(f'Tab {tab_index+1} was clicked!')

# Bind the event handler function to the Notebook widget
nb.bind('<<NotebookTabChanged>>', handle_tab_click)


###############################################for New_User
###############################################for New_User




user_frame = ttk.Frame(new_user)
user_frame.pack()

# labels 
label_obj_list = []
labels_list= ["First Name:","Last Name:","Email:","Phone Number:","Gender:","Birth Date:"]
label_row=0
for i in labels_list:
    a=ttk.Label(user_frame,text=i)
    a.grid(row=label_row,column=0,sticky=tk.W,pady=5)
    label_row+=1
    label_obj_list.append(a)

# Entries
entry_obj_var_list =[]
entry_obj_list= []
for i in range(4):
    b=tk.StringVar()
    a=ttk.Entry(user_frame,textvariable=b)
    a.grid(row=i,column=1,columnspan=2)
    entry_obj_list.append(a)
    entry_obj_var_list.append(b)

#Radio Buttons
gen_var = tk.StringVar()
male = ttk.Radiobutton(user_frame,text="Male",value="Male",variable=gen_var)
male.grid(row=4,column=1,sticky=tk.W)

Female = ttk.Radiobutton(user_frame,text="Female",value="Female",variable=gen_var)
Female.grid(row=4,column=2,sticky=tk.W)

# birth date

birth_date_obj = DateEntry(user_frame,width= 17,year=2000,state='readonly',background="blue")
birth_date_obj.grid(row=5,column=1,columnspan=2)


# Add Button


 
# for validating an Email
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


#for user_checking already enrolled or not
def user_check(_email,_num):
    query = "SELECT email, p_num FROM users"
    my_cursor.execute(query)
    for row in my_cursor:
        if _email==row[0] or _num ==row[1]:
            return True
    return False
    
["First Name:","Last Name:","Birth Date:","Email:","Phone Number:","Gender:"]
    
def Add():
    f_name = entry_obj_var_list[0].get()
    l_name = entry_obj_var_list[1].get()
    email = entry_obj_var_list[2].get()
    p_num= entry_obj_var_list[3].get()
    gender= gen_var.get()
    B_Date = birth_date_obj.get_date()

    print(f_name,email,p_num,gender)
    if f_name==''or l_name==""or B_Date=="" or email=='' or p_num ==''or gender=="":
        ms.showerror("Error","Please! fill the All fields")
    else:
        try:
            int(p_num)
            # print(p_num)
            if len(p_num)!=11:
                print("length of Phone number:",len(p_num))
                raise ValueError

            elif check(email):
                try:
                    if user_check(email,p_num):
                        ms.showerror("Message","You are already added")
                    else:
                        # with open("user.csv",'a',newline='') as f:
                        #     obj = Dw(f,fieldnames=["ID","First Name","Last Name","Email","Phone Number","Gender","Birth Date"])
                        #     if os.stat("user.csv").st_size ==0:
                        #         obj.writeheader()
                        #     ID = uuid.uuid4().hex[:4]
                        #     obj.writerow({
                        #         "ID":str(ID),
                        #         "First Name":f_name,
                        #         "Last Name":l_name,
                        #         "Email":email,
                        #         "Phone Number":p_num,
                        #         "Gender":gender,
                        #         "Birth Date":B_Date
                        #     })


                        ################### using data base to store the data:

                            ID = uuid.uuid4().hex[:4]
                            query ='INSERT INTO users(id, f_name, l_name, email, p_num, gender,birth_date) VALUES(%s,%s,%s,%s,%s,%s,%s)'
                            value =(str(ID),f_name,l_name,email,p_num,gender,B_Date)

                            my_cursor.execute(query,value)

                            conn.commit()
                            # conn.close()

                            ms.showinfo("Message",f"you are Successfully added\nYour ID is {ID}")
                            entry_obj_list[0].delete(0,tk.END)
                            entry_obj_list[1].delete(0,tk.END)
                            entry_obj_list[2].delete(0,tk.END)
                            entry_obj_list[3].delete(0,tk.END)
                            birth_date_obj.delete(0,tk.END)
                            gen_var.set("")
                            
                            

                except ValueError as err:
                    ms.showerror("Error",f"your error is {err}")

                
            else:
                ms.showerror("Error","please enter Correct Email")


        except ValueError:
            ms.showerror("Error","you enter wrong phone number")
        print("after try block")

    



Add_Btn = ttk.Button(user_frame,text="Add",command =Add)
Add_Btn.grid(row=6,column = 2)





#############################################################IN_out Page
#############################################################IN_out Page





in_out_frame = ttk.Frame(In_out)
in_out_frame.pack()

#labels
InOut_labels_obj_list = []
InOut_labels_list= ["Name:","ID:","Status:"]
InOut_label_row=0
for i in InOut_labels_list:
    a=ttk.Label(in_out_frame,text=i)
    a.grid(row=InOut_label_row,column=0,sticky=tk.W,pady=5)
    InOut_label_row+=1
    InOut_labels_obj_list.append(a)

# Entry
ID_var = tk.StringVar()
Id_obj = ttk.Entry(in_out_frame,textvariable=ID_var)
Id_obj.grid(row=1,column=1)

#Combobox
status_var = tk.StringVar()
status_list = ['Check In','Check Out']
status_obj = ttk.Combobox(in_out_frame,width=15,state='readonly',value=status_list,textvariable=status_var)
status_obj.grid(row=2,column =1)

# in_out command

def check_ID(_ID):
    # with open('user.csv','r') as f:
    #     R_obj = Dr(f)
    #     for row in R_obj:
    #         if _ID==row["ID"]:
    #             return [True,row["First Name"]]
    #     return [False]

    ######## reading data from database :
    query = "SELECT id, f_name FROM users"
    my_cursor.execute(query)
    temp_tu = my_cursor
    # print(temp_tu)
    for i in my_cursor:
        print(i)
        if _ID in i:
            
            return [True,i[1]]

# def for_name(_ID):

#     ######## reading data from database :
#     query = "SELECT id, f_name FROM users"
#     my_cursor.execute(query)
#     for i in my_cursor:
#         print(i)
#         if _ID in i:
#             return i[1]


def check_status(_ID,_status):
    # with open("Data1.csv",'r') as f:
    #     obj_r = Dr(f)
    #     for row in obj_r:
    #         if str(date.today())==row["Date"]:
    #             if row["ID"]==_ID:
    #                 if row["Status"]==_status:
    #                     return True
    #     return False

    #################### reading data from database

    query = "SELECT Date,ID,Status FROM data"
    my_cursor.execute(query)
    # print(temp_tu)
    for i in my_cursor:
        # print(i[0],str(date.today().strftime('%Y-%#m-%#d')))
        if str(date.today().strftime('%Y-%#m-%#d')) == i[0]:
            # print("date is matched")
            if _ID in i:
                if _status in i:

                    return True
    return False


    
def check_In_status(_Id):
    # with open("Data1.csv",'r') as f:
    #     obj_r = Dr(f)
    #     for row in obj_r:
    #         if str(date.today())==row["Date"]:
    #             if row["ID"]==_Id:
    #                 return row["Status"]
    #     return False

    ############   reading data from database
    query = "SELECT Date,ID,Status FROM data"
    my_cursor.execute(query)
    
    for i in my_cursor:
        if str(date.today().strftime('%Y-%#m-%#d')) == i[0]:
            
            if _Id in i:
                    return i[2]
    return False



                     
# print(check_In_status('834b'))

def add_status():
    ID =ID_var.get()
    status =status_var.get()
    # print(ID,status)
    if ID=="" or status =="":
        ms.showerror("Error","Please fill all the fields:")
    else:
        if len(ID) !=4:
            ms.showerror('Error',"ID consists on 4 AlphaNumeric value:")
        else:
            if check_ID(ID):
                name=check_ID(ID)[1]
                name_label = ttk.Label(in_out_frame,text=name.upper(),font=('helvetica',14))
                name_label.grid(row=0,column=1)
                
                if check_status(ID,status):
                    ms.showinfo("Message",f"you are already {status}")
                    status_obj.set('')
                    Id_obj.delete(0,tk.END)
                    name_label.destroy()
                else:
                    if status == status_list[1]:
                        if check_In_status(ID) == status_list[0]:
                            Date = date.today()
                            Time =datetime.now().strftime("%H:%M:%S")
                            # with open('Data1.csv','a',newline='') as f:
                            #     obj_w = Dw(f,fieldnames=["Date","Time","ID","Name","Status"])
                            #     if os.stat("Data1.csv").st_size ==0:
                            #         obj_w.writeheader()
                            #     obj_w.writerow({
                            #         "Date":Date,
                            #         "Time":Time,
                            #         "ID":ID,
                            #         "Name":name,
                            #         "Status":status
                            #     })

                            ################## ADDING STATUS INTO DATA BASE

                            query ='INSERT INTO data(Date,Time,ID,Name,Status) VALUES(%s,%s,%s,%s,%s)'
                            value =(Date,Time,ID,name,status)

                            my_cursor.execute(query,value)

                            conn.commit()
                            
                            ms.showinfo('Message',f"Successfully {status}")
                            status_obj.set('')
                            Id_obj.delete(0,tk.END)
                            name_label.destroy()                            
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
                        status_obj.set('')
                        Id_obj.delete(0,tk.END)
                        name_label.destroy()
            else:
                ms.showinfo("Message","This ID is not Exists")





#Enter Button 

Ent_btn = ttk.Button(in_out_frame,text="Enter",command =add_status)
Ent_btn.grid(row=3,column=1)


#for Admin page

Admin_frame = ttk.Frame(Admin)
Admin_frame.pack()

#label
Admin_label = ttk.Label(Admin_frame,text="Enter Admin Password")
Admin_label.grid(row=0,column=0,pady=5)

#entry
pass_var= tk.StringVar()
Admin_Entry = ttk.Entry(Admin_frame,textvariable=pass_var,show ="$")
Admin_Entry.grid(row=1,column =0,pady=5)

# Entry Button

cal1_var = tk.StringVar()
cal2_var =tk.StringVar()

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





############################################################ Admin start
############################################################ Admin start






def Admin_Btn():
    _pass = pass_var.get()

    if _pass=='password':
        admin_win = tk.Tk()
        admin_win.title("Admin Block:")
        admin_win.geometry("800x400")
        admin_win.resizable(False,False)



        sub_nb = ttk.Notebook(admin_win)
        sub_nb.pack(expand='True',fill = 'both')
        employ_frame = ttk.Frame(sub_nb)
        status_frame = ttk.Frame(sub_nb)
        sub_nb.add(employ_frame,text="Emploies")
        sub_nb.add(status_frame,text="Status")

        
        


        ################################################333# for employ_frame
        ################################################333# for employ_frame






        big_frame = ttk.Frame(employ_frame,height=200,width=700,borderwidth=5,relief="solid")
        big_frame.place(x=0,y=50)
           
        print_data_obj =[]
        
        def print_data():
            
            if len(print_data_obj)>0:
                print_data_obj[0].destroy()
                print_data_obj.pop()
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

            
            
           
        # ID_Entry
        delete_box = ttk.Frame(employ_frame,borderwidth=5,relief="solid")
        delete_box.place(x=300,y=0)

        _id = ttk.Label(delete_box,text="ID:")
        _id.grid(row=0,column=0)

        Id_ent1= ttk.Entry(delete_box,width=15)
        Id_ent1.grid(row=0,column=1)


        def del_btn_click(): #Delete button woring
            
            del_id =Id_ent1.get()
            query = f"DELETE FROM users WHERE id = '{del_id}'"
            my_cursor.execute(query)

            conn.commit()
            print_data()
            Id_ent1.delete(0,tk.END)

        show_data_btn = ttk.Button(employ_frame,text="Show Data",command=print_data)
        show_data_btn.place(x=0,y=0)                                           
                                    
        del_btn = ttk.Button(delete_box,text="Delete",command=del_btn_click)
        del_btn.grid(row=0,column=2)







        ###################################################### for status_frame
        ###################################################### for status_frame





        sub_status_frame = ttk.Frame(status_frame,height=275,width=525,borderwidth=5,relief="solid")
        sub_status_frame.place(x=0,y=50)
        
        # creating buttons

        btn_frame = ttk.Frame(status_frame,width=100,height=100,borderwidth=5,relief="solid")
        btn_frame.place(x=550,y=50)

        from_label = ttk.Label(btn_frame,text="Select Date:")
        from_label.grid(row=0 ,column=0,sticky=tk.W,pady=1)

        

        cal1 = DateEntry(btn_frame,selectmode = "day",state='readonly',width = 8,
            borderwidth = 2,
            year = 2023,
            background = 'blue')
        # cal1.state("readonly")
        cal1.grid(row=1 ,column=0,sticky=tk.W,pady=1)

        
        
        
        def st_btn_click():
            f_date = cal1.get_date()
            
            query = "SELECT * FROM data"
            my_cursor.execute(query)

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
                if _row[0]==f_date.strftime('%Y-%#m-%#d'):
                    sub_sub_status_Tr.insert('',tk.END,values=_row)

            

            sub_sub_status_Tr.grid(row=0,column=0,sticky='nsew')

            scl_bar = ttk.Scrollbar(sub_status_frame,orient='vertical') ### scroll bar
            scl_bar.grid(row=0,column=1,sticky='ns')
    
            scl_bar.configure(command=sub_sub_status_Tr.yview)
            sub_sub_status_Tr.configure(yscrollcommand=scl_bar.set)


        st_btn = ttk.Button(btn_frame,width=10,text="Enter",command=st_btn_click)
        st_btn.grid(row=2 ,column=0,sticky=tk.W,pady=1)

        combo_frame = ttk.Frame(status_frame,width=100,height=500,borderwidth=5,relief="solid")
        combo_frame.place(x=550,y=150)

        


        def create_list():
            query = "SELECT f_name,l_name FROM users"
            my_cursor.execute(query)

            temp_list =[]
            for row in my_cursor:
                temp_list.append(f"{row[0]} {row[1]}")
            conn.commit()
            return temp_list
        



        
        st_combo_lab = ttk.Label(combo_frame,text="Name:")
        st_combo_lab.grid(row=0 ,column=0,sticky=tk.W,pady=1)
        
        st_combo = ttk.Combobox(combo_frame,width=8 ,values=create_list(),state="readonly")
        st_combo.grid(row=1 ,column=0,sticky=tk.W,pady=1)
        
        mon_combo_lab = ttk.Label(combo_frame,text='Month:')
        mon_combo_lab.grid(row=2 ,column=0,sticky=tk.W,pady=1)

        com_mon = ttk.Combobox(combo_frame,width=8,values=[a for a in dic_for_month],
        state='readonly') # for Month:
        com_mon.grid(row=3 ,column=0,sticky=tk.W,pady=1)
        
        com_year_lab = ttk.Label(combo_frame,text='Year:')
        com_year_lab.grid(row=4 ,column=0,sticky=tk.W,pady=1)


        com_year = ttk.Combobox(combo_frame,width=8,values=[a for a in range(2023,2050)],
        state='readonly') # for year:
        com_year.grid(row=5 ,column=0,sticky=tk.W,pady=1)



        def fetch_ID(F,L):
            query = f"SELECT id FROM users WHERE f_name ='{F}' AND l_name= '{L}'"
            my_cursor.execute(query)
            for row in my_cursor:
                return row


        tr_obj =[]
        
        def print_table():

            if len(tr_obj)==0:
                ms.showerror("Error","Please, first create the table:")
                return
            rows = tr_obj[0].get_children()
            data = [['Date','Time',"ID","Name","Status"]]
            for row in rows:
                values = []
                for col in range(len(tr_obj[0]["columns"])):
                    value = tr_obj[0].item(row, "values")[col]
                    values.append(value)
                data.append(values)



            saveas = filedialog.asksaveasfile(mode='w',title="Save File",defaultextension="pdf")
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

            
            



        def combo_add_click():
            name=st_combo.get()
            month = com_mon.get()
            year =com_year.get()

            if len(tr_obj)>0:
                tr_obj[0].destroy()
                tr_obj.pop()

            if name ==""or month=='' or year=="":
                ms.showerror("Error","Please select the name of users:")
            else:
                lst1 = name.split()
                f_name= lst1[0]
                l_name = lst1[1]
                # print(len(f_name))
                # print(len(l_name))
                # print(month,year)
                
                query = f"SELECT * FROM data WHERE ID='{fetch_ID(f_name,l_name)[0]}' AND MONTH(Date) = '{dic_for_month[month]}' AND YEAR(Date) = '{year}'"
                my_cursor.execute(query)

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

                tr_obj.append(sub_sub_status_Tr)


        combo_Add_btn = ttk.Button(combo_frame,width=10,text="Add",command=combo_add_click)
        combo_Add_btn.grid(row=6 ,column=0,sticky=tk.W,pady=1)

        combo_print_btn = ttk.Button(combo_frame,width=10,text="Print",command=print_table)
        combo_print_btn.grid(row=7 ,column=0,sticky=tk.W,pady=1)



        admin_win.mainloop()

Entry_button = ttk.Button(Admin_frame,text="Enter",command =Admin_Btn)
Entry_button.grid(row=2,column=0,pady=5)





############################################ check hours working 
############################################ check hours working 






Id_month_frame = ttk.Frame(check_hours,height=80,width=495,borderwidth=5,relief='solid')
Id_month_frame.place(x=0,y=0,bordermode='outside')

below_id_mon_frame = ttk.Frame(check_hours,height=190,width=495,borderwidth=5,relief='solid')
below_id_mon_frame.place(x=0,y=80,bordermode='outside')

ID_Id_mon = ttk.Label(Id_month_frame,text="ID:") # Id label in check hour
ID_Id_mon.place(x=0,y=0)

mon_Id_mon = ttk.Label(Id_month_frame,text="Select Month:")# Select month label in check hour
mon_Id_mon.place(x=80,y=0)

year_Id_mon = ttk.Label(Id_month_frame,text="Select year:")# Select year label in check hour
year_Id_mon.place(x=175,y=0)

hours_Id_mon = ttk.Label(Id_month_frame,text="Total hours:")# total hour label in check hour
hours_Id_mon.place(x=325,y=0)

mon_id_var = tk.StringVar()
Ent_Id_mon = ttk.Entry(Id_month_frame,width=10,textvariable=mon_id_var)
Ent_Id_mon.place(x=0,y=20)






mon_id_Month_var = tk.StringVar()
com_Id_mon = ttk.Combobox(Id_month_frame,width=10,textvariable=mon_id_Month_var,value=[a for a in dic_for_month],
    state='readonly') # for Month:
com_Id_mon.place(x=80,y=20)

mon_id_Year_var = tk.StringVar()
com_y_Id_mon = ttk.Combobox(Id_month_frame,width=10,textvariable=mon_id_Year_var,value=[a for a in range(2023,2050)],
    state='readonly') # for year:
com_y_Id_mon.place(x=175,y=20)

def calculate_hours(_ID,_mon,_year):

    query = f"SELECT Date,Time,Status FROM data WHERE ID ='{_ID}' AND MONTH(Date) = '{dic_for_month[_mon]}' AND YEAR(Date) = '{_year}'"
    my_cursor.execute(query)
    _date =''
    h1,m1,s1="","",""
    h2,m2,s2="","",""
    p =timedelta(hours=0,minutes=0,seconds=0)    

    for row in my_cursor:
        if status_list[0]==row[2]:
            _date = row[0]
            h1,m1,s1=row[1].split(':')
            continue
        elif _date==row[0] and status_list[1]==row[2]:
            h2,m2,s2=row[1].split(':')
        else:
            _date=''
            h1,m1,s1=0,0,0
        p += timedelta(hours=int(h2),minutes=int(m2),seconds=int(s2))-timedelta(hours=int(h1),minutes=int(m1),seconds=int(s1))
    return p

month_status_obj = []

def month_status():
    _ID = mon_id_var.get()
    _mon = mon_id_Month_var.get()
    _year = mon_id_Year_var.get()

    if len(month_status_obj)>0:
        month_status_obj[1].destroy()
        month_status_obj[0].destroy()
        month_status_obj.pop()
        month_status_obj.pop()

    if _ID=='' or _mon=='' or _year=='':
        ms.showerror('Error',"Please fill the all fields:")
    elif check_ID(_ID)==False:
        ms.showerror("Error",f"This ID {_ID} is not exist:")
    else:
        query = f"SELECT * FROM data WHERE ID ='{_ID}' AND MONTH(Date) = '{dic_for_month[_mon]}' AND YEAR(Date) = '{_year}'"
        my_cursor.execute(query)


        column =['Date','Time',"ID","Name","Status"]

        tree_check_hour = ttk.Treeview(below_id_mon_frame,height=7,columns=column,show="headings")

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

        scl_bar = ttk.Scrollbar(below_id_mon_frame,orient='vertical') ### scroll bar
        scl_bar.grid(row=0,column=1,sticky='ns')

        scl_bar.configure(command=tree_check_hour.yview)
        tree_check_hour.configure(yscrollcommand=scl_bar.set)

        #calculating hours
        Cal_hours_Id_mon = ttk.Label(Id_month_frame,text=calculate_hours(_ID,_mon,_year))#Cal hour label in check hour
        Cal_hours_Id_mon.place(x=400,y=0)

        month_status_obj.append(tree_check_hour)
        month_status_obj.append(Cal_hours_Id_mon)

        Ent_Id_mon.delete(0,tk.END)
        mon_id_Month_var.set('')
        mon_id_Year_var.set('')



btn_Id_mon = ttk.Button(Id_month_frame,text="Enter",command =month_status)
btn_Id_mon.place(x=40,y=45)

def print_table():

    if len(month_status_obj)==0:
        ms.showerror("Error","Please, first create the table:")
        return
    rows = month_status_obj[0].get_children()
    data = [['Date','Time',"ID","Name","Status"]]
    for row in rows:
        values = []
        for col in range(len(month_status_obj[0]["columns"])):
            value = month_status_obj[0].item(row, "values")[col]
            values.append(value)
        data.append(values)



    saveas = filedialog.asksaveasfile(mode='w',title="Save File",defaultextension="pdf",filetypes=[("PDF", "*.pdf")])
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

print_check_hours = ttk.Button(Id_month_frame,text="Print",command =lambda : print_table())
print_check_hours.place(x=140,y=45)


win.mainloop()


conn.close()
