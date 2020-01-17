try:
    from Tkinter import *
except:
    from tkinter import *
from tkinter import messagebox
from searchcont import *
import sqlite3
con = sqlite3.Connection('hrdb')
cur = con.cursor()
#SQL Tables
cur.execute('create table if not exists ph_bk(sno number primary key,fname varchar(15) default "UNKNOWN",mname varchar(15) default "NULL" ,lname varchar(15) default "NULL" ,coname varchar(30) default "NULL" ,address varchar(30) default "NULL",city varchar(20) default "NULL",pincode varchar(15) default "NULL" ,web varchar(30) default "NULL" ,dob varchar(10) default sysdate)')
cur.execute('create table if not exists ph_num(sno number ,phnum number,phtype varchar(15),primary key(sno,phnum),CONSTRAINT fk_sno FOREIGN KEY(sno) REFERENCES ph_bk(sno))')
cur.execute('create table if not exists ph_em(sno number,emid varchar(30),emtype varchar(10),primary key(sno,emid), CONSTRAINT fk_sno FOREIGN KEY(sno) REFERENCES ph_bk(sno))')
con.commit()

#Intro Window
intro = Tk()
def destroy(e=1):
    intro.destroy()
intro.title("DEVELOPER")
intro.geometry('800x300')
intro.configure(bg='azure2')
Label(intro,text = 'JAYPEE UNIVERSITY OF ENGINEERING & TECHNOLOGY',font = 'Arial 20 bold',fg = 'Blue',bg='azure2').pack()
Label(intro,text = 'PHONEBOOK PROJECT',font = 'Arial 20 bold underline',fg = 'Blue',bg='azure2').pack()
Label(intro,text = 'DEVELOPED BY',font = 'Arial',fg = 'Blue',bg='azure2').pack()
Label(intro,text = 'KSHITIZ MISHRA',font = 'Arial',fg = 'Blue',bg='azure2').pack()
Label(intro,text = '181B111',font = 'Arial',fg = 'Blue',bg='azure2').pack()

intro.bind('<Motion>',destroy)
intro.mainloop()
    

#page to save contact
def save():
    if v10.get()==1:
        e10='OFFICE'
    elif v10.get()==2:
        e10='HOME'
    else :
        e10='OTHER '
        
    if v12.get()==1:
        e12='OFFICE'
    else :
        e12='PERSONAL'
    
    try :
        v11=int(e11.get())
    except:
        Label(root,text = '* must be in number',font = 'Arial 8',fg = 'Red').grid(row=12,column=2)
        return    
           
    data_pb = [0,str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get()),str(e6.get()),str(e7.get()),str(e8.get()),str(e9.get())]
    data_num=[0,str(e10),int(e11.get())]
    data_em=[0,str(e12),str(e13.get())]
    inputqry(data_pb,data_num,data_em)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e11.delete(0,END)
    e13.delete(0,END)

def update():
    messagebox.showinfo('Update','Update Rolls out Soon')
    
def close():
    x=messagebox.askokcancel('Alert','OK TO EXIT')
    if x==True:
        root.destroy()
    

root = Tk()
root.title("PHONE_BOOK")
root.configure(bg='azure2')
root.geometry('550x700')
img=PhotoImage(file ='ph_img.gif')
#Labels
Label(root,image=img).grid(row=0,column=1) 
Label(root,text = '  Phone Book  ',font = 'Arial 20 bold',fg = 'Blue',bg='azure2').grid(row=1,column=1)
Label(root,text = 'First Name',bg='azure2').grid(row=2,column=0,sticky=E)
Label(root,text = 'Middle Name',bg='azure2').grid(row=3,column=0,sticky=E)
Label(root,text = 'Last Name',bg='azure2').grid(row=4,column=0,sticky=E)
Label(root,text = 'Company Name',bg='azure2').grid(row=5,column=0,sticky=E)
Label(root,text = 'Address',bg='azure2').grid(row=6,column=0,sticky=E)
Label(root,text = 'City',bg='azure2').grid(row=7,column=0,sticky=E)
Label(root,text = 'Pincode',bg='azure2').grid(row=8,column=0,sticky=E)
Label(root,text = 'Website URL',bg='azure2').grid(row=9,column=0,sticky=E)
Label(root,text = 'Date of Birth',bg='azure2').grid(row=10,column=0,sticky=E)
Label(root,text = 'dd-mm-yyyy {1-jan-2000}',font = 'Arial 8',fg = 'Blue',bg='azure2').grid(row=10,column=2,sticky=W)
Label(root,text = 'Phone No type',bg = 'Yellow').grid(row=11,column=0,sticky=E)
Label(root,text = 'Phone Number',bg='azure2').grid(row=12,column=0,sticky=E)
Label(root,text = 'Email Type',bg = 'Yellow').grid(row=13,column=0,sticky=E)
Label(root,text = 'Email Id',bg='azure2').grid(row=14,column=0,sticky=E)

#Entry
e1 = Entry(root)
e1.grid(row=2,column=1)
e2 = Entry(root)
e2.grid(row=3,column=1)
e3 = Entry(root)
e3.grid(row=4,column=1)
e4 = Entry(root)
e4.grid(row=5,column=1)
e5 = Entry(root)
e5.grid(row=6,column=1)
e6 = Entry(root)
e6.grid(row=7,column=1)
e7 = Entry(root)
e7.grid(row=8,column=1)
e8 = Entry(root)
e8.grid(row=9,column=1)
e9 = Entry(root)
e9.grid(row=10,column=1)
e11 = Entry(root)
e11.grid(row=12,column=1)
e13 = Entry(root)
e13.grid(row=14,column=1)

#Radio Button
v10=IntVar()
Radiobutton(root,text='OFFICE',variable=v10,value =1,bg='azure2').grid(row=11,column=1)
Radiobutton(root,text='HOME  ',variable=v10,value =2,bg='azure2').grid(row=11,column=2)
Radiobutton(root,text='OTHER ',variable=v10,value =3,bg='azure2').grid(row=11,column=3)
v12=IntVar()
Radiobutton(root,text='OFFICE  ',variable=v12,value =1,bg='azure2').grid(row=13,column=1)
Radiobutton(root,text='PERSONAL',variable=v12,value =2,bg='azure2').grid(row=13,column=2)
#Button
Button(root,text='Save',bg = 'Black',fg = 'White',font = '30',command=save).grid(row=15,column=0)
Button(root,text='Close',bg = 'Black',fg = 'White',font = '30',command
       =close).grid(row=15,column=2)
Button(root,text='Search',bg = 'Black',fg = 'White',font = '30',command=searchgui).grid(row=15,column=1)
Button(root,text='+',bg = 'Black',fg = 'White',font = '30',padx=10,command=update).grid(row=12,column=3)

root.mainloop()
