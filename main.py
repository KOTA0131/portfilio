from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)


    pass_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_data = {website_entry.get(): {
        "email": email_entry.get(),
        "password": pass_entry.get()
    }}
    if len(website_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)


            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
                data.update(new_data)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

def search():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            web = website_entry.get()

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white")
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=1, row=0)





website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=27)
website_entry.grid(column=1, row=1)




email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "huangdaxishi@gmail.com")




pass_label = Label(text="Password:", bg="white")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=27)
pass_entry.grid(column=1, row=3)




generate_button = Button(text="Generate Password", bg="white", command=generate_pass)
generate_button.grid(column=2, row=3)




add_button = Button(text="Add", bg="white", width=38, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", bg="white", command=search)
search_button.grid(column=2, row=1)

window.mainloop()
