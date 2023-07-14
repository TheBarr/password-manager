from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Website or Password is empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                               message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", 'a') as f:
                f.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "name@mail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", width=14)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
