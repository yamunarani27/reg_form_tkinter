from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

root=Tk()
root.title('python+tkinter+mysql')
root.geometry("400x400")

def insertfn():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()

    if (id=="" or name=="" or phone==""):
        messagebox.showinfo("All fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="mydatabase")
        mycursor=con.cursor()
        mycursor.execute("insert into customers values('"+id+"','"+name+"','"+phone+"')")
        mycursor.execute("commit")

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        messagebox.showinfo("Inserted successfully")
        con.close()
    
def deletefn():
    if(e_id.get()==""):
        messagebox.showinfo("ID is compulsary for delete")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="mydatabase")
        mycursor=con.cursor()
        mycursor.execute("DELETE  FROM customers WHERE id='"+e_id.get()+"'")
        mycursor.execute("commit")

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        messagebox.showinfo("deleted successfully")
        con.close()

def updatefn():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()

    if (id=="" or name=="" or phone==""):
        messagebox.showinfo("All fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="mydatabase")
        mycursor=con.cursor()
        mycursor.execute("update customers set name='"+name+"',phone='"+phone"' WHERE id='"+e_id.get()+"' ")
        mycursor.execute("commit")

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        messagebox.showinfo("updated successfully")
        con.close()


def getfn():
    if(e_id.get()==""):
        messagebox.showinfo("ID is compulsary")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="mydatabase")
        mycursor=con.cursor()
        mycursor.execute("SELECT * FROM customers WHERE id='"+e_id.get()+"'")
        rows=mycursor.fetchall()
        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0,row[2])
            con.close()
def show():
        con=mysql.connect(host="localhost",user="root",password="",database="mydatabase")
        mycursor=con.cursor()
        mycursor.execute("SELECT * FROM customers")
        rows=mycursor.fetchall()
        for row in rows:
          insertdata=str(row[0])+'         '+row[1]
          list.insert(list.size()+1,insertdata)
        con.close()

id=Label(root,text="Enter id")
id.place(x=20,y=30)
name=Label(root,text="Enter name")
name.place(x=20,y=60)
phone=Label(root,text="Enter phone")
phone.place(x=20,y=90)
e_id=Entry()
e_id.place(x=100,y=30)
e_name=Entry()
e_name.place(x=100,y=60)
e_phone=Entry()
e_phone.place(x=100,y=90)

#insert values into db
insert=Button(root,text="Insert",command=insertfn)
insert.place(x=30,y=150)

#given id ,delete values of the corresponding id
delete=Button(root,text="Delete",command=deletefn)
delete.place(x=200,y=150)

#given id,displays values of the corresponding id in their respective fields
get=Button(root,text="Get",command=getfn)
get.place(x=100,y=150)

#update changes the existing values in the given id
update=Button(root,text="Update",command=updatefn)
update.place(x=200,y=150)

#display values at the side of tkinter window
list=Listbox(root)
list.place(x=250,y=30)
show()

root.mainloop(
