import pyperclip
import random
from tkinter import *
from tkinter import messagebox
import json
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers ) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    password_display.delete(0,END)
    password_display.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():

    website = website_entry.get()
    email = email_entry.get()
    password = password_display.get()
    new_data =        {
            website:
                   {
                       "email": email,
                       "password": password
                   }
    }
    #using message boxes to display a message
    if len(website)==0 or len(email) == 0 or len(password)==0:
        messagebox.showerror(title="OOPS",message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail : {email}"
                                                 f"\nPassword : {password}\nIs it ok to save?")
        if is_ok:
            with open("data.json", "r") as p_file:
                # json.dump(new_data,p_file,indent =4)
                data = json.load(p_file)
                print(data)
                website_entry.delete(0, END)
                password_display.delete(0, END)

    #writing to the file


# ---------------------------- UI SETUP ------------------------------- #

#window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#canvas setup
canvas = Canvas(width=200,height=200,highlightthickness=0)
pass_logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_logo)
canvas.grid(row=0,column=1)

#website label setup
website_label = Label(text="Website :",fg = "black",font= (FONT_NAME,10,"bold"))
website_label.grid(row=1,column=0)

#email_username label setup
email_username_label = Label(text="Email/Username :",fg = "black",font= (FONT_NAME,10,"bold"))
email_username_label.grid(row=2,column=0)

#password username label setup
password_label = Label(text="Password :",fg = "black",font= (FONT_NAME,10,"bold"))
password_label.grid(row=3,column=0)

#website entry setup
website_entry = Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

#email/username entry setup
email_entry = Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"yashpalravikumar1999@gmail.com")

#password display setup
password_display = Entry(width=33)
password_display.grid(row=3,column=1)

#generate button setup
generate_button = Button(text= "Generate",width=13,command=password_generate)
generate_button.grid(row=3,column=2)

#add button setup
add_button = Button(text="Add",width = 35,command=save_to_file)
add_button.grid(row=4,column = 1,columnspan =2)




#mainloop
window.mainloop()
