try:
    from Tkinter import *
except:
    from tkinter import *
from tkinter import messagebox
from detailcont import*
import sqlite3
con = sqlite3.Connection('hrdb')
cur = con.cursor()
############################################################################

#search
def searchgui():
    
    def details(e=1):
        raw_data=(e1.get(e1.curselection()))
        root1.destroy()
        detailgui(raw_data)
        
    def search(e=1):
    
        e1.delete(0,END)
        a=str(v1.get())
        cur.execute('select fname,mname,lname from ph_bk where fname like"%'+str(a)+'%" or mname like "%'+str(a)+'%" or lname like "%'+str(a)+'%" order by fname')
        sdata = cur.fetchall()
        for i in range(len(sdata)):
            x = sdata[i][0]+' '+sdata[i][1]+' '+sdata[i][2]
            e1.insert(i+1,x)
        root1.bind("<Button-1>", details)

    #GUI for search page
    root1 = Tk()
    root1.title("SEARCH")
    root1.configure(bg='azure2')
    root1.geometry('520x700')
    Label(root1,text = 'SEARCH CONTACT',font = 'Arial 20 bold',fg = 'Black',bg='azure2').grid(row=0,column=1)
    Label(root1,text = 'Enter Name ',font = 'Arial 10 bold',bg='azure2').grid(row=1,column=0)
    v1 = Entry(root1)
    v1.grid(row=1,column=1)
    e1=Listbox(root1,height=40,width=40,font='Arial 18',fg='Blue',bg='light yellow')
    cur.execute('select count(*) from ph_bk')
    n = cur.fetchall()[0][0]
    cur.execute('select fname,mname,lname from ph_bk order by fname')
    data = cur.fetchall()
    for i in range(n):
        x = data[i][0]+' '+data[i][1]+' '+data[i][2]
        e1.insert(i+1,x)
    e1.grid(row=2,column=0,columnspan=3)
    root1.bind("<KeyPress>",search)
    root1.mainloop()
#########################################################################
#save contact to Database
def inputqry(data_pb,data_num,data_em):
    cur.execute('select max(sno) from ph_bk')
    try:
        va1 = cur.fetchall()[0][0]+1
    except:
        va1=0
    cur.execute('select count(*) from ph_bk')
    va2 = cur.fetchall()[0][0]+1
    if va1<=va2:
        e0=va2
    else:
        e0=va1
    data_pb[0],data_num[0],data_em[0] = e0,e0,e0
    data_pb,data_num,data_em=tuple(data_pb),tuple(data_num),tuple(data_em)

    cur.execute('insert into ph_bk values(?,?,?,?,?,?,?,?,?,?)',data_pb)

    if data_num[2]!='':
        try:
            cur.execute('insert into ph_num values(?,?,?)',data_num)
        except Exception as e:
            messagebox.showerror('Error',e)
            return

    if data_em[2]!='':
        try:
            cur.execute('insert into ph_em values(?,?,?)',data_em)
        except Exception as e:
            messagebox.showerror('Error',e)
            return

    con.commit()
    messagebox.showinfo('saved','Contact Saved Successfully')
    return




