import mysql.connector as mc
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk

#check

#MySQL connection
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True


#root
root=tb.Window()
root.title('eSports Management System')
root.iconbitmap('D:\\Project\\EMS.ico')
root.geometry('960x540')
tb.Style(theme="cyborg") ; t=1

#variables
admin1=Image.open('D:\\Project\\admin.png')
player1=Image.open('D:\\Project\\player.png')
resized_admin = admin1.resize((200, 200))
resized_player = player1.resize((200, 200))
admin=ImageTk.PhotoImage(resized_admin)
player=ImageTk.PhotoImage(resized_player)

#other definitions
def themeswap():
    global t
    if t==1:
        tb.Style(theme="cosmo")
        t=0
    elif t==0:
        tb.Style(theme="cyborg")
        t=1

def logout():
    L1.tkraise()

#page swap definitions
def admin_login():
    pass
def player_login():
    pass

#Frames
L1=tb.Frame(root)
LA=tb.Frame(root)

M1=tb.Frame(root)

f1=tb.Frame(root)
f2=tb.Frame(root)
f3=tb.Frame(root)
f4=tb.Frame(root)
f5=tb.Frame(root)
f6=tb.Frame(root)
f7=tb.Frame(root)
f8=tb.Frame(root)
f9=tb.Frame(root)

#L1 items
L1_1=tb.Frame(L1)
L1_title=tb.Label(L1, text='ESPORTS MANAGEMENT SYSTEM', font=('Times bold', 25), relief='groove', padding=5)
L1_title1=tb.Label(L1, text='SELECT LOGIN TYPE', font=('Times bold', 15))
L1_title2=tb.Label(L1, text='  ADMIN                                       PLAYER', font=('Times bold', 15))
b_admin=tb.Button(L1_1, text='ADMIN', image=admin, command=admin_login)
b_player=tb.Button(L1_1, text='PLAYER', image=player, command=player_login)


L1_title.pack(pady=20)
L1_title1.pack(pady=(20,20))
L1_1.pack(pady=20)
b_admin.pack(side='left', padx=40 )
b_player.pack(side='left', padx=40)
L1_title2.pack()


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
L1.grid(row=0, column=0, sticky="nsew")
LA.grid(row=0, column=0, sticky="nsew")
logout()
root.mainloop()