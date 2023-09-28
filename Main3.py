from faulthandler import disable
import mysql.connector as mc
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
import hashlib
import logging

#check

#MySQL connection
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
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

search1=Image.open('search.png')
resized_search = search1.resize((16, 16))
isearch=ImageTk.PhotoImage(resized_search)

send1=Image.open('send.png')
resized_send = send1.resize((16, 16))
isend=ImageTk.PhotoImage(resized_send)

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
        display()
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

def messageclear(label):
    label.forget()

def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if s_tag.get() == 'Enter player tag':
       s_tag.delete(0, "end") # delete all the text in the entry
       s_tag.insert(0, '') #Insert blank for user input
       s_tag.config(foreground='')
def on_focusout(event):
    if s_tag.get() == '':
        s_tag.insert(0, 'Enter player tag')
        s_tag.config(foreground='grey')

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

player_details=[]

def plogin(username, password):
    global player_details
    q=f"select * from information where Player_ID = '{username}' and Password= {password}"
    cur.execute(q)
    player_details=cur.fetchall()
    if player_details==[]:
        return False
    else:
        return True

def display():
    global player_details
    outputframe.forget()
    for entry in [MP_ope1,MP_ope2,MP_ope3,MP_ope4,MP_ope5,MP_ope6,MP_ope7]:
        entry.config(state='normal')
        entry.delete(1.0, 'end')
    for row in player_details:
        MP_ope1.insert(1.0, str(row[0]) )
        MP_ope2.insert(1.0, str(row[1]) )
        MP_ope3.insert(1.0, str(row[2]) )
        MP_ope4.insert(1.0, str(row[3]) )
        MP_ope5.insert(1.0, str(row[4]) )
        MP_ope6.insert(1.0, str(row[5]) )
        MP_ope7.insert(1.0, str(row[6]) )
    for entry in [MP_ope1,MP_ope2,MP_ope3,MP_ope4,MP_ope5,MP_ope6,MP_ope7]:
        entry.config(state='disabled')
    outputframe.pack()
def player_login():
    global player_details
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
    ppassword=pe1.get()
    q4=f"insert into information values({tag},'{id}','{role}',{score},'{name}','{region}',{rank},{ppassword})"
    try:
        cur.execute(q4)
        success4.pack()
        root.after(2000, messageclear, success4)
    except:
        fail4.pack()
        root.after(2000, messageclear, fail4)

def addum():
    name=ume1.get()
    date=ume2.get()
    team=ume3.get()
    prize=ume4.get()
    q5=f"insert into schedule values('{name}','{date}','{team}',{prize})"
    try:
        cur.execute(q5)
        success5.pack()
        root.after(2000, messageclear, success5)
    except:
        fail5.pack()
        root.after(2000, messageclear, fail5)

def search():
    outputframe7.forget()
    for entry in [ope1,ope2,ope3,ope4,ope5,ope6,ope7]:
        entry.config(state='normal')
        entry.delete(1.0, 'end')
    tag=s_tag.get()
    try:
        x=int(tag)
        q_5 = f"Select * from information where Tag = '{tag}'"
        cur.execute(q_5)
        records = cur.fetchall()
        if records == []:
            fail7_1.pack()
            root.after(2000, messageclear, fail7_1)
        for row in records:
            ope1.insert(1.0, str(row[0]) )
            ope2.insert(1.0, str(row[1]) )
            ope3.insert(1.0, str(row[2]) )
            ope4.insert(1.0, str(row[3]) )
            ope5.insert(1.0, str(row[4]) )
            ope6.insert(1.0, str(row[5]) )
            ope7.insert(1.0, str(row[6]) )
            outputframe7.pack()
    except:
        fail7_2.pack()
        root.after(2000, messageclear, fail7_2)
    for entry in [ope1,ope2,ope3,ope4,ope5,ope6,ope7]:
        entry.config(state='disabled')

#(edit team definitions)
swapchoice2=0
def nope():
    pass
def aa():
    f6_1_1_1.pack()
    b6_1.config(state='disabled')
    b6_2.config(command=nope)
def ab1():
    xTag=e6_1.get()
    yTag=e6_2.get()
    if xTag and yTag:
        try:
            cur.execute(f'select * from team1 where Tag = {xTag}')
            for i in cur:
                xID= i[1]
                xRole= i[2]
                xScore= i[3]
            cur.execute(f'select * from team2 where Tag = {yTag}')
            for j in cur:
                yID= j[1]
                yRole= j[2]
                yScore= j[3]
            q1 = f"Update team1 set Tag={yTag},Player_ID='{yID}',Role='{yRole}',Player_Score={yScore} where Tag = {xTag}"
            q2 = f"Update team2 set Tag={xTag},Player_ID='{xID}',Role='{xRole}',Player_Score={xScore} where Tag = {yTag}"
            cur.execute(q1)
            cur.execute(q2)
            success6.pack()
            root.after(2000, messageclear, success6)
        except:
            fail6.pack()
            root.after(2000, messageclear, fail6)
    else:
        fail6_1.pack()
        root.after(2000, messageclear, fail6_1)
def ab2():
    if swapchoice2 == 1:
        team='team1'
    elif swapchoice2 == 2:
        team='team2'
    xTag=e6_2a.get()
    zTag=e6_1a.get()
    if xTag and zTag:
        try:
            cur.execute(f"select * from information where Tag = {zTag}")
            for i in cur:
                zID= i[1]
                zRole= i[2]
                zScore= i[3]

            q1 = f"Update {team} set Tag={zTag},Player_ID='{zID}',Role='{zRole}',Player_Score={zScore} where Tag = {xTag}"
            cur.execute(q1)
            success6.pack()
            root.after(2000, messageclear, success6)
        except:
            fail6.pack()
            root.after(2000, messageclear, fail6)   
    else:
        fail6_1.pack()
        root.after(2000, messageclear, fail6_1)    
def ac():
    f6_1_2.pack()
    b6_2.config(state='disabled')
    b6_1.config(command=nope)
def ad1():
    global swapchoice2
    f6_1_2_1.pack()
    b6_2_1.config(state='disabled')
    b6_2_2.config(command=nope)
    swapchoice2=1
def ad2():
    global swapchoice2
    f6_1_2_1.pack()
    b6_2_2.config(state='disabled')
    b6_2_1.config(command=nope)
    swapchoice2=2
def reset6():
    e6_1.delete(0, 'end')
    e6_2.delete(0, 'end')
    e6_1a.delete(0, 'end')
    e6_2a.delete(0, 'end')
    b6_1.config(state='normal', command=aa)
    b6_2.config(state='normal', command=ac)
    b6_2_1.config(state='normal', command=ad1)
    b6_2_2.config(state='normal', command=ad2)
    f6_1_1_1.forget()
    f6_1_1.forget()
    f6_1_2_1.forget()
    f6_1_2.forget()
#(Edit team definitions end)

#(Update details definition)
col_choice=''
col_available=['Tag', 'Player_ID', 'Player_Name', 'Player_Score', 'Region', 'Regional_Rank']
tag_stored=''
def get_ctu(clicked):
    global col_choice
    index=clicked - 1
    buttonlist[index].config(state='disabled')
    for button in buttonlist:
        button.config(command=nope)
    col_choice=clicked
    entryframe8_1.pack()
    pass
def submit8_1():
    global tag_stored
    tag_stored=tag_entry.get()
    try:
        x=int(tag_stored)
        q_temp=f"select * from information where tag={tag_stored}"
        cur.execute(q_temp)
        record_temp=cur.fetchall()
        if record_temp==[]:
            fail8_2.pack()
            root.after(1000, messageclear, fail8_2)
        else:
            entryframe8_2.pack()
            tag_entry.config(state='disabled')
    except:
        fail8_1.pack()
        root.after(1000, messageclear, fail8_1)
def submit8_2():
    global col_choice, col_available, tag_stored
    col=col_available[col_choice - 1]
    row=tag_stored
    up=up_entry.get()
    try:
        if col == "Player_Score" or col == "Regional_Rank":
            q_8 = f"Update information set {col} = {up} where tag = {row}"
            cur.execute(q_8)
        elif col == "Player_ID" or col == "Player_Name" or col == "Region":
            q_8 = f"Update information set {col} = '{up}' where tag = {row}"
            cur.execute(q_8)
        elif col == "Tag":
            q_8 = f"Update information set {col} = {up} where tag = {row}"
            q_8_1 = f"Update information set password = {up} where tag = {row}"
            cur.execute(q_8)
            cur.execute(q_8_1)
        up_entry.config(state='disabled')
        success8.pack()
        root.after(1000, messageclear, success8)
    except:
        fail8_3.pack()
        root.after(1000, messageclear, fail8_3)
def reset8():
    c_1.config(state='normal', command=lambda: get_ctu(1))
    c_2.config(state='normal', command=lambda: get_ctu(2))
    c_3.config(state='normal', command=lambda: get_ctu(3))
    c_4.config(state='normal', command=lambda: get_ctu(4))
    c_5.config(state='normal', command=lambda: get_ctu(5))
    c_6.config(state='normal', command=lambda: get_ctu(6))
    tag_entry.config(state='normal')
    tag_entry.delete(0, 'end')
    up_entry.delete(0, 'end')
    entryframe8_2.forget()
    entryframe8_1.forget()
#(Update details definition end)

def remove():
    rem=tag_entry9.get()
    try:
        x=int(rem)
        l = []
        l1=[]
        l2=[]
        q_9_1= f"select tag from information where tag = {rem}"
        cur.execute(q_9_1)
        for i in cur:
            l.append(i[0])
        if l==[]:
            fail9_2.pack()
            root.after(1000, messageclear, fail9_2)
        else:
            q_9_2_1 = f"select tag from team1 where tag = {rem}"
            q_9_2_2 = f"select tag from team2 where tag = {rem}"
            cur.execute(q_9_2_1)
            for j in cur:
                l1.append(j[0])
            cur.execute(q_9_2_2)
            for j in cur:
                l2.append(j[0])
            if l == l1 or l == l2:
                fail9_3.pack()
                root.after(1000, messageclear, fail9_3)
            else:
                q_7 = f"delete from information where tag = {rem}"
                cur.execute(q_7)
                success9.pack()
                root.after(1000, messageclear, success9)
    except:    
        fail9_1.pack()
        root.after(1000, messageclear, fail9_1)


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
load1=tb.Label(LA1)


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

#LP1 items
load2=tb.Label(LP1)

#MP items
MP_title=tb.Label(MP, text= 'Welcome')
outputframe=tb.Frame(MP)

MP_ope1=tb.Text(outputframe, height=1, width=20, state='disabled')
MP_ope2=tb.Text(outputframe, height=1, width=20, state='disabled')
MP_ope3=tb.Text(outputframe, height=1, width=20, state='disabled')
MP_ope4=tb.Text(outputframe, height=1, width=20, state='disabled')
MP_ope5=tb.Text(outputframe, height=1, width=20, state='disabled')
MP_ope6=tb.Text(outputframe, height=1, width=20, state='disabled')
MP_ope7=tb.Text(outputframe, height=1, width=20, state='disabled')
MP_opl1=tb.Label(outputframe, text='Tag')
MP_opl2=tb.Label(outputframe, text='Player ID')
MP_opl3=tb.Label(outputframe, text='Role')
MP_opl4=tb.Label(outputframe, text='Score')
MP_opl5=tb.Label(outputframe, text='Name')
MP_opl6=tb.Label(outputframe, text='Region')
MP_opl7=tb.Label(outputframe, text='Regional rank')

MP_logout=tb.Button(MP, text='LOGOUT', command=logout)

MP_ope1.grid(row= 0, column= 1)
MP_ope2.grid(row= 1, column= 1)
MP_ope3.grid(row= 2, column= 1)
MP_ope4.grid(row= 3, column= 1)
MP_ope5.grid(row= 4, column= 1)
MP_ope6.grid(row= 5, column= 1)
MP_ope7.grid(row= 6, column= 1)
MP_opl1.grid(row= 0, column= 0)
MP_opl2.grid(row= 1, column= 0)
MP_opl3.grid(row= 2, column= 0)
MP_opl4.grid(row= 3, column= 0)
MP_opl5.grid(row= 4, column= 0)
MP_opl6.grid(row= 5, column= 0)
MP_opl7.grid(row= 6, column= 0)

MP_title.pack()
outputframe.pack()
MP_logout.pack(side='bottom')


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
pl1=tb.Label(entryframe4, text='Tag')
pl2=tb.Label(entryframe4, text='Player ID')
pl3=tb.Label(entryframe4, text='Role')
pl4=tb.Label(entryframe4, text='Score')
pl5=tb.Label(entryframe4, text='Name')
pl6=tb.Label(entryframe4, text='Region')
pl7=tb.Label(entryframe4, text='Regional rank')
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
pl1.grid(row= 0, column= 0)
pl2.grid(row= 1, column= 0)
pl3.grid(row= 2, column= 0)
pl4.grid(row= 3, column= 0)
pl5.grid(row= 4, column= 0)
pl6.grid(row= 5, column= 0)
pl7.grid(row= 6, column= 0)

entryframe4.pack()
submit4.pack()
mainmenu9.pack(side='bottom')

#f5 items
entryframe5=tb.Frame(f5)
f5_title=tb.Label(f5, text='Add Upcoming Matches', font=('Times bold', 12), relief='groove', padding=2)
f5_title1=tb.Label(f5, text='Input Details')
ume1=tb.Entry(entryframe5)
ume2=tb.Entry(entryframe5)
ume3=tb.Entry(entryframe5)
ume4=tb.Entry(entryframe5)
uml1=tb.Label(entryframe5, text='League')
uml2=tb.Label(entryframe5, text='Date')
uml3=tb.Label(entryframe5, text='Participants')
uml4=tb.Label(entryframe5, text='Price')

submit5=tb.Button(f5, text='Submit', command=addum)
success5=tb.Label(f5, text='Added succesfully')
fail5=tb.Label(f5, text='Unsuccesful')
mainmenu9=tb.Button(f5, text='Main Menu', command=mainmenu)


f5_title.pack()
f5_title1.pack()

ume1.grid(row= 0, column= 1)
ume2.grid(row= 1, column= 1)
ume3.grid(row= 2, column= 1)
ume4.grid(row= 3, column= 1)
uml1.grid(row= 0, column= 0)
uml2.grid(row= 1, column= 0)
uml3.grid(row= 2, column= 0)
uml4.grid(row= 3, column= 0)

entryframe5.pack()
submit5.pack()
mainmenu9.pack(side='bottom')

#f6 items
f6_1=tb.Frame(f6)
f6_1_1=tb.Frame(f6)
f6_1_1_1=tb.Frame(f6)
f6_1_1_1a=tb.Frame(f6_1_1_1)
f6_1_1_1b=tb.Frame(f6_1_1_1)
f6_1_2=tb.Frame(f6)
f6_1_2_1=tb.Frame(f6)
f6_1_2_1a=tb.Frame(f6_1_2_1)
f6_1_2_1b=tb.Frame(f6_1_2_1)

b6_1=tb.Button(f6_1, text='Between Teams', command=aa)
b6_2=tb.Button(f6_1, text='From Reserve to Teams', command=ac)
l6_1=tb.Label(f6_1_1_1a,text="Enter Tag of player to swap from Team 1")
l6_2=tb.Label(f6_1_1_1b,text="Enter Tag of player to swap from Team 2")
e6_1=tb.Entry(f6_1_1_1a)
e6_2=tb.Entry(f6_1_1_1b)
submit6_1=tb.Button(f6_1_1_1, text='SUBMIT', command=ab1)
b6_2_1=tb.Button(f6_1_2, text='To Team1', command=ad1)
b6_2_2=tb.Button(f6_1_2, text='To Team2', command=ad2)
l6_1a=tb.Label(f6_1_2_1a,text="Enter Tag of player from reserve")
l6_2a=tb.Label(f6_1_2_1b,text="Enter Tag of player in team")
e6_1a=tb.Entry(f6_1_2_1a)
e6_2a=tb.Entry(f6_1_2_1b)
submit6_1a=tb.Button(f6_1_2_1,  text='SUBMIT', command=ab2)

f6_title=tb.Label(f6, text='Swap Players', font=('Times bold', 12), relief='groove', padding=2)
success6=tb.Label(f6, text='Swap succesful!!')
fail6=tb.Label(f6, text='Swap unsuccesful...')
fail6_1=tb.Label(f6, text='Fill in both')
b_reset6=tb.Button(f6, text='Reset selection', command=reset6)
mainmenu9=tb.Button(f6, text='Main Menu', command=mainmenu)

b6_1.pack(side='left')
b6_2.pack(side='left')
l6_1.pack(side='left')
e6_1.pack(side='left')
f6_1_1_1a.pack(side='left')
l6_2.pack(side='left')
e6_2.pack(side='left')
f6_1_1_1b.pack(side='left')
submit6_1.pack()
b6_2_1.pack(side='left')
b6_2_2.pack(side='left')
l6_1a.pack(side='left')
e6_1a.pack(side='left')
f6_1_2_1a.pack(side='left')
l6_2a.pack(side='left')
e6_2a.pack(side='left')
f6_1_2_1b.pack(side='left')
submit6_1a.pack()

f6_title.pack()
f6_1.pack()
mainmenu9.pack(side='bottom')
b_reset6.pack(side='bottom')

#f7 items
outputframe7=tb.Frame(f7)
searchbar=tb.Frame(f7)
f7_title=tb.Label(f7, text='Search Players', font=('Times bold', 12), relief='groove', padding=2)
s_tag=tb.Entry(searchbar)
s_tag.insert(0, 'Enter player tag')
s_tag.config(foreground='grey')
s_tag.bind('<FocusIn>', on_entry_click)
s_tag.bind('<FocusOut>', on_focusout)

ope1=tb.Text(outputframe7, height=1, width=20, state='disabled')
ope2=tb.Text(outputframe7, height=1, width=20, state='disabled')
ope3=tb.Text(outputframe7, height=1, width=20, state='disabled')
ope4=tb.Text(outputframe7, height=1, width=20, state='disabled')
ope5=tb.Text(outputframe7, height=1, width=20, state='disabled')
ope6=tb.Text(outputframe7, height=1, width=20, state='disabled')
ope7=tb.Text(outputframe7, height=1, width=20, state='disabled')
opl1=tb.Label(outputframe7, text='Tag')
opl2=tb.Label(outputframe7, text='Player ID')
opl3=tb.Label(outputframe7, text='Role')
opl4=tb.Label(outputframe7, text='Score')
opl5=tb.Label(outputframe7, text='Name')
opl6=tb.Label(outputframe7, text='Region')
opl7=tb.Label(outputframe7, text='Regional rank')

fail7_1=tb.Label(f7, text='Player not found')
fail7_2=tb.Label(f7, text='Invalid tag')
s_button=tb.Button(searchbar, image=isearch, command=search)
mainmenu9=tb.Button(f7, text='Main Menu', command=mainmenu)

ope1.grid(row= 0, column= 1)
ope2.grid(row= 1, column= 1)
ope3.grid(row= 2, column= 1)
ope4.grid(row= 3, column= 1)
ope5.grid(row= 4, column= 1)
ope6.grid(row= 5, column= 1)
ope7.grid(row= 6, column= 1)
opl1.grid(row= 0, column= 0)
opl2.grid(row= 1, column= 0)
opl3.grid(row= 2, column= 0)
opl4.grid(row= 3, column= 0)
opl5.grid(row= 4, column= 0)
opl6.grid(row= 5, column= 0)
opl7.grid(row= 6, column= 0)

f7_title.pack()
s_tag.pack(side='left')
s_button.pack(side='left')
searchbar.pack()
mainmenu9.pack(side='bottom')

#f8 items
buttonframe=tb.Frame(f8)
entryframe8_1=tb.Frame(f8)
entryframe8_2=tb.Frame(f8)
f8_title=tb.Label(f8, text='Update player details', font=('Times bold', 12), relief='groove', padding=2)
f8_title1=tb.Label(f8, text='select coloumn to update')

c_1=tb.Button(buttonframe, text='Tag', command=lambda: get_ctu(1))
c_2=tb.Button(buttonframe, text='Player ID', command=lambda: get_ctu(2))
c_3=tb.Button(buttonframe, text='Player Name', command=lambda: get_ctu(3))
c_4=tb.Button(buttonframe, text='Score', command=lambda: get_ctu(4))
c_5=tb.Button(buttonframe, text='Region', command=lambda: get_ctu(5))
c_6=tb.Button(buttonframe, text='Regional Rank', command=lambda: get_ctu(6))
buttonlist=[c_1,c_2,c_3,c_4,c_5,c_6]
tag_label=tb.Label(entryframe8_1, text='Enter tag of player')
tag_entry=tb.Entry(entryframe8_1)
tag_submit=tb.Button(entryframe8_1, image=isend, command=submit8_1)
up_label=tb.Label(entryframe8_2, text='Enter new detail')
up_entry=tb.Entry(entryframe8_2)
up_submit=tb.Button(entryframe8_2, image=isend, command=submit8_2)
fail8_1=tb.Label(f8, text='Invalid tag')
fail8_2=tb.Label(f8, text='No player found')
fail8_3=tb.Label(f8, text='Error. Try again')
success8=tb.Label(f8, text='Update successful')
b_reset8=tb.Button(f8, text='Reset selection', command=reset8)
mainmenu9=tb.Button(f8, text='Main Menu', command=mainmenu)

c_1.grid(row= 0,column= 0)
c_2.grid(row= 0,column= 1)
c_3.grid(row= 0,column= 2)
c_4.grid(row= 1,column= 0)
c_5.grid(row= 1,column= 1)
c_6.grid(row= 1,column= 2)

tag_label.pack(side='left')
tag_entry.pack(side='left')
tag_submit.pack(side='left')
up_label.pack(side='left')
up_entry.pack(side='left')
up_submit.pack(side='left')
f8_title.pack()
f8_title1.pack()
buttonframe.pack()
mainmenu9.pack(side='bottom')
b_reset8.pack(side='bottom')

#f9 items
entryframe9=tb.Frame(f9)
f9_title=tb.Label(f9, text='Remove player', font=('Times bold', 12), relief='groove', padding=2)
f9_title1=tb.Label(f9, text='Note- Players playing for either teams cannot be removed.')
mainmenu9=tb.Button(f9, text='Main Menu', command=mainmenu)
tag_label9=tb.Label(entryframe9, text='Enter tag of player to be removed')
tag_entry9=tb.Entry(entryframe9)
fail9_1=tb.Label(f9, text='Invalid tag')
fail9_2=tb.Label(f9, text='Player not found')
fail9_3=tb.Label(f9, text="Can't execute command because player already exist in a team")
success9=tb.Label(f9, text='Player removed successfully')
tag_submit9=tb.Button(entryframe9, image=isend, command=remove)

tag_label9.pack(side='left')
tag_entry9.pack(side='left')
tag_submit9.pack(side='left')
f9_title.pack()
f9_title1.pack()
entryframe9.pack()
mainmenu9.pack(side='bottom')

#Main frames set up
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frames=[L1,LA,LP,LA1,LP1,MP,M1,f1,f2,f3,f4,f5,f6,f7,f8,f9]
for frame in frames:
    frame.grid(row=0, column=0, sticky="nsew")

logout()
root.mainloop()