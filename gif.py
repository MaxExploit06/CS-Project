import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def update_gif(canvas, img, frame_index):
    canvas.itemconfig(bg_img, image=img[frame_index])
    root.after(100, update_gif, canvas, img, (frame_index + 1) % len(img))

root = tk.Tk()
root.geometry("500x500")  # Set the window size

def gif():
    global bg_img
    # Load the animated GIF image
    gif_path = "C:\\Users\\USER\\Downloads\\anime.gif"
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

    # Create a Canvas widget to display the GIF background
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    # Create a background image on the Canvas
    bg_img = canvas.create_image(0, 0, anchor=tk.NW, image=frames[0])

    # Start the animation loop
    update_gif(canvas, frames, 0)

    # Add other widgets and functionality here
gif()


root.mainloop()