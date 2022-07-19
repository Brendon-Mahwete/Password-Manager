from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    new_password = "".join(password_list)
    # for char in password_list:
    #    new_password += char

    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    my_dict = {
        website_entry.get(): {
            "Email": email_entry.get(),
            "Password": password_entry.get()}
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Don't leave any empty input.")
    else:
        try:
            with open("data.json", "r") as my_file:
                # Read old data
                data = json.load(my_file)

        except FileNotFoundError:
            with open("data.json", "w") as my_file:
                json.dump(my_dict, my_file, indent=4)
        else:
            with open("data.json", "w") as my_file:
                # Update old data ith new data
                data.update(my_dict)
                # Saving updated data with new data
                json.dump(data, my_file, indent=4)
        finally:
            website_entry.delete(0, END)
            website_entry.focus()
            password_entry.delete(0, END)


# ---------------------------- SEARCH WEBSITE NAME ------------------------------- #


def search():
    website_key = website_entry.get()

    try:
        with open("data.json", "r") as my_file:
            data = json.load(my_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        with open("data.json", "r") as my_file:
            data = json.load(my_file)
            count = 0
            if website_key in data:
                messagebox.showinfo(title="Info", message=f"Email: {data[website_key]['Email']}\nPassword: "
                                                          f"{data[website_key]['Password']}")
            else:
                messagebox.showerror(title="Error", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

# Creating the window with the Tk class
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Creating the labels
website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "bren@gmail.com")  # The default email.

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Creating Buttons
password_button = Button(text="Generate Password", command=generate)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW")

# Creating the image holder with the PhotoImage Class
lock_image = PhotoImage(file="logo.png")

# Then the image holder will be linked to the canvas
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

window.mainloop()
