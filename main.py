from re import findall
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for a in range(randint(8, 10))]
    password_number = [choice(numbers) for b in range(randint(2, 4))]
    password_symbol = [choice(symbols) for c in range(randint(2, 4))]

    password_list = password_symbol + password_number + password_letter
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = webisite_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OI Stop Joking!!", message="Fill all the fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Reading old data
                data = json.dump(new_data,data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            webisite_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)

# ---------------------------- Search Bar ------------------------------- #

def search():
    website = webisite_entry.get()
    try:
        with open("data.json", "r") as store:
            data = json.load(store)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Found the Website", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="not found 420", message=f"{website} is not found in data, lol")

        # for _ in store:
        #     if website == data:
        #         print(data)
        #     else:
        #         save()

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=150, pady=150)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels...

webiste_labels = Label(text="Website :|  ")
webiste_labels.grid(row=1, column=0)
email_label = Label(text="Email/UserID :(  ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password :)  ")
password_label.grid(row=3, column=0)

#Entries...

webisite_entry = Entry(width=25)
webisite_entry.grid(row=1, column=1)
webisite_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

#Buttons...

generate_button = Button(text="Create Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="       Search       ", command=search)
search_button.grid(row=1, column=2)

windows.mainloop()