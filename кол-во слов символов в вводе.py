from tkinter import *


window = Tk()
window.geometry('500x300')
window.title('Подсчет слов и символов')


def count(*args):
    count = 0
    text = input.get("1.0", "end-1c")
    text = text.split()
    label_words.configure(text=f'Кол-во слов: {len(text)}')

    for symbol in text:
        count += len(symbol)
    label_symbols_1.configure(text=f'Кол-во символов без пробелов: {count}')



input = Text(window, width=40, height=10)
input.focus()
label_words = Label(window, text='Кол-во слов: ')
label_symbols_1 = Label(window, text='Кол-во символов без пробелов: ')
close = Button(window, text='Закрыть', command=lambda: window.destroy())
button = Button(window, text='Посчитать', command=count)

input.pack(side=TOP)
label_words.pack(side=TOP)
label_symbols_1.pack(side=TOP)
button.pack(side=TOP)
close.pack(side=RIGHT)

window.mainloop()


