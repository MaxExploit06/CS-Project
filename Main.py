import mysql.connector as mc
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk, ImageSequence
import hashlib
import logging
import time

#MySQL connection
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True


#root
root=tb.Window()
root.title('eSports Management System')
root.iconbitmap('EMS.ico')
root.geometry('960x540')
tb.Style(theme="cyborg") ; t=1

#Images
admin1=Image.open('admin.png')
player1=Image.open('player.png')
resized_admin = admin1.resize((200, 200))
resized_player = player1.resize((200, 200))
admin=ImageTk.PhotoImage(resized_admin)
player=ImageTk.PhotoImage(resized_player)

see1=Image.open('see.png')
hide1=Image.open('hide.png')
resized_see = see1.resize((16, 16))
resized_hide = hide1.resize((16, 16))
see=ImageTk.PhotoImage(resized_see)
hide=ImageTk.PhotoImage(resized_hide)

def gif():
    current_frame = loading.tell()
    load.configure(image=frames[current_frame])
    root.after(loading.delay[current_frame], gif)
    try:
        loading.seek(current_frame + 1)
    except EOFError:
        loading.seek(0)

loading = Image.open("loading.gif")
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(loading)]

t1=1 ; t2=1

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

def a_eye_toggle():
    global Apw2, Aeye, t1
    if t1==1:
        Apw2.config(show= '')
        Aeye.config(image=hide)
        t1=0
    elif t1==0:
        Apw2.config(show='*')
        Aeye.config(image=see)
        t1=1

def p_eye_toggle():
    global Ppw2, Peye, t2
    if t2==1:
        Ppw2.config(show= '')
        Peye.config(image=hide)
        t2=0
    elif t2==0:
        Ppw2.config(show='*')
        Peye.config(image=see)
        t2=1



#Account system

# Initialize the logger
logging.basicConfig(filename='login_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_login_attempt(username, success=True):
    status = "success" if success else "failed"
    logging.info(f"Login attempt: User '{username}' - {status}")

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

'''def register_user(username, password):
    with open('user_accounts.txt', 'a') as file:
        file.write(f"{username}:{hash_password(password)}\n")'''

def admin_login():
    global Aus2, Apw2
    username=Aus2.get()
    Aus2.delete(0, END)
    password=Apw2.get()
    Apw2.delete(0, END)
    with open('user_accounts.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and hash_password(password) == stored_password:
                log_login_attempt(username)
                LA1.tkraise()
                gif()
    log_login_attempt(username, success=False)
    return False

#page swap definitions
def admin_login():
    LA.tkraise()
def player_login():
    LP.tkraise()

#Frames
L1=tb.Frame(root)
LA=tb.Frame(root)
LP=tb.Frame(root)
LA1=tb.Frame(root)

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

#LA items
LA_1=tb.Frame(LA)
LA_2=tb.Frame(LA)
LA_title=tb.Label(LA, text='ADMIN LOGIN', font=('Times bold', 20), padding=5)
LA_title1=tb.Label(LA, text='Enter Username and Password', font=('Times bold', 15))
LA_back=tb.Button(LA, text='Back', command=logout)
Aus1=tb.Label(LA_1, text='Username')
Apw1=tb.Label(LA_2, text='Password')
Aus2=tb.Entry(LA_1)
Apw2=tb.Entry(LA_2, show='*')
Aeye=tb.Button(LA_2, image=see, command=a_eye_toggle)
submit1=tb.Button(LA, text='Submit', command=admin_login)

Aus1.pack(side='left')
Aus2.pack(side='left')
Apw1.pack(side='left')
Apw2.pack(side='left')
Aeye.pack(side='left')
LA_title.pack(pady=20)
LA_title1.pack(pady=(20,20))
LA_1.pack()
LA_2.pack()
submit1.pack()
LA_back.pack()

#LA1 items
load=tb.Label(LA1)

load.pack()

#LP items
LP_1=tb.Frame(LP)
LP_2=tb.Frame(LP)
LP_title=tb.Label(LP, text='ADMIN LOGIN', font=('Times bold', 20), padding=5)
LP_title1=tb.Label(LP, text='Enter Username and Password', font=('Times bold', 15))
LP_back=tb.Button(LP, text='Back', command=logout)
Pus1=tb.Label(LP_1, text='Username')
Ppw1=tb.Label(LP_2, text='Password')
Pus2=tb.Entry(LP_1)
Ppw2=tb.Entry(LP_2, show='*')
Peye=tb.Button(LP_2, image=see, command=p_eye_toggle)

Pus1.pack(side='left')
Pus2.pack(side='left')
Ppw1.pack(side='left')
Ppw2.pack(side='left')
Peye.pack(side='left')
LP_title.pack(pady=20)
LP_title1.pack(pady=(20,20))
LP_1.pack()
LP_2.pack()
LP_back.pack()

#Main frames set up
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frames=[L1,LA,LP,LA1]
for frame in frames:
    frame.grid(row=0, column=0, sticky="nsew")

logout()
LA1.tkraise()
gif()

root.mainloop()