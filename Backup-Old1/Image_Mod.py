from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


def update_gif(canvas, img, frame_index, M1, root):
    canvas.itemconfig(bg_img, image=img[frame_index])
    if frame_index==56:
        M1.tkraise()
    else:
        root.after(30, update_gif, canvas, img, (frame_index + 1) % len(img),M1,root)

def update_gif2(canvas, img, frame_index, MP, root):
    canvas.itemconfig(bg_img, image=img[frame_index])
    if frame_index==56:
        MP.tkraise()
    else:
        root.after(30, update_gif2, canvas, img, (frame_index + 1) % len(img),MP,root)


def GIF1_dark(LA1,M1,root):
    LA1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\CS-Project\\Graphics\\loading.gif"
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
    update_gif(canvas, frames, 0, M1, root)

def GIF1_light(LA1,M1,root):
    LA1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\CS-Project\\Graphics\\loading2.gif"
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
    update_gif(canvas, frames, 0, M1, root)

def GIF2_dark(LP1,MP,root):
    LP1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\CS-Project\\Graphics\\loading.gif"
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
    update_gif2(canvas, frames, 0, MP, root)

def GIF2_light(LP1,MP,root):
    LP1.tkraise()
    global bg_img
    # Load the animated GIF image
    gif_path = os.getcwd()+"\\CS-Project\\Graphics\\loading2.gif"
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
    update_gif2(canvas, frames, 0, MP, root)