import tkinter as tk
from tkinter import simpledialog
import mysql.connector
import sys

db = mysql.connector.connect(host= "localhost", user="root", password= "admin", database= "ace")
cursor = db.cursor()

def popfunc(strval):
    pop = tk.Toplevel(root)
    pop_label= tk.Label(pop,text=strval)
    pop_label.pack()
def savedata():
    try:
        name_file = simpledialog.askstring("File name", "Enter the name of the file")
        data= text.get("1.0","end")
        cmd="INSERT INTO data(name,content) VALUES(%s,%s)"
        cursor.execute(cmd, (name_file,data))
        db.commit()
    except:
        popfunc("It literally says SAVE and not APPEND")

def openfile():
    try:
        global pop
        name_file = simpledialog.askstring("File name", "Enter the name of the file")
        cmd= "SELECT content from data where name= %s"
        val = (name_file,)
        cursor.execute(cmd,val)
        results= cursor.fetchall()
        for i in results:
            text.insert(1.0,i)
    except:
        popfunc("You cannot open that file ")

def delfile():
    try:
        name_file = simpledialog.askstring("File name", "Enter the name of the file")
        cmd = "DELETE from data where name= %s"
        val=(name_file,)
        cursor.execute(cmd, val)
        db.commit()
    except:
        popfunc("It already does not exist what do you even mean")

def appfile():
    try:
        name_file = simpledialog.askstring("File name", "Enter the name of the file")
        data= text.get("1.0","end")
        cmd= "UPDATE data SET content= %s where name=%s"
        val= (data, name_file)
        cursor.execute(cmd, val)
        db.commit() 
    except:
        popfunc("First create a file, skill issue")

def showfile():
    global pop
    cursor.execute("Select name from data")
    results= cursor.fetchall()
    names=""

    pop = tk.Toplevel(root)
    pop.title("File names")
    pop.geometry("800x1000")
    
    for j in results:
        names=j
        pop_label= tk.Label(pop,text=names)
        pop_label.pack()

def closefile():
    close=sys.exit()
root = tk.Tk()

root.title("Notepad")
root.geometry("800x450")


text= tk.Text(root)
text.pack(fill='x')

btframe= tk.Frame(root)
btframe.columnconfigure(0,weight=1)
btframe.columnconfigure(1,weight=1)

openbt= tk.Button(btframe, text="Open", command = openfile)
openbt.grid(row=0,column=0, sticky=tk.W+tk.E)

savebt= tk.Button(btframe, text="Save", command= savedata)
savebt.grid(row=0,column=1, sticky=tk.W+tk.E)

delbt= tk.Button(btframe, text="Delete",command= delfile)
delbt.grid(row=0,column=2, sticky=tk.W+tk.E)

appendbt= tk.Button(btframe, text="Append",command= appfile)
appendbt.grid(row=1,column=0, sticky=tk.W+tk.E)

showbt= tk.Button(btframe, text="Show Files", command= showfile)
showbt.grid(row=1,column=1, sticky=tk.W+tk.E)

closebt= tk.Button(btframe, text="Close", command=closefile)
closebt.grid(row=1,column=2, sticky=tk.W+tk.E)

btframe.pack(fill='x')

root.mainloop()