import tkinter as tk
from tkinter import messagebox


def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Add code here to save the username and password to a database or file

    messagebox.showinfo("Success", "Registration successful")


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Add code here to check if the username and password match the saved credentials

    messagebox.showinfo("Success", "Login successful")



# Create the main window
window = tk.Tk()
window.title("Registration and Login")
window.geometry("500x400")

# Username label and entry
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window, background='wheat1')
entry_username.pack()

# Password label and entry
label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*", background='wheat1')
entry_password.pack()

# Confirm password label and entry
label_confirm_password = tk.Label(window, text="Confirm Password:")
label_confirm_password.pack()
entry_confirm_password = tk.Entry(window, show="*", background='wheat1')
entry_confirm_password.pack()

# Register button
btn_register = tk.Button(window, text="Register", command=register, background='cyan2')
btn_register.pack()

# Login button
btn_login = tk.Button(window, text="  Login  ", command=login, background='pink1')
btn_login.pack()

# Start the Tkinter event loop
window.mainloop()
