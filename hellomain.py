from tkinter import *
from tkinter import messagebox
import mysql.connector
from hello import *

root = Tk()
root.title('Hello App')
root.iconbitmap('hello.ico')
root.geometry("390x100")
          
db = mysql.connector.connect(
    host="localhost",
    user="", # type your username here
    password="", # type your password here
    database="hello"
)
c = db.cursor()


run = Hello()
run.mainloop()
db.close()