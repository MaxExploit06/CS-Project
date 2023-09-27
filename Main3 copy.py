import mysql.connector as mc
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
import hashlib
import logging
import time

#check

#MySQL connection
mydb = mc.connect(host="localhost",user="root",password="bruh",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True


#root
root=tb.Window()
root.title('eSports Management System')
root.iconbitmap('EMS.ico')
root.geometry('960x540')
tb.Style(theme="cyborg") ; t=0
colors=root.style.colors

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

def update_gif(canvas, img, frame_index):
    canvas.itemconfig(bg_img, image=img[frame_index])
    if frame_index==56:
        M1.tkraise()
    else:
        root.after(30, update_gif, canvas, img, (frame_index + 1) % len(img))

def update_gif2(canvas, img, frame_index):
    canvas.itemconfig(bg_img, image=img[frame_index])
    if frame_index==56:
        MP.tkraise()
    else:
        root.after(30, update_gif2, canvas, img, (frame_index + 1) % len(img))

def gif():
    LA1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = "loading.gif"
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

    # Create a Canvas widget to display the GIF background
    canvas = tb.Canvas(LA1, width=800, height=600)
    LA1.grid_rowconfigure(0, weight=1)
    LA1.grid_columnconfigure(0, weight=1)
    canvas.grid(row=0,column=0, sticky="nsew")

    # Create a background image on the Canvas
    bg_img = canvas.create_image(0, 0, anchor=tb.NW, image=frames[0])

    # Start the animation loop
    update_gif(canvas, frames, 0)
    
    # Add other widgets and functionality here

def gif2():
    LP1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = "loading.gif"
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

    # Create a Canvas widget to display the GIF background
    canvas = tb.Canvas(LP1, width=800, height=600)
    LP1.grid_rowconfigure(0, weight=1)
    LP1.grid_columnconfigure(0, weight=1)
    canvas.grid(row=0,column=0, sticky="nsew")

    # Create a background image on the Canvas
    bg_img = canvas.create_image(0, 0, anchor=tb.NW, image=frames[0])

    # Start the animation loop
    update_gif2(canvas, frames, 0)
    
    # Add other widgets and functionality here
    

t1=1 ; t2=1

#other definitions
def themeswap():
    global t
    if t==0:
        tb.Style(theme="cosmo")
        themebutton.config(bootstyle='dark, toolbutton, outline')
        t=1
    elif t==1:
        tb.Style(theme="cyborg")
        themebutton.config(bootstyle='light, toolbutton, outline')
        t=0

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

logging.basicConfig(filename='login_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_login_attempt(username, success=True):
    status = "success" if success else "failed"
    logging.info(f"Login attempt: User '{username}' - {status}")

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

'''def register_user(username, password):
    with open('user_accounts.txt', 'a') as file:
        file.write(f"{username}:{hash_password(password)}\n")'''

def login(username, password):
    with open('user_accounts.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and hash_password(password) == stored_password:
                log_login_attempt(username)
                return True
    log_login_attempt(username, success=False)
    return False

def admin_login():
    global Aus2, Apw2
    username=Aus2.get()
    Aus2.delete(0, END)
    password=Apw2.get()
    Apw2.delete(0, END)
    if username and password:
        if login(username, password):
            LA1.tkraise()
            gif()
        else:
            LA_title1.config(text="Login failed")
    else:
        LA_title1.config(text="Please enter both username and password")

def plogin(username, password):
    q=f"select * from information where Player_ID = '{username}' and Password= {password}"
    cur.execute(q)
    record=cur.fetchall
    if record==[]:
        return False
    else:
        return True

def player_login():
    global Pus2, Ppw2
    username=Pus2.get()
    Aus2.delete(0, END)
    password=Ppw2.get()
    Apw2.delete(0, END)
    try:
        x=int(password)
        if username and password:
           if plogin(username, password):
            LP1.tkraise()
            gif2()
           else:
            LP_title1.config(text="Login failed")
        else:
            LP_title1.config(text="Please enter both username and password")
    except:
        LP_title1.config(text="invalid password")
    


#page swap definitions
def admin_login_swap():
    LA.tkraise()
def player_login_swap():
    LP.tkraise()

def mainmenu():
    M1.tkraise()
def f1_swap():
    f1.tkraise()
def f2_swap():
    f2.tkraise()
def f3_swap():
    f3.tkraise()
def f4_swap():
    f4.tkraise()
def f5_swap():
    f5.tkraise()
def f6_swap():
    f6.tkraise()
    w=f6.winfo_reqwidth()
def f7_swap():
    f7.tkraise()
def f8_swap():
    f8.tkraise()
    w=f8.winfo_reqwidth()
def f9_swap():
    f9.tkraise()

#sql connectivity functions
um_content=''
def um(team):
    global um_content, area
    area.config(state='normal')
    um_content=''
    if team==1:
        q_1="select * from schedule where Participant='team1'"
    elif team==2:
        q_1="select * from schedule where Participant='team2'"
    cur.execute(q_1)
    records = cur.fetchall()
    for row in records:
        um_content+=f'League: {row[0]} \n Date: {row[1]} \n Participant: {row[2]} \n Price: {row[3]} $ \n\n'
    area.delete("1.0", END)
    area.insert("1.0", um_content)
    area.config(state='disable')

rowdata=[]
def dt(team):
    table2.delete_rows()
    global rowdata
    area2.forget()
    table2.pack()
    if team==1:
        team='team1'
    elif team==2:
        team='team2'
    cur.execute(f"select * from {team}")
    records = cur.fetchall()
    for row in records:
        table2.insert_row('end', row)
    table2.load_table_data()

score=''
scoremessage=StringVar()
scoremessage.set('')
def team_score(team):
    global score, scoremessage
    if team==1:
        team='team1'
    elif team==2:
        team='team2'
    q_2=f'select sum(Player_Score) from {team}'
    cur.execute(q_2)
    for i in cur:
        score = i[0]
    scoremessage.set(f'The team score is {score}')

def addplayer():

    tag=pe1.get()
    id=pe2.get()
    role=pe3.get()
    score=pe4.get()
    name=pe5.get()
    region=pe6.get()
    rank=pe7.get()
    ppassword=pe8.get()
    q4=f"insert into information values({tag},'{id}','{role}',{score},'{name}','{region}',{rank},{ppassword})"
    try:
        cur.execute(q4)
        success4.pack()
        '''time.sleep(2)
        success4.forget()'''
    except:
        fail4.pack()
        '''time.sleep(2)
        fail4.forget()'''
        


#Frames
L1=tb.Frame(root)
LA=tb.Frame(root)
LP=tb.Frame(root)
LA1=tb.Frame(root)
LP1=tb.Frame(root) #mid login player
MP=tb.Frame(root) #post login player

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
b_admin=tb.Button(L1_1, text='ADMIN', image=admin, command=admin_login_swap)
b_player=tb.Button(L1_1, text='PLAYER', image=player, command=player_login_swap)


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


#LP items
LP_1=tb.Frame(LP)
LP_2=tb.Frame(LP)
LP_title=tb.Label(LP, text='PLAYER LOGIN', font=('Times bold', 20), padding=5)
LP_title1=tb.Label(LP, text='Enter Username and Password', font=('Times bold', 15))
LP_back=tb.Button(LP, text='Back', command=logout)
Pus1=tb.Label(LP_1, text='Username')
Ppw1=tb.Label(LP_2, text='Password')
Pus2=tb.Entry(LP_1)
Ppw2=tb.Entry(LP_2, show='*')
Peye=tb.Button(LP_2, image=see, command=p_eye_toggle)
submit2=tb.Button(LP, text='Submit', command=player_login)

Pus1.pack(side='left')
Pus2.pack(side='left')
Ppw1.pack(side='left')
Ppw2.pack(side='left')
Peye.pack(side='left')
LP_title.pack(pady=20)
LP_title1.pack(pady=(20,20))
LP_1.pack()
LP_2.pack()
submit2.pack()
LP_back.pack()

#M1 items
M1_1=tb.Frame(M1)
M1_2=tb.Frame(M1)
M1_3=tb.Frame(M1)

b1=Button(M1_1, text='Display upcoming matches', padx=1.5, pady=5, command=f1_swap)
b2=Button(M1_1, text='Display team', padx=40, pady=5, command=f2_swap)
b3=Button(M1_1, text='Display team score', padx=25, pady=5, command=f3_swap)
b4=Button(M1_2, text='Add player', padx=45, pady=5, command=f4_swap)
b5=Button(M1_2, text='Add upcoming match', padx=16, pady=5, command=f5_swap)
b6=Button(M1_2, text='Edit team', padx=49.5, pady=5, command=f6_swap)
b7=Button(M1_3, text='Search player', padx=39, pady=5, command=f7_swap)
b8=Button(M1_3, text='Update player details', padx=20, pady=5, command=f8_swap)
b9=Button(M1_3, text='Remove player', padx=36, pady=5, command=f9_swap)
swap_val= IntVar()
themebutton=tb.Checkbutton(M1, bootstyle="light,toolbutton,outline",text="Switch Theme",variable=swap_val,onvalue=1,offvalue=0, command=themeswap)

M1_title=tb.Label(M1, text='ESPORTS MANAGEMENT SYSTEM', font=('Times bold', 25), relief='groove', padding=5)

b1.pack(side='left')
b2.pack(side='left')
b3.pack(side='left')
b4.pack(side='left')
b5.pack(side='left')
b6.pack(side='left')
b7.pack(side='left')
b8.pack(side='left')
b9.pack(side='left')
M1_title.pack()
M1_1.pack()
M1_2.pack()
M1_3.pack()
themebutton.pack()

#f1 items
f1_title=tb.Label(f1, text='Upcoming Matches', font=('Times bold', 12), relief='groove', padding=2)
f1_title1=tb.Label(f1, text='Select a team to view their upcoming matches')
f1_1=tb.Frame(f1)
team1=tb.Button(f1_1, text='Team 1', command=lambda: um(1))
team2=tb.Button(f1_1, text='Team 2', command=lambda: um(2))
area=tb.Text(f1, height= 15, width= 52, relief='sunken', state='disable')
mainmenu9=tb.Button(f1, text='Main Menu', command=mainmenu)

f1_title.pack()
f1_title1.pack()
team1.pack(side='left')
team2.pack(side='left')
f1_1.pack()
area.pack()
mainmenu9.pack()

#f2 items
f2_title=tb.Label(f2, text='Display Team', font=('Times bold', 12), relief='groove', padding=2)
f2_title1=tb.Label(f2, text='Select a team to view members')
f2_1=tb.Frame(f2)
dteam1=tb.Button(f2_1, text='Team 1', command=lambda: dt(1))
dteam2=tb.Button(f2_1, text='Team 2', command=lambda: dt(2))
area2=tb.Text(f2, height= 15, width= 52, relief='sunken', state='disable')

coldata=[{'text':'Tag', "stretch": False}, {'text':'Player ID', "stretch": False}, {'text':'Role', "stretch": False}, {'text':'Score', "stretch": False} ]

table2=Tableview(
    master=f2,
    coldata=coldata,
    rowdata=rowdata,
    paginated=False,
    searchable=False,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
    height=4,
)
mainmenu9=tb.Button(f2, text='Main Menu', command=mainmenu)

f2_title.pack()
f2_title1.pack()
dteam1.pack(side='left')
dteam2.pack(side='left')
f2_1.pack()
area2.pack()
mainmenu9.pack(side='bottom')

#f3 items
f3_title=tb.Label(f3, text='Display Team Score', font=('Times bold', 12), relief='groove', padding=2)
f3_title1=tb.Label(f3, text='Select a team to view team score')
f3_1=tb.Frame(f3)
steam1=tb.Button(f3_1, text='Team 1', command=lambda: team_score(1))
steam2=tb.Button(f3_1, text='Team 2', command=lambda: team_score(2))
mainmenu9=tb.Button(f3, text='Main Menu', command=mainmenu)
scorelabel=tb.Label(f3, textvariable=scoremessage)

f3_title.pack()
f3_title1.pack()
steam1.pack(side='left')
steam2.pack(side='left')
f3_1.pack()
scorelabel.pack()
mainmenu9.pack(side='bottom')

#f4 items
entryframe4=tb.Frame(f4)
f4_title=tb.Label(f4, text='Add Player', font=('Times bold', 12), relief='groove', padding=2)
f4_title1=tb.Label(f4, text='Input Details')
pe1=tb.Entry(entryframe4)
pe2=tb.Entry(entryframe4)
pe3=tb.Entry(entryframe4)
pe4=tb.Entry(entryframe4)
pe5=tb.Entry(entryframe4)
pe6=tb.Entry(entryframe4)
pe7=tb.Entry(entryframe4)
pe8=tb.Entry(entryframe4)
pl1=tb.Label(entryframe4, text='Tag')
pl2=tb.Label(entryframe4, text='Player ID')
pl3=tb.Label(entryframe4, text='Role')
pl4=tb.Label(entryframe4, text='Score')
pl5=tb.Label(entryframe4, text='Name')
pl6=tb.Label(entryframe4, text='Region')
pl7=tb.Label(entryframe4, text='Regional rank')
pl8=tb.Label(entryframe4, text='Set password')
submit4=tb.Button(f4, text='Submit', command=addplayer)
success4=tb.Label(f4, text='Added succesfully')
fail4=tb.Label(f4, text='Unsuccesful')
mainmenu9=tb.Button(f4, text='Main Menu', command=mainmenu)


f4_title.pack()
f4_title1.pack()

pe1.grid(row= 0, column= 1)
pe2.grid(row= 1, column= 1)
pe3.grid(row= 2, column= 1)
pe4.grid(row= 3, column= 1)
pe5.grid(row= 4, column= 1)
pe6.grid(row= 5, column= 1)
pe7.grid(row= 6, column= 1)
pe8.grid(row= 7, column= 1)
pl1.grid(row= 0, column= 0)
pl2.grid(row= 1, column= 0)
pl3.grid(row= 2, column= 0)
pl4.grid(row= 3, column= 0)
pl5.grid(row= 4, column= 0)
pl6.grid(row= 5, column= 0)
pl7.grid(row= 6, column= 0)
pl8.grid(row= 7, column= 0)

entryframe4.pack()
submit4.pack()
mainmenu9.pack(side='bottom')

#f5 items
mainmenu9=tb.Button(f5, text='Main Menu', command=mainmenu)

mainmenu9.pack()

#f6 items
mainmenu9=tb.Button(f6, text='Main Menu', command=mainmenu)

mainmenu9.pack()

#f7 items
mainmenu9=tb.Button(f7, text='Main Menu', command=mainmenu)

mainmenu9.pack()

#f8 items
mainmenu9=tb.Button(f8, text='Main Menu', command=mainmenu)

mainmenu9.pack()

#f9 items
mainmenu9=tb.Button(f9, text='Main Menu', command=mainmenu)

mainmenu9.pack()

#Main frames set up
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frames=[L1,LA,LP,LA1,LP1,M1,f1,f2,f3,f4,f5,f6,f7,f8,f9]
for frame in frames:
    frame.grid(row=0, column=0, sticky="nsew")

logout()
root.mainloop()