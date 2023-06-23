import string
import random
from tkinter import *
import pyperclip


root = Tk()
root.geometry("400x600")
root.title("Random password generator")

output_pass = StringVar()

all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]


def randPassGen():
    password = ""
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)
        password = password + random.choice(char_type)

    output_pass.set(password)

def copyPass():
    pyperclip.copy(output_pass.get())


# heading
pass_head = Label(root, text='Password Length', font='arial 12 bold').pack(pady=10)

# pass_length box
pass_len = IntVar()
length = Spinbox(root, from_=5, to_=20, textvariable=pass_len, width=24, font='arial 16').pack()

# button to generate pass
Button(root, command=randPassGen, text="Generate Password", font="Arial 10", bg='black', fg='white',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

# generated_pass_output
pass_label = Label(root, text='Random Generated Password', font='arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=output_pass, width=24, font='arial 16').pack()

# Copy to clipboard button

Button(root, text='Copy to Clipboard', command=copyPass, font="Arial 10", bg='black', fg='white',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

root.mainloop()  # to bundle pack the code for tkinter