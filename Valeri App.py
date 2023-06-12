import csv
from datetime import datetime
import os
import smtplib
import tkinter as tk
import pyautogui as pg
import time
import subprocess, random
from tkinter import *
from tkinter import messagebox
import pyttsx3


# Registering the user
def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Code to save the username and password to a database or file
    reg_users(username, password)

    messagebox.showinfo("Success", "Registration successful")


# Login the user
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Code to check if the username and password match the saved credentials

    # In case of success
    if check_username(username, password):
        messagebox.showinfo("Success", "Login Successful")

    # In case of bad user
    else:
        messagebox.showinfo("USER DOEST EXIST", "User doesn't exist")
        time.sleep(2)
        # voice warning
        message = 'WARNING Your have attempt unauthorized action! The security department has been informed.' \
           ' Your identity will be captured!'
        text_to_speach(message)
        # opening the camera
        camera_recording_the_user()
        # sending email warning
        time_of_attempt = get_current_time()
        subject = 'WARNING. Unauthorized login attempt'
        body = f'Unauthorized user - | {username.upper()} | with password - ' \
               f'| {password.upper()} | has attempt to login to the system ' \
               f'at {time_of_attempt}!!!'
        email_message = 'Email with your details has been sent to the security department.'
        text_to_speach(email_message)
        #send_email('', '', '', subject, body)





# Adding users to CSV file
def reg_users(user, password):
    with open('Users_REg.csv', 'a', newline='') as csvfile:
        fieldnames = ['User', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #writer.writeheader()
        info = {f'User': user,
                f'Password': password}
        writer.writerow(info)


# Checking if user exist
def check_username(user, password):
    with open("Users_REg.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            current_user = row[0]
            current_password = row[1]
            if user == current_user and password == current_password:
                return True
        return False


# The camera will open and screenshot the face of the intruder
def camera_recording_the_user():
    # Launch Windows OS Camera
    subprocess.run('start microsoft.windows.camera:', shell=True)

    time.sleep(2)  # Required !
    img = pg.screenshot()  # Take screenshot using PyAutoGUI's function
    time.sleep(2)  # Required !
    num = random.randint(1, 100)
    destination_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\\")
    img.save(
        f"{destination_folder}\Selfie{num}.png")  # Save image screenshot at desired location on your computer

    # Close the camera
    subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)

    # Displaying warning message
    top = Tk()
    top.geometry("20x20")
    messagebox.showinfo("WARNING", "Your have attempt unauthorized action!!! Your identity has been captured!")
    top.mainloop()


# Text to speach
def text_to_speach(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Sending Email to secure mailbox
def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")



# getting current time
def get_current_time():
    time = datetime.now().strftime('%Y-%m-%d')
    return time




""" TKinter Box"""

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

