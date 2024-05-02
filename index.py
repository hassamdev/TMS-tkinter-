print("Balancesheet")


from csv import DictWriter as Dw
from csv import DictReader as Dr
import os 
from tkinter import messagebox as ms

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import customtkinter as ctk



def balance_sheet(fr,win,back,sign,email):
    fr.destroy()
    # win = tk.Tk()
    # win.title("Creating Balancesheet:")
    win.geometry("500x400")

    frame = ctk.CTkFrame(win)
    frame.pack(padx=30,pady=60,fill='both',expand = True)

    back_btn = ctk.CTkButton(frame,text="back",width=10,command=lambda : back(frame,sign,email=email),corner_radius=100)
    back_btn.place(x=5,y=5)

    main_label = ctk.CTkLabel(frame,text="Balance Sheet")
    main_label.place(x=300,y=5)
    column_list=["Date","Description","Amount"]

    tree_fr = ttk.Frame(frame)
    tree_fr.place(x=0,y=50)

    tree1_fr = ttk.Frame(frame)
    tree1_fr.place(x=450,y=50)



    #  entry frame _

    ent_frame = ttk.Frame(frame,borderwidth=5,relief="solid")
    ent_frame.place(x=900,y=25)

    date_label1 = ttk.Label(ent_frame,text="Date",width=30,background='#7fbeeb',font=('helvetica 10 bold'),
        borderwidth=5,relief='solid')
    date_label1.pack()

    date_ent = DateEntry(ent_frame,width = 25)
    date_ent.pack()

    description_label1 = ttk.Label(ent_frame,text="Description",width=30,background='#7fbeeb',font=('helvetica 10 bold'),
        borderwidth=5,relief='solid')
    description_label1.pack()

    des_ent = ttk.Entry(ent_frame,width = 30)
    des_ent.pack()

    Amount_label1 = ttk.Label(ent_frame,text="Amount",width=30,background='#7fbeeb',font=('helvetica 10 bold'),
        borderwidth=5,relief='solid')
    Amount_label1.pack()


    am_ent = ttk.Entry(ent_frame,width = 30)
    am_ent.pack()

    obj_list=[]

    def btn_click():
        
        
        date = date_ent.get()
        des = des_ent.get()
        amount = am_ent.get()
        
        if date=="" or des =="" or amount=="":
            ms.showerror("Error ","please fill the fields:")
        else:

            try:
                int(amount)

            except ValueError:
                ms.showerror('Error',"enter only integers in amount")
            else:
                with open("balance.csv","a",newline="") as f:
                    wr = Dw(f,fieldnames=["Date","Description","Amount"])
                    if os.stat("balance.csv").st_size==0:
                        wr.writeheader()
                    wr.writerow({
                        "Date":date,
                        "Description":des,
                        "Amount":amount
                    })
                tmp_list=["Date","Description","Amount"]
                with open("balance.csv","r") as f:
                    obj_R = Dr(f)
                    r=1
                    c=0
                    
                    if len(obj_list)>0:
                        obj_list[0].destroy()
        
                    
                    tree = ttk.Treeview(tree_fr,columns=column_list,show="headings",height=40)
                    tree.heading(column_list[0],text=column_list[0])
                    tree.heading(column_list[1],text=column_list[1])
                    tree.heading(column_list[2],text=column_list[2])

                    tree.column(column_list[0],width=100,anchor=tk.CENTER)
                    tree.column(column_list[1],width=200,anchor=tk.CENTER)
                    tree.column(column_list[2],width=100,anchor=tk.CENTER)
                    c=0
                    for row in obj_R:
                        c+=1
                        if c%2==0:
                            tree.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("even",))
                        else:
                            tree.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("odd",))
                        
                    tree.tag_configure('even',foreground="black",background="white")
                    tree.tag_configure('odd',foreground="white",background="black")
                    
                    tree.grid(row=0,column=0,sticky="nesw")
                    
                    scl_bar = ttk.Scrollbar(tree_fr,orient="vertical")
                    scl_bar.grid(row=0,column=1,sticky="ns")
                    scl_bar.configure(command=tree.yview)
                    tree.configure(yscrollcommand=scl_bar.set)
                    
                    Sum_btn = ttk.Button(tree_fr,text="Sum",command = lambda : sum_click(tree))
                    Sum_btn.grid(row=1,column=0)
                    
                    obj_list.append(tree)
                    
                date_ent.delete(0,tk.END)
                des_ent.delete(0,tk.END)
                am_ent.delete(0,tk.END)

    btn = ttk.Button(ent_frame,text="Add1",command = btn_click)
    btn.pack()

    def sum_click(Tr):
        
        if len(obj_list)==0:
            ms.showerror("Error","first create the table:")
            return
        temp =0
        
        r=0
        with open("balance.csv","r") as f:
            obj_R = Dr(f)
            for row in obj_R:
                r+=1
                temp += int(row['Amount'])
        print(temp)
        temp_=['Total',"",temp]
        
        Tr.insert('',tk.END,values=temp_ ,tags="blue")
        
        Tr.tag_configure('blue',foreground="white",background="blue")



    # def del_click():
    #     pass

    # Delete_btn = ttk.Button(ent_frame,text="Delete",command = None)
    # Delete_btn.pack()

    obj_list1=[]

    def show():
        
        if len(obj_list)>0:
            obj_list[0].destroy()
        
        tmp_list=["Date","Description","Amount"]
        with open("balance.csv","r") as f:
            obj_R = Dr(f)
            r=1
            c=0
            tree = ttk.Treeview(tree_fr,columns=column_list,show="headings",height=40)
            
            style = ttk.Style()
            style.configure('Treeview',borderwidth=1,highlightthickness=1,bd=1)
            tree.configure(style="Treeview")
            
            tree.heading(column_list[0],text=column_list[0])
            tree.heading(column_list[1],text=column_list[1])
            tree.heading(column_list[2],text=column_list[2])
            

            tree.column(column_list[0],width=100,anchor=tk.CENTER)
            tree.column(column_list[1],width=200,anchor=tk.CENTER)
            tree.column(column_list[2],width=100,anchor=tk.CENTER)

            c=0
            for row in obj_R:
                c+=1
                if c%2==0:
                    tree.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("even",))
                else:
                    tree.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("odd",))
                
            tree.tag_configure('even',foreground="black",background="white")
            tree.tag_configure('odd',foreground="white",background="black")
            
            tree.grid(row=0,column=0,sticky="nesw")
            
            scl_bar = ttk.Scrollbar(tree_fr,orient="vertical")
            scl_bar.grid(row=0,column=1,sticky="ns")
            scl_bar.configure(command=tree.yview)
            tree.configure(yscrollcommand=scl_bar.set)
            
            Sum_btn = ttk.Button(tree_fr,text="Sum",command = lambda : sum_click(tree))
            Sum_btn.grid(row=1,column=0)
            
            obj_list.append(tree)
        
        if len(obj_list1)>0:
            obj_list1[0].destroy()
        
        tmp_list=["Date","Description","Amount"]
        with open("data.csv","r") as f:
            obj_R = Dr(f)
            r=1
            c=0
            tree1 = ttk.Treeview(tree1_fr,columns=column_list,show="headings",height=40)
            tree1.heading(column_list[0],text=column_list[0])
            tree1.heading(column_list[1],text=column_list[1])
            tree1.heading(column_list[2],text=column_list[2])

            tree1.column(column_list[0],width=100,anchor=tk.CENTER)
            tree1.column(column_list[1],width=200,anchor=tk.CENTER)
            tree1.column(column_list[2],width=100,anchor=tk.CENTER)
            c=0
            for row in obj_R:
                c+=1
                if c%2==0:
                    tree1.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("even",))
                else:
                    tree1.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("odd",))
                
            tree1.tag_configure('even',foreground="black",background="white")
            tree1.tag_configure('odd',foreground="white",background="black")
            
            tree1.grid(row=0,column=0,sticky="nesw")
            
            
            scl_bar = ttk.Scrollbar(tree1_fr,orient="vertical")
            scl_bar.grid(row=0,column=1,sticky="ns")
            scl_bar.configure(command=tree.yview)
            tree1.configure(yscrollcommand=scl_bar.set)
            
            Sum2_btn = ttk.Button(tree1_fr,text="Sum2",command = lambda : sum2_click(tree1))
            Sum2_btn.grid(row=1,column=0)
            
            obj_list1.append(tree1)
            
            # fr= ttk.Frame(win)
            # fr.place(x=900,y =300)
            
            # Amount_lab = ttk.Label(fr,text="CurrentAmount:")
            # Amount_lab.pack()
            
            # sub_fr = ttk.Frame(fr)
            # sub_fr.pack()
            
            # ttk.abel(sub_fr,text="hassam").pack()
            
            # curr_btn = ttk.Button(fr,text="action")
            # curr_btn.pack()


    Show_Table_btn = ttk.Button(ent_frame,text="Show Table",command = show)
    Show_Table_btn.pack()

            

    def add2_click():
        date = date_ent.get()
        des = des_ent.get()
        amount = am_ent.get()
        
        if date=="" or des =="" or amount=="":
            ms.showerror("Error ","please fill the fields:")
        else:

            try:
                int(amount)

            except ValueError:
                ms.showerror('Error',"enter only integers in amount")
            else:
                with open("data.csv","a",newline="") as f:
                    wr = Dw(f,fieldnames=["Date","Description","Amount"])
                    if os.stat("data.csv").st_size==0:
                        wr.writeheader()
                    wr.writerow({
                        "Date":date,
                        "Description":des,
                        "Amount":amount
                    })
                tmp_list=["Date","Description","Amount"]
                with open("data.csv","r") as f:
                    obj_R = Dr(f)
                    r=1
                    c=0
                    
                    if len(obj_list1)>0:
                        obj_list1[0].destroy()
        
                    
                    tree = ttk.Treeview(tree1_fr,columns=column_list,show="headings",height=40)
                    tree.heading(column_list[0],text=column_list[0])
                    tree.heading(column_list[1],text=column_list[1])
                    tree.heading(column_list[2],text=column_list[2])

                    tree.column(column_list[0],width=100,anchor=tk.CENTER)
                    tree.column(column_list[1],width=200,anchor=tk.CENTER)
                    tree.column(column_list[2],width=100,anchor=tk.CENTER)
                    c=0
                    for row in obj_R:
                        c+=1
                        if c%2==0:
                            tree.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("even",))
                        else:
                            tree.insert('',tk.END,values=[row[a] for a in tmp_list],tags=("odd",))
                
                    tree.tag_configure('even',foreground="black",background="white")
                    tree.tag_configure('odd',foreground="white",background="black")
                    
                    tree.grid(row=0,column=0,sticky="nesw")
                    
                    scl_bar = ttk.Scrollbar(tree1_fr,orient="vertical")
                    scl_bar.grid(row=0,column=1,sticky="ns")
                    scl_bar.configure(command=tree.yview)
                    tree.configure(yscrollcommand=scl_bar.set)
                    
                    Sum2_btn = ttk.Button(tree1_fr,text="Sum2",command = lambda : sum2_click(tree))
                    Sum2_btn.grid(row=1,column=0)
                    
                    obj_list1.append(tree)
                    
                date_ent.delete(0,tk.END)
                des_ent.delete(0,tk.END)
                am_ent.delete(0,tk.END)



    add2_btn = ttk.Button(ent_frame,text="Add2",command = add2_click)
    add2_btn.pack()

    def sum2_click(Tr):
        if len(obj_list1)==0:
            ms.showerror("Error","first create the table:")
            return
        temp =0
        
        r=0
        with open("data.csv","r") as f:
            obj_R = Dr(f)
            for row in obj_R:
                r+=1
                temp += int(row['Amount'])
        print(temp)
        temp_=['Total',"",temp]
        
        Tr.insert('',tk.END,values=temp_ ,tags="blue")
        
        Tr.tag_configure('blue',foreground="white",background="blue")















# win.mainloop()
