import mysql.connector as mc
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence, ImageOps
import hashlib
import logging
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from datetime import date
from tkinter.font import Font

#check

#MySQL connection
mydb = mc.connect(host="localhost",user="root",password="root",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True


#root
root=tb.Window()
root.title('eSports Management System')
root.iconbitmap(os.getcwd()+"\\Graphics\\EMS.ico")
root.geometry('960x540')
tb.Style(theme="cyborg") ; t=0
colors=root.style.colors

#music
pygame.mixer.init()

def click():
    pygame.mixer.music.load(os.getcwd()+"\\Graphics\\click.mp3")
    pygame.mixer.music.play(loops=0)

#Images
admin1=Image.open(os.getcwd()+"\\Graphics\\admin.png")
player1=Image.open(os.getcwd()+"\\Graphics\\player.png")
resized_admin = admin1.resize((200, 200))
resized_player = player1.resize((200, 200))
admin=ImageTk.PhotoImage(resized_admin)
player=ImageTk.PhotoImage(resized_player)

see1=Image.open(os.getcwd()+"\\Graphics\\see.png")
hide1=Image.open(os.getcwd()+"\\Graphics\\hide.png")
resized_see = see1.resize((16, 16))
resized_hide = hide1.resize((16, 16))

search1=Image.open(os.getcwd()+"\\Graphics\\search.png")
resized_search = search1.resize((16, 16))
isearch=ImageTk.PhotoImage(resized_search)
search2=Image.open(os.getcwd()+"\\Graphics\\search_w.png")
resized_search2 = search2.resize((16, 16))
isearch_white=ImageTk.PhotoImage(resized_search2)

send1=Image.open(os.getcwd()+"\\Graphics\\send.png")
resized_send = send1.resize((16, 16))
isend=ImageTk.PhotoImage(resized_send)
send2=Image.open(os.getcwd()+"\\Graphics\\send_w.png")
resized_send2 = send2.resize((16, 16))
isend_white=ImageTk.PhotoImage(resized_send2)

#___Invertion of images
r,g,b,a = resized_admin.split()
r1,g1,b1,a1 = resized_player.split()
r2,g2,b2,a2 = resized_see.split()
r3,g3,b3,a3 = resized_hide.split()
rgb_image_A = Image.merge('RGB', (r,g,b))
rgb_image_P = Image.merge('RGB', (r1,g1,b1))
rgb_image_see = Image.merge('RGB', (r2,g2,b2))
rgb_image_hide = Image.merge('RGB', (r3,g3,b3))
inv_ad = ImageOps.invert(rgb_image_A)
inv_pl = ImageOps.invert(rgb_image_P)
inv_see = ImageOps.invert(rgb_image_see)
inv_hide = ImageOps.invert(rgb_image_hide)
R,G,B = inv_ad.split()
R1,G1,B1 = inv_pl.split()
R2,G2,B2 = inv_see.split()
R3,G3,B3 = inv_hide.split()
#___

inverted_admin = Image.merge('RGBA', (R,G,B,a))
inverted_player = Image.merge('RGBA', (R1,G1,B1,a1))
admin_black=ImageTk.PhotoImage(inverted_admin)
player_black=ImageTk.PhotoImage(inverted_player)

inverted_see= Image.merge('RGBA', (R2,G2,B2,a2))
inverted_hide= Image.merge('RGBA', (R3,G3,B3,a3))
see= ImageTk.PhotoImage(inverted_see)
hide= ImageTk.PhotoImage(inverted_hide)

wpDark=Image.open(os.getcwd()+"\\Graphics\\wp_Dark.jpg")
resized_wpDark=wpDark.resize((960,540))
wp1= ImageTk.PhotoImage(resized_wpDark)

wpLight=Image.open(os.getcwd()+"\\Graphics\\wp_Light.jpg")
resized_wpLight=wpLight.resize((960,540))
wp2= ImageTk.PhotoImage(resized_wpLight)


#Font and Style
f_helvetica = Font(family="Helvetica",size=20,weight="bold",slant="italic",underline=0,overstrike=0)
f_times = Font(family="Times New Roman",size=20,weight="bold",slant="italic",underline=0,overstrike=0)
f_arial = Font(family="Arial",size=12,weight="normal",slant="italic",underline=0,overstrike=0)
f_verdana = Font(family="Verdana",size=15,weight="bold",slant="roman",underline=0,overstrike=0)
f_sans = Font(family="Comic Sans MS",size=20,weight="bold",slant="roman",underline=0,overstrike=0)
f_trebuchet = Font(family="Trebuchet MS",size=12,weight="normal",slant="roman",underline=0,overstrike=0)
f_georgia = Font(family="Georgia",size=17,weight="bold",slant="roman",underline=0,overstrike=0)

sty= tb.Style(theme='cyborg')
sty.configure("info.TLabel",background="black", foreground='white')
sty.configure("info.Outline.TButton",background="black", foreground='white')
sty.configure("info.TEntry", fieldbackground='black')


#GIF related funtions
def update_gif(canvas, img, frame_index):
    canvas.itemconfig(bg_img, image=img[frame_index])
    if frame_index==56:
        M1.tkraise()
        M1_1.tkraise()
        M1_2.tkraise()
        M1_3.tkraise()
    else:
        root.after(30, update_gif, canvas, img, (frame_index + 1) % len(img))

def update_gif2(canvas, img, frame_index):
    canvas.itemconfig(bg_img, image=img[frame_index])
    if frame_index==56:
        MP.tkraise()
        outputframe.tkraise()
        display()
    else:
        root.after(30, update_gif2, canvas, img, (frame_index + 1) % len(img))


def GIF1_dark():
    LA1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\Graphics\\loading.gif"
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

def GIF1_light():
    LA1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\Graphics\\loading2.gif"
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

def GIF2_dark():
    LP1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\Graphics\\loading.gif"
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

def GIF2_light():
    LP1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\Graphics\\loading2.gif"
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

def update_login_gif(label, label2, label3, label4, img, frame_index):
    label.config(image=img[frame_index])
    label.photo_ref = img[frame_index]
    label2.config(image=img[frame_index])
    label2.photo_ref = img[frame_index]
    label3.config(image=img[frame_index])
    label3.photo_ref = img[frame_index]
    label4.config(image=img[frame_index])
    label4.photo_ref = img[frame_index]
    root.after(40, update_login_gif, label, label2, label3, label4, img, (frame_index + 1) % len(img))

def login_gif():
    gif_path = os.getcwd()+"\\Graphics\\logif.gif"
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
    L1_bg.config(image=frames[0])
    L1_bg.photo_ref = frames[0]
    L1_1_bg.config(image=frames[0])
    L1_1_bg.photo_ref = frames[0]
    LA_bg.config(image=frames[0])
    LA_bg.photo_ref = frames[0]
    LP_bg.config(image=frames[0])
    LP_bg.photo_ref = frames[0]
    update_login_gif(L1_bg, L1_1_bg, LA_bg, LP_bg, frames, 0)  

t1=1 ; t2=1

#other definitions
def themeswap():
    global t, gif_path
    pygame.mixer.music.load(os.getcwd()+"\\Graphics\\toggle.mp3")
    pygame.mixer.music.play(loops=0)

    b_list= [b1,b2,b3,b4,b5,b6,b7,b8,b9,b6_1,b6_2,b6_2_1,b6_2_2,b_reset6,b_reset8,submit4,submit5,submit6_1,submit6_1a,
             team1,team2,mainmenu1,mainmenu2,mainmenu3,mainmenu4,mainmenu5,mainmenu6,mainmenu7,mainmenu8,mainmenu9,
             dteam1,dteam2,refresh,c_1,c_2,c_3,c_4,c_5,c_6]

    e_list= [pe1,pe2,pe3,pe4,pe5,pe6,pe7,ume1,ume4,e6_1,e6_2,e6_1a,e6_2a,s_tag,tag_entry,up_entry,tag_entry9]

    wp_list= (MP_bg,M1_bg,f1_bg,f2_bg,f4_bg,f5_bg,f6_bg,f7_bg,f8_bg,f9_bg)

    if t==0:
        sty=tb.Style(theme="cosmo")
        sty.configure("info.TLabel",background="black")
        sty.configure("info.Outline.TButton",background="black")
        sty.configure("info.TEntry", fieldbackground='black', foreground='white')

        themebutton1.config(bootstyle='dark, outline')
        themebutton2.config(bootstyle='dark, outline')
         
        for i in b_list:
            i.config(style="danger.Outline.TButton")
        for j in e_list:
            j.config(style="danger.TEntry")
        for k in wp_list:
            k.config(image=wp2)

        meter1.configure(bootstyle='danger')
        meter2.configure(bootstyle='danger')
        ume2.configure(bootstyle='danger')
        tag_submit.config(style="danger.Outline.TButton", image=isend)
        up_submit.config(style="danger.Outline.TButton", image=isend)
        s_button.config(style="danger.Outline.TButton", image=isearch)
        tag_submit9.config(style="danger.Outline.TButton", image=isend)
        table2.configure(bootstyle='danger')
        ume3.configure(bootstyle='danger')
        t=1
    elif t==1:
        sty=tb.Style(theme="cyborg")
        sty.configure("info.TLabel",background="black")
        sty.configure("info.Outline.TButton",background="black")
        sty.configure("info.TEntry", fieldbackground='black', foreground='white')

        themebutton1.config(bootstyle='light, outline')
        themebutton2.config(bootstyle='light, outline')

        for i in b_list:
            i.config(style="info.Outline.TButton")
        for j in e_list:
            j.config(style="info.TEntry")
        for k in wp_list:
            k.config(image=wp1)

        meter1.configure(bootstyle='info')
        meter2.configure(bootstyle='info')
        ume2.configure(bootstyle='info')
        tag_submit.config(style="info.Outline.TButton", image=isend_white)
        up_submit.config(style="info.Outline.TButton", image=isend_white)
        s_button.config(style="info.Outline.TButton", image=isearch_white)
        tag_submit9.config(style="info.Outline.TButton", image=isend_white)
        table2.configure(bootstyle='info')
        ume3.configure(bootstyle='info')
        t=0

def logout():
    click()
    Aus2.delete(0, END)
    Apw2.delete(0, END)
    Pus2.delete(0, END)
    Ppw2.delete(0, END)
    L1.tkraise()
    L1_1.tkraise()

def a_eye_toggle():
    click()
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
    click()
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

def on_click(event):
    click()

#Account system

logging.basicConfig(filename=os.getcwd()+"\\login_log.txt", level=logging.INFO, format='%(asctime)s - %(message)s')

def log_login_attempt(username, success=True):
    status = "success" if success else "failed"
    logging.info(f"Login attempt: User '{username}' - {status}")

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

'''def register_user(username, password):
    with open(os.getcwd()+"\\user_accounts.txt", 'a') as file:
        file.write(f"{username}:{hash_password(password)}\n")'''

def login(username, password):
    with open(os.getcwd()+"\\user_accounts.txt", 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and hash_password(password) == stored_password:
                log_login_attempt(username)
                return True
    log_login_attempt(username, success=False)
    return False

def admin_login():
    click()
    global t
    username=Aus2.get()
    Aus2.delete(0, END)
    password=Apw2.get()
    Apw2.delete(0, END)
    if username and password:
        if login(username, password):
            LA1.tkraise()
            if t==0:
                GIF1_dark()
            elif t==1:
                GIF1_light()
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
    click()
    global player_details, t
    username=Pus2.get()
    Pus2.delete(0, END)
    password=Ppw2.get()
    Ppw2.delete(0, END)
    if username and password:
        try:
            x=int(password)
            if plogin(username, password):
                LP1.tkraise()
                if t==0:
                    GIF2_dark()
                elif t==1:
                    GIF2_light()
            else:
                LP_title1.config(text="Login failed")
        except:
            LP_title1.config(text="invalid password")
    else:
        LP_title1.config(text="Please enter both username and password")
    
    


#page swap definitions
def admin_login_swap():
    click()
    LA.tkraise()
def player_login_swap():
    click()
    LP.tkraise()
    LP_1.tkraise()
    LP_2.tkraise()

def f1_swap():
    click()
    f1.tkraise()
def f2_swap():
    click()
    f2.tkraise()
def f3_swap():
    f3.tkraise()
    team_score_update()
def f4_swap():
    click()
    f4.tkraise()
def f5_swap():
    click()
    f5.tkraise()
def f6_swap():
    click()
    f6.tkraise()
    f6_1.tkraise()
    f6_1_1.tkraise()
    f6_1_1_1.tkraise()
    f6_1_1_1a.tkraise()
    f6_1_1_1b.tkraise()
    f6_1_2.tkraise()
    f6_1_2_1.tkraise()
    f6_1_2_1a.tkraise()
    f6_1_2_1b.tkraise()
def f7_swap():
    click()
    f7.tkraise()
def f8_swap():
    click()
    f8.tkraise()
def f9_swap():
    click()
    f9.tkraise()

#main menu definitions
def fmainmenu1():
    click()
    area.config(state='normal')
    area.delete("1.0", END)
    area.config(state='disable')
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu2():
    click()
    table2.forget()
    area2.pack()
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu3():
    click()
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu4():
    click()
    for entry in [pe1,pe2,pe3,pe4,pe5,pe6,pe7]:
        entry.delete(0, 'end')
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu5():
    click()
    for entry in [ume1,ume4]:
        entry.delete(0, 'end')
    ume2.entry.delete(0, 'end')
    ume2.entry.insert(0, ume2._startdate.strftime(ume2._dateformat))
    ume3.set('')
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu6():
    reset6()
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu7():
    click()
    s_tag.delete(0, 'end')
    s_tag.insert(0, 'Enter player tag')
    s_tag.config(foreground='grey')
    outputframe7.forget()
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu8():
    reset8()
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()
def fmainmenu9():
    click()
    tag_entry9.delete(0, 'end')
    M1.tkraise()
    M1_1.tkraise()
    M1_2.tkraise()
    M1_3.tkraise()

#sql connectivity functions
um_content=''
def um(team):
    click()
    global um_content
    area.config(state='normal')
    um_content=''
    if team==1:
        q_1="select * from schedule where Participant='team1'"
    elif team==2:
        q_1="select * from schedule where Participant='team2'"
    cur.execute(q_1)
    records = cur.fetchall()
    for row in records:
        um_content+=f'League: {row[0]} \n Date: {row[1]} \n Participant: {row[2]} \n Prize: {row[3]} $ \n\n'
    area.delete("1.0", END)
    area.insert("1.0", um_content)
    area.config(state='disable')

rowdata=[]
def dt(team):
    click()
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

teamscore1=0
teamscore2=0
def team_score_update():
    click()
    global teamscore1, teamscore2
    meter1.configure(amountused = 0)
    meter2.configure(amountused = 0)
    q_2_1=f'select sum(Player_Score) from team1'
    q_2_2=f'select sum(Player_Score) from team2'
    cur.execute(q_2_1)
    for i in cur:
        teamscore1 = i[0]
    cur.execute(q_2_2)
    for i in cur:
        teamscore2 = i[0]
    meter1_gif(0)
    meter2_gif(0)

def meter1_gif(x):
        global teamscore1
        meter1.configure(amountused = x)
        if x==teamscore1:
            pass
        elif x < teamscore1-15:
            root.after(30, meter1_gif, x+10)
        else:
            root.after(30, meter1_gif, x+1)
def meter2_gif(x):
        global teamscore2
        meter2.configure(amountused = x)
        if x==teamscore2:
            pass
        elif x < teamscore2-15:
            root.after(30, meter2_gif, x+10)
        else:
            root.after(30, meter2_gif, x+1)


def addplayer():
    click()
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
    click()
    name=ume1.get()
    date=ume2.entry.get()
    team=ume3.get()
    prize=ume4.get()
    if team=='team1' or team=='team2':
        q5=f"insert into schedule values('{name}','{date}','{team}',{prize})"
        try:
            cur.execute(q5)
            success5.pack()
            root.after(2000, messageclear, success5)
        except:
            fail5_1.pack()
            root.after(2000, messageclear, fail5_1)
    else:
        fail5_2.pack()
        root.after(2000, messageclear, fail5_2)

def search():
    click()
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
    click()
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
    click()
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
    click()
    f6_1_2.pack(pady=8)
    b6_2.config(state='disabled')
    b6_1.config(command=nope)
def ad1():
    click()
    global swapchoice2
    f6_1_2_1.pack()
    b6_2_1.config(state='disabled')
    b6_2_2.config(command=nope)
    swapchoice2=1
def ad2():
    click()
    global swapchoice2
    f6_1_2_1.pack()
    b6_2_2.config(state='disabled')
    b6_2_1.config(command=nope)
    swapchoice2=2
def reset6():
    click()
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
    click()
    global col_choice
    index=clicked - 1
    buttonlist[index].config(state='disabled')
    for button in buttonlist:
        button.config(command=nope)
    col_choice=clicked
    entryframe8_1.pack()
    pass
def submit8_1():
    click()
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
    click()
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
            q_8_1 = f"Update information set password = {up} where tag = {up}"
            cur.execute(q_8)
            cur.execute(q_8_1)
        up_entry.config(state='disabled')
        success8.pack()
        root.after(1000, messageclear, success8)
    except:
        fail8_3.pack()
        root.after(1000, messageclear, fail8_3)
def reset8():
    click()
    c_1.config(state='normal', command=lambda: get_ctu(1))
    c_2.config(state='normal', command=lambda: get_ctu(2))
    c_3.config(state='normal', command=lambda: get_ctu(3))
    c_4.config(state='normal', command=lambda: get_ctu(4))
    c_5.config(state='normal', command=lambda: get_ctu(5))
    c_6.config(state='normal', command=lambda: get_ctu(6))
    tag_entry.config(state='normal')
    tag_entry.delete(0, 'end')
    up_entry.config(state='normal')
    up_entry.delete(0, 'end')
    entryframe8_2.forget()
    entryframe8_1.forget()
#(Update details definition end)

def remove():
    click()
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
L1_bg= Label(L1)
L1_1_bg= Label(L1_1)
L1_title=tb.Label(L1,style="info.TLabel", text='ESPORTS MANAGEMENT SYSTEM', font=f_helvetica, relief='groove', padding=5)
L1_title1=tb.Label(L1,style="info.TLabel", text=' SELECT LOGIN TYPE ', font=f_georgia,relief='raised')
L1_title2_1=tb.Label(L1,style="info.TLabel", text=' ADMIN ', font=f_trebuchet,relief='raised')
L1_title2_2=tb.Label(L1,style="info.TLabel", text=' PLAYER ', font=f_trebuchet,relief='raised')
b_admin=tb.Button(L1_1, bootstyle='info, outline',style="info.Outline.TButton", image=admin, command=admin_login_swap)
b_player=tb.Button(L1_1, bootstyle='info, outline',style="info.Outline.TButton", image=player, command=player_login_swap)

L1_bg.place(x=-2,y=-2)
L1_1_bg.place(x=-218,y=-179)
L1_title.pack(pady=20)
L1_title1.pack(pady=(20,20))
L1_1.pack(pady=20)
b_admin.pack(side='left', padx=(0,40) )
b_player.pack(side='left', padx=(40,0))
L1_title2_1.pack(side='left',padx=(290,0))
L1_title2_2.pack(side="right",padx=(0,285))

#LA items
LA_bg=Label(LA)
LA_1=tb.Frame(LA)
LA_2=tb.Frame(LA)
LA_title=tb.Label(LA, style="info.TLabel", text='ADMIN LOGIN', font=f_georgia, padding=5)
LA_title1=tb.Label(LA, style="info.TLabel", text='Enter Username and Password', font=f_trebuchet)
LA_back=tb.Button(LA, style="info.Outline.TButton", text='Back', command=logout)
Aus1=tb.Label(LA_1, style="info.TLabel", text='Username ',font=f_trebuchet)
Apw1=tb.Label(LA_2, style="info.TLabel", text='Password  ',font=f_trebuchet)
Aus2=tb.Entry(LA_1, style="info.TEntry")
Apw2=tb.Entry(LA_2,style="info.TEntry", show='*', width=14)
Aeye=tb.Button(LA_2, style="info.Outline.TButton", image=see, command=a_eye_toggle)
submit1=tb.Button(LA, style="info.Outline.TButton", text='Submit', command=admin_login)

LA_bg.place(x=-2,y=-2)
Aus1.pack(side='left')
Aus2.pack(side='left')
Apw1.pack(side='left')
Apw2.pack(side='left')
Aeye.pack(side='left')
LA_title.pack(pady=20)
LA_title1.pack(pady=(20,20))
LA_1.pack()
LA_2.pack()
submit1.pack(pady=(20,5))
LA_back.pack()

#LA1 items
load1=tb.Label(LA1)


#LP items
LP_1=tb.Frame(LP)
LP_2=tb.Frame(LP)
LP_bg=Label(LP)
LP_title=tb.Label(LP, style="info.TLabel", text='PLAYER LOGIN',font=f_georgia, padding=5)
LP_title1=tb.Label(LP, style="info.TLabel", text='Enter Username and Password',font=f_trebuchet)
LP_back=tb.Button(LP, style="info.Outline.TButton", text='Back', command=logout)
Pus1=tb.Label(LP_1, style="info.TLabel", text='Username ',font=f_trebuchet)
Ppw1=tb.Label(LP_2, style="info.TLabel", text='Password  ',font=f_trebuchet)
Pus2=tb.Entry(LP_1, style="info.TEntry")
Ppw2=tb.Entry(LP_2, style="info.TEntry", show='*', width=13)
Peye=tb.Button(LP_2, style="info.Outline.TButton", image=see, command=p_eye_toggle)
submit2=tb.Button(LP, style="info.Outline.TButton", text='Submit', command=player_login)

LP_bg.place(x=-2,y=-2)
Pus1.pack(side='left')
Pus2.pack(side='left')
Ppw1.pack(side='left')
Ppw2.pack(side='left')
Peye.pack(side='left')
LP_title.pack(pady=20)
LP_title1.pack(pady=(20,20))
LP_1.pack()
LP_2.pack()
submit2.pack(pady=(20,5))
LP_back.pack()

#LP1 items
load2=tb.Label(LP1)

#MP items
MP_bg=tb.Label(MP,image=wp1)
MP_title=tb.Label(MP, text= 'Welcome', font=f_times)
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

MP_logout=tb.Button(MP, style='danger.Outline.TButton', text='LOGOUT', command=logout)
themebutton2=tb.Button(MP, bootstyle="light, outline",text="Switch Theme", command=themeswap)

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

MP_bg.place(x=0,y=0)
MP_title.pack(pady=(100,10))
outputframe.pack()
MP_logout.pack(side='left',anchor='sw', padx=5, pady=5)
themebutton2.pack(side='right', anchor='se', padx=5, pady=5)


#M1 items
M1_1=tb.Frame(M1)
M1_2=tb.Frame(M1)
M1_3=tb.Frame(M1)

M1_bg=tb.Label(M1, image=wp1)
b1=tb.Button(M1_1, text='Display upcoming matches', command=f1_swap,style="info.Outline.TButton")
b2=tb.Button(M1_1, text='Display team', command=f2_swap,style="info.Outline.TButton")
b3=tb.Button(M1_1, text='Display team score', command=f3_swap,style="info.Outline.TButton")
b4=tb.Button(M1_2, text='Add player', command=f4_swap,style="info.Outline.TButton")
b5=tb.Button(M1_2, text='Add upcoming match', command=f5_swap,style="info.Outline.TButton")
b6=tb.Button(M1_2, text='Edit team', command=f6_swap,style="info.Outline.TButton")
b7=tb.Button(M1_3, text='Search player', command=f7_swap,style="info.Outline.TButton")
b8=tb.Button(M1_3, text='Update player details', command=f8_swap,style="info.Outline.TButton")
b9=tb.Button(M1_3, text='Remove player', command=f9_swap,style="info.Outline.TButton")
themebutton1=tb.Button(M1, bootstyle="light, outline",text="Switch Theme", command=themeswap)

M1_title=tb.Label(M1, text='ESPORTS MANAGEMENT SYSTEM', font=f_helvetica, relief='groove', padding=5)
M1_logout=tb.Button(M1, style='danger.Outline.TButton', text='LOGOUT', command=logout)

M1_bg.place(x=0,y=0)
b1.pack(side='left',padx=5)
b2.pack(side='left',padx=5)
b3.pack(side='left',padx=5)
b4.pack(side='left',padx=5)
b5.pack(side='left',padx=5)
b6.pack(side='left',padx=5)
b7.pack(side='left',padx=5)
b8.pack(side='left',padx=5)
b9.pack(side='left',padx=5)
M1_title.pack(pady=(70,50))
M1_1.pack(pady=(30,5))
M1_2.pack(pady=(0,5))
M1_3.pack(pady=(0,5))
M1_logout.pack(side='left', anchor='sw', padx=5, pady=5)
themebutton1.pack(side='right', anchor='se', padx=5, pady=5)

#f1 items
f1_bg=tb.Label(f1,image=wp1)
f1_title=tb.Label(f1, text='Upcoming Matches', font=f_verdana, relief='groove', padding=2)
f1_title1=tb.Label(f1, text='Select a team to view their upcoming matches',font=f_trebuchet)
f1_1=tb.Frame(f1)
team1=tb.Button(f1_1, style='info.Outline.TButton', text='Team 1', command=lambda: um(1))
team2=tb.Button(f1_1, style='info.Outline.TButton', text='Team 2', command=lambda: um(2))
area=tb.Text(f1, height= 15, width= 52, relief='sunken', state='disable')
mainmenu1=tb.Button(f1, style='info.Outline.TButton', text='Main Menu', command=fmainmenu1)

f1_bg.place(x=0,y=0)
f1_title.pack(pady=20)
f1_title1.pack(pady=(0,10))
team1.pack(side='left')
team2.pack(side='left')
f1_1.pack(pady=5)
area.pack()
mainmenu1.pack(side='bottom')

#f2 items
f2_bg=tb.Label(f2,image=wp1)
f2_title=tb.Label(f2, text='Display Team', font=f_verdana, relief='groove', padding=2)
f2_title1=tb.Label(f2, text='Select a team to view members',font=f_trebuchet)
f2_1=tb.Frame(f2)
dteam1=tb.Button(f2_1, style='info.Outline.TButton', text='Team 1', command=lambda: dt(1))
dteam2=tb.Button(f2_1, style='info.Outline.TButton', text='Team 2', command=lambda: dt(2))
area2=tb.Text(f2, height= 15, width= 52, relief='sunken', state='disable')

coldata=[{'text':'Tag', "stretch": False}, {'text':'Player ID', "stretch": False}, {'text':'Role', "stretch": False}, {'text':'Score', "stretch": False} ]

table2=Tableview(
    master=f2,
    coldata=coldata,
    rowdata=rowdata,
    paginated=False,
    searchable=False,
    bootstyle=INFO,
    stripecolor=(colors.light, None),
    height=4,
)
mainmenu2=tb.Button(f2, style='info.Outline.TButton', text='Main Menu', command=fmainmenu2)

f2_bg.place(x=0,y=0)
f2_title.pack(pady=20)
f2_title1.pack(pady=(0,10))
dteam1.pack(side='left')
dteam2.pack(side='left')
f2_1.pack(pady=8)
area2.pack()
mainmenu2.pack(side='bottom')

#f3 items

# f3_bg=tb.Label(f3,image=wp1)
f3_title=tb.Label(f3, text='Display Team Score', font=f_verdana, relief='groove', padding=2)
f3_title1=tb.Label(f3, text='Select a team to view team score',font=f_trebuchet)
f3_1=tb.Frame(f3)
'''steam1=tb.Button(f3_1, text='Team 1', command=lambda: team_score(1))
steam2=tb.Button(f3_1, text='Team 2', command=lambda: team_score(2))'''
mainmenu3=tb.Button(f3, style='info.Outline.TButton', text='Main Menu', command=fmainmenu3)
scorelabel=tb.Label(f3)
meters=tb.Frame(f3)
meter1=tb.Meter(meters, bootstyle='info', subtext='TEAM 1', interactive=False, textright='/400',
              metertype='semi', amounttotal=400, amountused=0)
meter2=tb.Meter(meters, bootstyle='info', subtext='TEAM 2', interactive=False, textright='/400',
              metertype='semi', amounttotal=400, amountused=0)
refresh=tb.Button(f3, text= 'Refresh', command= team_score_update, style="info.Outline.TButton")

# f3_bg.place(x=0,y=0)
f3_title.pack(pady=20)
f3_title1.pack(pady=(0,10))
'''steam1.pack(side='left')
steam2.pack(side='left')'''
f3_1.pack()
scorelabel.pack()
meter1.pack(side='left')
meter2.pack(side='left')
meters.pack()
mainmenu3.pack(side='bottom')
refresh.pack(side='bottom',pady=5)

#f4 items
f4_bg=tb.Label(f4,image=wp1)
entryframe4=tb.Frame(f4,border=2, borderwidth=2)
f4_title=tb.Label(f4, text='Add Player', font=f_verdana, relief='groove', padding=2)
f4_title1=tb.Label(f4, text='Input Details',font=f_trebuchet)
pe1=tb.Entry(entryframe4, style="info.TEntry")
pe2=tb.Entry(entryframe4, style="info.TEntry")
pe3=tb.Entry(entryframe4, style="info.TEntry")
pe4=tb.Entry(entryframe4, style="info.TEntry")
pe5=tb.Entry(entryframe4, style="info.TEntry")
pe6=tb.Entry(entryframe4, style="info.TEntry")
pe7=tb.Entry(entryframe4, style="info.TEntry")
pl1=tb.Label(entryframe4, text='Tag',font=f_trebuchet)
pl2=tb.Label(entryframe4, text='Player ID',font=f_trebuchet)
pl3=tb.Label(entryframe4, text='Role',font=f_trebuchet)
pl4=tb.Label(entryframe4, text='Score',font=f_trebuchet)
pl5=tb.Label(entryframe4, text='Name',font=f_trebuchet)
pl6=tb.Label(entryframe4, text='Region',font=f_trebuchet)
pl7=tb.Label(entryframe4, text='Regional rank',font=f_trebuchet)
submit4=tb.Button(f4, style='info.Outline.TButton', text='Submit', command=addplayer)
success4=tb.Label(f4, text='Added succesfully',font=f_arial)
fail4=tb.Label(f4, text='Unsuccesful',font=f_arial)
mainmenu4=tb.Button(f4, style='info.Outline.TButton', text='Main Menu', command=fmainmenu4)

f4_bg.place(x=0,y=0)
f4_title.pack(pady=(20,50))
f4_title1.pack(pady=(0,10))

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
submit4.pack(pady=20)
mainmenu4.pack(side='bottom')

#f5 items
f5_bg=tb.Label(f5,image=wp1)
teams=['team1', 'team2']
entryframe5=tb.Frame(f5)
f5_title=tb.Label(f5, text='Add Upcoming Matches', font=f_verdana, relief='groove', padding=2)
f5_title1=tb.Label(f5, text='Input Details',font=f_trebuchet)
ume1=tb.Entry(entryframe5, style="info.TEntry")
ume2=tb.DateEntry(entryframe5, dateformat='%Y-%m-%d', bootstyle='info', firstweekday=0, startdate=date.today())
ume2.entry.config(width=15)
ume2.button.config(command=lambda: [ume2._on_date_ask(), click()])
ume2.button.bind('<FocusIn>', on_click)
ume3=tb.Combobox(entryframe5, bootstyle='info', values=teams, state='readonly', width=18)
ume3.bind('<Button-1>', on_click)
ume4=tb.Entry(entryframe5, style="info.TEntry")
uml1=tb.Label(entryframe5, text='League',font=f_trebuchet)
uml2=tb.Label(entryframe5, text='Date',font=f_trebuchet)
uml3=tb.Label(entryframe5, text='Participants',font=f_trebuchet)
uml4=tb.Label(entryframe5, text='Prize',font=f_trebuchet)

submit5=tb.Button(f5, style='info.Outline.TButton', text='Submit', command=addum)
success5=tb.Label(f5, text='Added succesfully',font=f_arial)
fail5_1=tb.Label(f5, text='Unsuccesful',font=f_arial)
fail5_2=tb.Label(f5, text='Select a team',font=f_arial)
mainmenu5=tb.Button(f5, style='info.Outline.TButton', text='Main Menu', command=fmainmenu5)

f5_bg.place(x=0,y=0)
f5_title.pack(pady=(50,60))
f5_title1.pack(pady=(0,10))

ume1.grid(row= 0, column= 1)
ume2.grid(row= 1, column= 1)
ume3.grid(row= 2, column= 1)
ume4.grid(row= 3, column= 1)
uml1.grid(row= 0, column= 0,pady=5)
uml2.grid(row= 1, column= 0,pady=5)
uml3.grid(row= 2, column= 0,pady=5)
uml4.grid(row= 3, column= 0,pady=5)

entryframe5.pack()
submit5.pack(pady=20)
mainmenu5.pack(side='bottom')

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

f6_bg=tb.Label(f6,image=wp1)
b6_1=tb.Button(f6_1, text='Between Teams', command=aa,style="info.Outline.TButton")
b6_2=tb.Button(f6_1, text='From Reserve to Teams', command=ac,style="info.Outline.TButton")
l6_1=tb.Label(f6_1_1_1a,text="Enter Tag of player to swap from Team 1    ",font=f_trebuchet)
l6_2=tb.Label(f6_1_1_1b,text="Enter Tag of player to swap from Team 2    ",font=f_trebuchet)
e6_1=tb.Entry(f6_1_1_1a, style="info.TEntry",width=45)
e6_2=tb.Entry(f6_1_1_1b, style="info.TEntry",width=45)
submit6_1=tb.Button(f6_1_1_1, text='SUBMIT', command=ab1,style="info.Outline.TButton")
b6_2_1=tb.Button(f6_1_2, text='To Team1', command=ad1,style="info.Outline.TButton")
b6_2_2=tb.Button(f6_1_2, text='To Team2', command=ad2,style="info.Outline.TButton")
l6_1a=tb.Label(f6_1_2_1a,text="Enter Tag of player from reserve    ",font=f_trebuchet)
l6_2a=tb.Label(f6_1_2_1b,text="Enter Tag of player in team    ",font=f_trebuchet)
e6_1a=tb.Entry(f6_1_2_1a, style="info.TEntry",width=36)
e6_2a=tb.Entry(f6_1_2_1b, style="info.TEntry",width=30)
submit6_1a=tb.Button(f6_1_2_1,  text='SUBMIT', command=ab2,style="info.Outline.TButton")
f6_title=tb.Label(f6, text='Swap Players', font=f_verdana, relief='groove', padding=2)
success6=tb.Label(f6, text='Swap succesful!!',font=f_arial)
fail6=tb.Label(f6, text='Swap unsuccesful...',font=f_arial)
fail6_1=tb.Label(f6, text='Fill in both',font=f_arial)
b_reset6=tb.Button(f6, text='Reset selection', command=reset6, style="info.Outline.TButton")
mainmenu6=tb.Button(f6, style='info.Outline.TButton', text='Main Menu', command=fmainmenu6)

f6_bg.place(x=0,y=0)
b6_1.pack(side='left')
b6_2.pack(side='left')
l6_1.pack(side='top')
e6_1.pack(side='left')
f6_1_1_1a.pack(side='left',pady=5)
l6_2.pack(side='top')
e6_2.pack(side='left')
f6_1_1_1b.pack(side='left',pady=5)
submit6_1.pack(pady=(40,0))
b6_2_1.pack(side='left')
b6_2_2.pack(side='left')
l6_1a.pack(side='top')
e6_1a.pack(side='left')
f6_1_2_1a.pack(side='left',pady=5)
l6_2a.pack(side='top')
e6_2a.pack(side='left')
f6_1_2_1b.pack(side='left',pady=5)
submit6_1a.pack(pady=(40,0))

f6_title.pack(pady=20)
f6_1.pack(pady=8)
mainmenu6.pack(side='bottom')
b_reset6.pack(side='bottom',pady=5)

#f7 items
f7_bg=tb.Label(f7,image=wp1)
outputframe7=tb.Frame(f7)
searchbar=tb.Frame(f7)
f7_title=tb.Label(f7, text='Search Players', font=f_verdana, relief='groove',padding=2)
s_tag=tb.Entry(searchbar, style="info.TEntry")
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
opl1=tb.Label(outputframe7, text='Tag',font=f_trebuchet)
opl2=tb.Label(outputframe7, text='Player ID',font=f_trebuchet)
opl3=tb.Label(outputframe7, text='Role',font=f_trebuchet)
opl4=tb.Label(outputframe7, text='Score',font=f_trebuchet)
opl5=tb.Label(outputframe7, text='Name',font=f_trebuchet)
opl6=tb.Label(outputframe7, text='Region',font=f_trebuchet)
opl7=tb.Label(outputframe7, text='Regional rank',font=f_trebuchet)

fail7_1=tb.Label(f7, text='Player not found',font=f_arial)
fail7_2=tb.Label(f7, text='Invalid tag',font=f_arial)
s_button=tb.Button(searchbar, style='info.Outline.TButton', image=isearch_white, command=search)
mainmenu7=tb.Button(f7, style='info.Outline.TButton', text='Main Menu', command=fmainmenu7)

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

f7_bg.place(x=0,y=0)
f7_title.pack(pady=20)
s_tag.pack(side='left')
s_button.pack(side='left')
searchbar.pack(pady=(0,25))
mainmenu7.pack(side='bottom')

#f8 items
f8_bg=tb.Label(f8,image=wp1)
buttonframe=tb.Frame(f8)
entryframe8_1=tb.Frame(f8)
entryframe8_2=tb.Frame(f8)
f8_title=tb.Label(f8, text='Update player details', font=f_verdana, relief='groove', padding=2)
f8_title1=tb.Label(f8, text='Select coloumn to update',font=f_trebuchet)

c_1=tb.Button(buttonframe, style='info.Outline.TButton', text='Tag', command=lambda: get_ctu(1))
c_2=tb.Button(buttonframe, style='info.Outline.TButton', text='Player ID', command=lambda: get_ctu(2))
c_3=tb.Button(buttonframe, style='info.Outline.TButton', text='Player Name', command=lambda: get_ctu(3))
c_4=tb.Button(buttonframe, style='info.Outline.TButton', text='Score', command=lambda: get_ctu(4))
c_5=tb.Button(buttonframe, style='info.Outline.TButton', text='Region', command=lambda: get_ctu(5))
c_6=tb.Button(buttonframe, style='info.Outline.TButton', text='Regional Rank', command=lambda: get_ctu(6))
buttonlist=[c_1,c_2,c_3,c_4,c_5,c_6]
tag_label=tb.Label(entryframe8_1, text='Enter tag of player ',font=f_trebuchet)
tag_entry=tb.Entry(entryframe8_1, style="info.TEntry")
tag_submit=tb.Button(entryframe8_1, style='info.Outline.TButton', image=isend_white, command=submit8_1)
up_label=tb.Label(entryframe8_2, text='Enter new detail    ',font=f_trebuchet)
up_entry=tb.Entry(entryframe8_2, style="info.TEntry")
up_submit=tb.Button(entryframe8_2, style='info.Outline.TButton', image=isend_white, command=submit8_2)
fail8_1=tb.Label(f8, text='Invalid tag',font=f_arial)
fail8_2=tb.Label(f8, text='No player found',font=f_arial)
fail8_3=tb.Label(f8, text='Error. Try again',font=f_arial)
success8=tb.Label(f8, text='Update successful',font=f_arial)
b_reset8=tb.Button(f8, text='Reset selection', command=reset8,style="info.Outline.TButton")
mainmenu8=tb.Button(f8, style='info.Outline.TButton', text='Main Menu', command=fmainmenu8)

c_1.grid(row= 0,column= 0,pady=(0,5),padx=5)
c_2.grid(row= 0,column= 1,pady=(0,5),padx=5)
c_3.grid(row= 0,column= 2,pady=(0,5),padx=5)
c_4.grid(row= 1,column= 0,padx=5)
c_5.grid(row= 1,column= 1,padx=5)
c_6.grid(row= 1,column= 2,padx=5)

f8_bg.place(x=0,y=0)
tag_label.pack(side='left')
tag_entry.pack(side='left')
tag_submit.pack(side='left')
up_label.pack(side='left')
up_entry.pack(side='left')
up_submit.pack(side='left')
f8_title.pack(pady=(30,40))
f8_title1.pack(pady=(0,10))
buttonframe.pack(pady=30)
mainmenu8.pack(side='bottom')
b_reset8.pack(side='bottom')

#f9 items
f9_bg=tb.Label(f9,image=wp1)
entryframe9=tb.Frame(f9)
f9_title=tb.Label(f9, text='Remove player', font=f_verdana, relief='groove', padding=2)
f9_title1=tb.Label(f9, text='Note- Players playing for either teams cannot be removed.',font=f_trebuchet)
tag_label9=tb.Label(entryframe9, text='Enter tag of player to be removed ',font=f_trebuchet)
tag_entry9=tb.Entry(entryframe9, style="info.TEntry")
fail9_1=tb.Label(f9, text='Invalid tag',font=f_arial)
fail9_2=tb.Label(f9, text='Player not found',font=f_arial)
fail9_3=tb.Label(f9, text="Can't execute command because player already exist in a team",font=f_arial)
success9=tb.Label(f9, text='Player removed successfully',font=f_arial)
tag_submit9=tb.Button(entryframe9, style='info.Outline.TButton', image=isend_white, command=remove)
mainmenu9=tb.Button(f9, style='info.Outline.TButton', text='Main Menu', command=fmainmenu9)

f9_bg.place(x=0,y=0)
tag_label9.pack(side='left')
tag_entry9.pack(side='left')
tag_submit9.pack(side='left')
f9_title.pack(pady=(50,110))
f9_title1.pack(pady=(0,10))
entryframe9.pack()
mainmenu9.pack(side='bottom')

#Main frames set up
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frames=[L1,LA,LP,LA1,LP1,MP,M1,f1,f2,f3,f4,f5,f6,f7,f8,f9]
for frame in frames:
    frame.grid(row=0, column=0, sticky="nsew")

L1.tkraise()
L1_1.tkraise()
login_gif()
root.mainloop()