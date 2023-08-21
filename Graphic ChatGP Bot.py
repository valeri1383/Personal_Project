import tkinter as tk
from tkinter import scrolledtext, Entry, Button
import openai

# Set your OpenAI API key here
openai.api_key = "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"

messages = []

# Create the main window
root = tk.Tk()
root.title("Chat Box")

# Create a scrolled text widget for displaying the chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10)

# Create an entry widget for typing messages
entry = Entry(root)
entry.pack(fill=tk.BOTH, padx=10, pady=5)

def send_message():
    message = entry.get()
    if message:
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response.choices[0].message['content']
        messages.append({"role": "assistant", "content": reply})
        display_user_message("You: " + message + "\n")
        root.after(500, display_bot_message, "Bot: " + reply + "\n")
        entry.delete(0, tk.END)

def display_user_message(message):
    chat_area.configure(state=tk.NORMAL)
    chat_area.insert(tk.END, message, "user")
    chat_area.configure(state=tk.DISABLED)

def display_bot_message(message):
    chat_area.configure(state=tk.NORMAL)
    chat_area.insert(tk.END, message, "assistant")
    chat_area.configure(state=tk.DISABLED)

# Configure tag styles for different roles
chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("assistant", foreground="green")

# Create a send button
send_button = Button(root, text="Send", command=send_message)
send_button.pack(fill=tk.BOTH, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
