import mysql.connector as mc
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk
from ttkbootstrap.dialogs.dialogs import FontDialog
from tkinter.font import Font

#check

#MySQL connection
mydb = mc.connect(host="localhost",user="root",password="bruh",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True


#root
root=tb.Window()
root.title('eSports Management System')
root.iconbitmap('C:\\Users\\USER\\Python Prog\\CS-Project\\EMS.ico')
root.geometry('960x540')
tb.Style(theme="cyborg") ; t=1

#Images
admin1=Image.open('C:\\Users\\USER\\Python Prog\\CS-Project\\admin.png')
player1=Image.open('C:\\Users\\USER\\Python Prog\\CS-Project\\player.png')
resized_admin = admin1.resize((200, 200))
resized_player = player1.resize((200, 200))
admin=ImageTk.PhotoImage(resized_admin)
player=ImageTk.PhotoImage(resized_player)

see1=Image.open('C:\\Users\\USER\\Python Prog\\CS-Project\\see.png')
hide1=Image.open('C:\\Users\\USER\\Python Prog\\CS-Project\\hide.png')
resized_see = see1.resize((16, 16))
resized_hide = hide1.resize((16, 16))
see=ImageTk.PhotoImage(resized_see)
hide=ImageTk.PhotoImage(resized_hide)
t1=1

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

def eye_toggle():
    global pw2, eye, t1
    if t1==1:
        pw2.config(show= '')
        eye.config(image=hide)
        t1=0
    elif t1==0:
        pw2.config(show='*')
        eye.config(image=see)
        t1=1

#page swap definitions
def admin_login():
    LA.tkraise()
def player_login():
    LP.tkraise()

#Frames
L1=tb.Frame(root)
LA=tb.Frame(root)
LP=tb.Frame(root)

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

#font
f_helvetica = Font(family="Helvetica",size=20,weight="bold",slant="italic",underline=0,overstrike=0)
f_times = Font(family="Times New Roman",size=20,weight="bold",slant="roman",underline=0,overstrike=0)
f_arial = Font(family="Arial",size=20,weight="bold",slant="roman",underline=0,overstrike=0)
f_verdana = Font(family="Verdana",size=20,weight="bold",slant="roman",underline=0,overstrike=0)
f_sans = Font(family="Comic Sans MS",size=20,weight="bold",slant="roman",underline=0,overstrike=0)
f_trebuchet = Font(family="Trebuchet MS",size=20,weight="bold",slant="roman",underline=0,overstrike=0)
f_georgia = Font(family="Georgia",size=20,weight="bold",slant="roman",underline=0,overstrike=0)


#L1 items
L1_1=tb.Frame(L1)
L1_title=tb.Label(L1, text='ESPORTS MANAGEMENT SYSTEM',bootstyle="danger",font=f_georgia,relief="groove", padding=5)
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

#LA items
LA_1=tb.Frame(LA)
LA_2=tb.Frame(LA)
LA_title=tb.Label(LA, text='ADMIN LOGIN', font=('Times bold', 20), padding=5)
LA_title1=tb.Label(LA, text='Enter Username and Password', font=('Times bold', 15))
LA_back=tb.Button(LA, text='Back', command=logout)
us1=tb.Label(LA_1, text='Username')
pw1=tb.Label(LA_2, text='Password')
us2=tb.Entry(LA_1)
pw2=tb.Entry(LA_2, show='*')
eye=tb.Button(LA_2, image=see, command=eye_toggle)

us1.pack(side='left')
us2.pack(side='left')
pw1.pack(side='left')
pw2.pack(side='left')
eye.pack(side='left')
LA_title.pack(pady=20)
LA_title1.pack(pady=(20,20))
LA_1.pack()
LA_2.pack()
LA_back.pack()

#LP items
LP_back=tb.Button(LP, text='Back', command=logout)

LP_back.pack()

#Main frames set up
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frames=[L1,LA,LP]
for frame in frames:
    frame.grid(row=0, column=0, sticky="nsew")

logout()

root.mainloop()