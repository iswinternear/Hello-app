from tkinter import *
from tkinter import messagebox
import mysql.connector


# create database
"""
create new py file
import mysql.connector
copy line 12-20 and paste to file
"""
# db = mysql.connector.connect(
#     host="localhost",
#     user="",  # type your username here
#     password="" # type your password here
# )

# c = db.cursor()

# c.execute("CREATE DATABASE hello")

class Hello(Frame):
    
    db = c = None
    
    def __init__(self, master=None, *args, **kwargs):
        global db, c
        # connect to database
        db = mysql.connector.connect(
            host="localhost",
            user="", # type your username here
            password="", # type your password here
            database="hello"
        )
        c = db.cursor()
        
        Frame.__init__(self, master)
        self.grid()
        
        # name label
        name_lbl = Label(self, text="Name")
        name_lbl.grid(row=0, column=0, padx=5, pady=5)
        
        # name entry
        self.name_ent = Entry(self, width=30)
        self.name_ent.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky=W+E)
        
        # buttons
        # inserts name into log
        enter_btn = Button(self, text="Enter", command=self.enter, bg="light gray", width=10)
        enter_btn.grid(row=1,column=0, padx=(15,3), pady=3, sticky=EW)
        # shows the log
        show_btn = Button(self, text="Log", command=self.show, bg="light gray", width=10)
        show_btn.grid(row=1,column=1, padx=3, pady=3, ipadx=2, sticky=EW)
        # delete a name from the log
        delete_btn = Button(self, text="Delete", command=self.delete, bg="light gray", width=10)
        delete_btn.grid(row=1, column=2, padx=3, pady=3, sticky=EW)
        # clears the whole log
        clear_btn = Button(self, text="Clear", command=self.clear, bg="light gray", width=10)
        clear_btn.grid(row=1, column=3, padx=3, pady=3, sticky=EW)
        
    def create_table(self):
        # create table
        c.execute("CREATE TABLE Log (id int PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(50) NOT NULL)")
        
    #define enter method for "Enter" button
    def enter(self):
        # popup message after clicking "Enter" button
        wasup = messagebox.showinfo("Hello", "Hello " + self.name_ent.get() + "!")
        
        # inserting name into table
        name_insert = "INSERT INTO Log (name) VALUES (%s)"
        name_get = [self.name_ent.get()]
        c.execute(name_insert, name_get)
        # c.execute("INSERT INTO Log (name) VALUES(%s)", (self.ent.get()))
        
        db.commit()
        
        # clear text box after clicking the "Enter" button
        self.name_ent.delete(0, END)
        
    # create show method for "Log" button
    def show(self):
        # displays id and names from the Log table
        c.execute("SELECT * FROM Log")
        logs = c.fetchall()
        
        printlog = ""
        for log in logs:
            printlog += str(log) + "\n"
        
        # popup message after clicking "Show History"
        logsbox = messagebox.showinfo("Log", printlog)

    # create delete method for "Delete" button
    def delete(self):
        
        # id label
        id_lbl = Label(self, text="ID Number")
        id_lbl.grid(row=3, column=0, padx=5, pady=5)
        
        # id Entry
        self.id_ent = Entry(self, width=10,)
        self.id_ent.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky=W+E)
        
        # id button
        id_btn = Button(self, text="Confirm", command=self.confirm, bg="light gray", width=10)
        id_btn.grid(row=3, column=3, padx=3, pady=3, sticky=EW)
        
    # create confirm method for "Confirm" button
    def confirm(self):
        # delete a row from the table by using get()
        c.execute("DELETE FROM Log WHERE id = (%s)" % self.id_ent.get())
        
        db.commit()
        
        # clear text box after clicking the "Confirm button
        self.id_ent.delete(0, END)
    
    # create clear method for "Clear" button 
    def clear(self):
        c.execute("DELETE FROM Log")
        
        db.commit()
        
