from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('500x300')
window.title('Оценка работы сервиса')

val = IntVar

close = Button(window, text='Закрыть', command=lambda: window.destroy())

def get_value(*args):
    label.configure(text=f'Ваша оценка: {int(scale.get())}')

scale = ttk.Scale(window, orient=HORIZONTAL, length=150, from_=0, to=100, command=get_value, variable=val)
label = Label(window, text='Ваша оценка: ')

label.pack(side=TOP)
scale.pack(side=TOP)
close.pack(side=RIGHT)

window.mainloop()
