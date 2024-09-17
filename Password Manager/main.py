import random
from tkinter import *
from tkinter import messagebox
import pyperclip

def copy():
    pyperclip.copy(password_entry)

def on_click():
    try:
        low = int(var1_entry.get())
        up = int(var2_entry.get())
        num = int(var3_entry.get())
        sym = int(var4_entry.get())
    except:
        messagebox.showinfo("Error", "Please enter the number")
    generate_password(low, up, num, sym)

def generate_password(include_lowercase, include_uppercase, include_numbers, include_symbols):
    password_entry.delete(0, END)
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}\\|;':\",./<>?"
    password = ""
    for i in range(include_lowercase):
        password += random.choice(lowercase)
    for i in range(include_uppercase):
        password += random.choice(uppercase)
    for i in range(include_numbers):
        password += random.choice(number)
    for i in range(include_symbols):
        password += random.choice(symbols)
    password1 = list(password)
    random.shuffle(password1)
    password = ''.join(password1)
    password_entry.insert(0, password)
    pyperclip.copy(password)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lower = Label(text='Include lowercase')
lower.grid(column=1, row=0)
upper = Label(text='Include uppercase')
upper.grid(column=1, row=1)
number = Label(text='Include numbers')
number.grid(column=1, row=2)
symbol = Label(text='Include symbols')
symbol.grid(column=1, row=3)

var1_entry = Entry(width=1)
var1_entry.grid(column=2, row=0)
var2_entry = Entry(width=1)
var2_entry.grid(column=2, row=1)
var3_entry = Entry(width=1)
var3_entry.grid(column=2, row=2)
var4_entry = Entry(width=1)
var4_entry.grid(column=2, row=3)

generate_password_btn = Button(text="Generate Password", command=on_click)
generate_password_btn.grid(column=2, row=5)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=5)

window.mainloop()