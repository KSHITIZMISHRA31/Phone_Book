try:
    from Tkinter import *
except:
    from tkinter import *
import sqlite3
from tkinter import messagebox
con = sqlite3.Connection('hrdb')
cur = con.cursor()

def detailgui(name):
    def edit():
        def edi():
            data_pb=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),x[0][0])
            cur.execute('UPDATE ph_bk set fname=?,mname=?,lname=?,coname=?,address=?,city=?,pincode=?,web=?,dob=? where sno=?',data_pb)
            con.commit()
            if e11.get()!='':
                cur.execute('UPDATE ph_num set phnum=?,phtype=? where sno=?',(e11.get(),e10.get(),x[0][0]))
                con.commit()
            if e13.get()!='':
                cur.execute('UPDATE ph_em set emid=?,emtype=? where sno=?',(e13.get(),e12.get(),x[0][0]))
                con.commit()
            messagebox.showinfo('UPDATE','Contact Updated Successfully')
            root1.destroy()
            
        def clo():
            jk=messagebox.askokcancel('Alert','Unsaved Changes May Lost')
            if jk==True:
                root1.destroy()
        root.destroy()
        #GUI for update
        root1 = Tk()
        root1.title("EDIT")
        root1.configure(bg='azure2')
        root1.geometry('330x400')
        Label(root1,text = 'EDIT CONTACT',font = 'Arial 20 bold',fg = 'Blue',bg='azure2').grid(row=0,column=0,columnspan=2)
        Label(root1,text = 'First Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=2,column=0,sticky=E)
        Label(root1,text = 'Middle Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=3,column=0,sticky=E)
        Label(root1,text = 'Last Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=4,column=0,sticky=E)
        Label(root1,text = 'Company Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=5,column=0,sticky=E)
        Label(root1,text = 'Address : ',font = 'Arial 12 bold',bg='azure2').grid(row=6,column=0,sticky=E)
        Label(root1,text = 'City : ',font = 'Arial 12 bold',bg='azure2').grid(row=7,column=0,sticky=E)
        Label(root1,text = 'Pincode : ',font = 'Arial 12 bold',bg='azure2').grid(row=8,column=0,sticky=E)
        Label(root1,text = 'Website URL : ',font = 'Arial 12 bold',bg='azure2').grid(row=9,column=0,sticky=E)
        Label(root1,text = 'Date of Birth : ',font = 'Arial 12 bold',bg='azure2').grid(row=10,column=0,sticky=E)
        Label(root1,text = 'Phone No type : ',font = 'Arial 12 bold',bg='azure2').grid(row=11,column=0,sticky=E)
        Label(root1,text = 'Phone Number : ',font = 'Arial 12 bold',bg='azure2').grid(row=12,column=0,sticky=E)
        Label(root1,text = 'Email Type : ',font = 'Arial 12 bold',bg='azure2').grid(row=13,column=0,sticky=E)
        Label(root1,text = 'Email Id : ',font = 'Arial 12 bold',bg='azure2').grid(row=14,column=0,sticky=E)
        e1 = Entry(root1)
        e1.insert(0, x[0][1])
        e1.grid(row=2,column=1)
        e2 = Entry(root1)
        e2.insert(0, x[0][2])
        e2.grid(row=3,column=1)
        e3 = Entry(root1)
        e3.insert(0, x[0][3])
        e3.grid(row=4,column=1)
        e4 = Entry(root1)
        e4.insert(0, x[0][4])
        e4.grid(row=5,column=1)
        e5 = Entry(root1)
        e5.insert(0, x[0][5])
        e5.grid(row=6,column=1)
        e6 = Entry(root1)
        e6.insert(0, x[0][6])
        e6.grid(row=7,column=1)
        e7 = Entry(root1)
        e7.insert(0, x[0][7])
        e7.grid(row=8,column=1)
        e8 = Entry(root1)
        e8.insert(0, x[0][8])
        e8.grid(row=9,column=1)
        e9 = Entry(root1)
        e9.insert(0, x[0][9])
        e9.grid(row=10,column=1)
        #for number_type
        try:
            e10=Entry(root1)
            e10.insert(0,p[0][1])
            e10.grid(row=11,column=1)
        except:
            e10=Entry(root1)
            e10.insert(0,'')
            e10.grid(row=11,column=1)
        #for ph_number
        try:
            e11=Entry(root1)
            e11.insert(0,p[0][2])
            e11.grid(row=12,column=1)
        except:
            e11=Entry(root1)
            e11.insert(0,'')
            e11.grid(row=12,column=1)
        #for em_type
        try:
            e12=Entry(root1)
            e12.insert(0,q[0][1])
            e12.grid(row=13,column=1)
        except:
            e12=Entry(root1)
            e12.insert(0,'')
            e12.grid(row=13,column=1)
        #for em
        try:
            e13=Entry(root1)
            e13.insert(0,q[0][2])
            e13.grid(row=14,column=1)
        except:
            e13=Entry(root1)
            e13.insert(0,'')
            e13.grid(row=14,column=1)
            
        Button(root1,text = 'Save',command=edi,bg = 'Black',fg = 'White',font = '30').grid(row=15,column=0)
        Button(root1,text = 'Exit',command=clo,bg = 'Black',fg = 'White',font = '30').grid(row=15,column=2)
        root1.mainloop()
        
    def delete_rec():
        cur.execute('delete from ph_num where sno=?',(x[0][0],))
        con.commit()
        cur.execute('delete from ph_em where sno=?',(x[0][0],))
        con.commit()
        cur.execute('delete from ph_bk where sno=?',(x[0][0],))
        con.commit()
        
        messagebox.showinfo('saved','Contact Deleted Successfully')
        root.destroy()
        return
            
    def close():
        p=messagebox.askokcancel('Alert','OK TO EXIT')
        if p==True:
            root.destroy()       

    y = ['','','']
    x = name.split(' ')
    for i in range(len(x)):
        y[i] = x[i]
    #query to select data from table
    cur.execute('select * from ph_bk where fname=? and mname=? and lname=?',tuple(y))
    x = cur.fetchall()
    cur.execute('select * from ph_num where sno=?',(x[0][0],))
    p = cur.fetchall()
    cur.execute('select * from ph_em where sno=?',(x[0][0],))
    q = cur.fetchall()
    
    root = Tk()
    root.title("PHONE_BOOK")
    root.configure(bg='azure2')
    root.geometry('330x400')
    #Label for details page 
    Label(root,text = ' CONTACT DETAILS ',font = 'Arial 20 bold',fg = 'Blue',bg='azure2').grid(row=0,column=0,columnspan=2)
    Label(root,text = 'First Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=2,column=0,sticky=E)
    Label(root,text = 'Middle Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=3,column=0,sticky=E)
    Label(root,text = 'Last Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=4,column=0,sticky=E)
    Label(root,text = 'Company Name : ',font = 'Arial 12 bold',bg='azure2').grid(row=5,column=0,sticky=E)
    Label(root,text = 'Address : ',font = 'Arial 12 bold',bg='azure2').grid(row=6,column=0,sticky=E)
    Label(root,text = 'City : ',font = 'Arial 12 bold',bg='azure2').grid(row=7,column=0,sticky=E)
    Label(root,text = 'Pincode : ',font = 'Arial 12 bold',bg='azure2').grid(row=8,column=0,sticky=E)
    Label(root,text = 'Website URL : ',font = 'Arial 12 bold',bg='azure2').grid(row=9,column=0,sticky=E)
    Label(root,text = 'Date of Birth : ',font = 'Arial 12 bold',bg='azure2').grid(row=10,column=0,sticky=E)
    Label(root,text = 'Phone No type : ',font = 'Arial 12 bold',bg='azure2').grid(row=11,column=0,sticky=E)
    Label(root,text = 'Phone Number : ',font = 'Arial 12 bold',bg='azure2').grid(row=12,column=0,sticky=E)
    Label(root,text = 'Email Type : ',font = 'Arial 12 bold',bg='azure2').grid(row=13,column=0,sticky=E)
    Label(root,text = 'Email Id : ',font = 'Arial 12 bold',bg='azure2').grid(row=14,column=0,sticky=E)
    #details
    Label(root,text = x[0][1],bg='azure2').grid(row=2,column=1,sticky=W)
    Label(root,text = x[0][2],bg='azure2').grid(row=3,column=1,sticky=W)
    Label(root,text = x[0][3],bg='azure2').grid(row=4,column=1,sticky=W)
    Label(root,text = x[0][4],bg='azure2').grid(row=5,column=1,sticky=W)
    Label(root,text = x[0][5],bg='azure2').grid(row=6,column=1,sticky=W)
    Label(root,text = x[0][6],bg='azure2').grid(row=7,column=1,sticky=W)
    Label(root,text = x[0][7],bg='azure2').grid(row=8,column=1,sticky=W)
    Label(root,text = x[0][8],bg='azure2').grid(row=9,column=1,sticky=W)
    Label(root,text = x[0][9],bg='azure2').grid(row=10,column=1,sticky=W)
    try:
        Label(root,text = p[0][1],bg='azure2').grid(row=11,column=1,sticky=W)
    except:
        Label(root,text = '',bg='azure2').grid(row=11,column=1,sticky=W)
    try:
        Label(root,text = p[0][2],bg='azure2').grid(row=12,column=1,sticky=W)
    except:
        Label(root,text = '',bg='azure2').grid(row=12,column=1,sticky=W)
    try:
        Label(root,text = q[0][1],bg='azure2').grid(row=13,column=1,sticky=W)
    except:
        Label(root,text = '',bg='azure2').grid(row=13,column=1,sticky=W)
    try:
        Label(root,text = q[0][2],bg='azure2').grid(row=14,column=1,sticky=W)
    except:
        Label(root,text = '',bg='azure2').grid(row=14,column=1,sticky=W)
    #buttons
    Button(root,text = 'Update',command=edit,bg = 'Black',fg = 'White',font = '30').grid(row=15,column=0)
    Button(root,text = 'Delete',command=delete_rec,bg = 'Black',fg = 'White',font = '30').grid(row=15,column=1)
    Button(root,text = 'Exit',command=close,bg = 'Black',fg = 'White',font = '30').grid(row=15,column=2)
    root.mainloop()    
    return