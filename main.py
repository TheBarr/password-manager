from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
user_data_label = Label(text="Email/Username:")
user_data_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
user_entry = Entry(width=50)
user_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", width=14)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=43)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
