import random
import string
import tkinter as tk

window = tk.Tk()
window.geometry("350x325")
window.title("Random Password Genrator")

frame = tk.Frame(master = window, width=300, height=225, bg = "purple")
frame.pack(pady=10)

up = tk.IntVar()
low = tk.IntVar()
dig = tk.IntVar()
sym = tk.IntVar()

uc = tk.Label(master = frame, text = "Uppercase")
uc.place(x = 10, y = 25)
entry1 = tk.Spinbox(master = frame, from_= 1, to_ = 5, width=5, textvariable=up)
entry1.place(x = 120, y = 25)

lc = tk.Label(master = frame, text = "Lowercase")
lc.place(x = 10, y = 75)
entry2 = tk.Spinbox(master = frame,from_= 1, to_ = 5, width=5, textvariable=low)
entry2.place(x = 120, y = 75)

dg = tk.Label(master = frame, text = "Digits")
dg.place(x = 10, y = 125)
entry3 = tk.Spinbox(master = frame,from_= 1, to_ = 5, width=5, textvariable=dig)
entry3.place(x = 120, y = 125)

pn = tk.Label(master = frame, text = "Punctuations")
pn.place(x = 10, y = 175)
entry4 = tk.Spinbox(master = frame,from_= 1, to_ = 5, width=5, textvariable=sym)
entry4.place(x = 120, y = 175)

def generate():
    upper = random.sample(string.ascii_uppercase, up.get())
    lower = random.sample(string.ascii_lowercase, low.get())
    digits = random.sample(string.digits, dig.get())
    symbols = random.sample(string.punctuation, sym.get())

    total = upper + lower + digits + symbols
    total = random.sample(total, len(total))
    total = "".join(total) 
    psw.config(text = "Password : " +total)


button = tk.Button(text = "Generate", command=generate)
button.pack(pady=5)

psw = tk.Label()
psw.pack(pady=5)

window.mainloop()