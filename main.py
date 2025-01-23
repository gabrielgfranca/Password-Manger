from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import os


FONT = ("Arial", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)

    else:
        password_entry.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE INFORMATION ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Please, don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The are the details entered: \n\nEmail or Username: {email_username} \n"
                                                      f"Password: {password}\n\nIs it ok to save?")
        if is_ok:
            with open("PasswordManager.txt", "a") as data:
                data.write(f"Website: {website}\n")
                data.write(f"Email/Username: {email_username}\n")
                data.write(f"Password: {password}\n")
                data.write("-" * 20 + "\n")

            os.startfile("PasswordManager.txt")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Window Config
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Canvas Config
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0, columnspan=2, sticky="ew")


# Label Config
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1, sticky="e")

email_username_label = Label(text="Email/Username:", font=FONT)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky="e")


# Entry Config
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w") # Aligned to left
website_entry.focus()

email_username_entry = Entry(width=43)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w") # Aligned to left

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w") # Aligned to left


# Buttons Config
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=1, row=3, columnspan=3, sticky="e")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()
