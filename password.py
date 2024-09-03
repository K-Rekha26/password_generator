import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_entry.get()
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid length")
        return
    
    length = int(length)
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4")
        return

    complexity = complexity_var.get()
    characters = ""
    
    if complexity == "Low":
        characters = string.ascii_lowercase
    elif complexity == "Medium":
        characters = string.ascii_letters
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a frame for the inputs
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Create length label and entry
length_label = tk.Label(input_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=10)
length_entry = tk.Entry(input_frame)
length_entry.grid(row=0, column=1, padx=10)

# Create complexity label and dropdown
complexity_label = tk.Label(input_frame, text="Complexity:")
complexity_label.grid(row=1, column=0, padx=10)
complexity_var = tk.StringVar(value="Medium")
complexity_options = ["Low", "Medium", "High"]
complexity_menu = tk.OptionMenu(input_frame, complexity_var, *complexity_options)
complexity_menu.grid(row=1, column=1, padx=10)

# Create a button to generate the password
generate_button = tk.Button(input_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, columnspan=2, pady=10)

# Create an entry to display the generated password
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=10)

# Run the main loop
root.mainloop()
