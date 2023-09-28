import tkinter as tk

# Define themes with button colors
themes = {
    "light": {"button": "white", "text": "black"},
    "dark": {"button": "black", "text": "white"}
}

# Function to change the theme
def change_theme(theme_name):
    button_color = themes[theme_name]["button"]
    text_color = themes[theme_name]["text"]

    # Update button colors
    button.config(bg=button_color, fg=text_color)

    # Update the color of another button with a command
    update_button_color(button_with_command, button_color)

# Function to toggle the theme
def toggle_theme():
    current_theme = theme_var.get()
    new_theme = "light" if current_theme == "dark" else "dark"
    theme_var.set(new_theme)
    change_theme(new_theme)

# Function to change the color of another button
def update_button_color(button_to_update, color):
    button_to_update.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Theme Change Example")

# Create a button with a command
button_with_command = tk.Button(root, text="Button with Command", command=lambda: print("Button Clicked"))
button_with_command.pack(padx=20, pady=20)

# Create a button to change the theme
theme_var = tk.StringVar()
theme_var.set("light")  # Initial theme
button = tk.Button(root, text="Change Theme", command=toggle_theme)
button.pack(padx=20, pady=20)

# Initialize button color
change_theme(theme_var.get())

root.mainloop()
