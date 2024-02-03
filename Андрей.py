from tkinter import *
import random


def re_plc(event):
    x = random.random()
    y = random.random()
    if x < 0.1:
        x += 0.1
    elif x > 0.9:
        x -= 0.1
    if y < 0.1:
        y += 0.1
    elif y > 0.9:
        y -= 0.1
    btn.place(relx=x, rely=y)


root = Tk()
root.geometry("500x500")

niga = Label(text="Негры люди?")
niga.place(relx=0.4, rely=0.43)

btn = Button(text="Да", width=4)
btn.place(relx=0.5, rely=0.5)
btn.bind("<Button-1>", re_plc)
btn.bind("<Enter>", re_plc)

btn2 = Button(text="Нет", width=4)
btn2.place(relx=0.35, rely=0.5)

root.mainloop()
