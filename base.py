from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import Menu

def clicked():
    res = txt.get()
    lbl.configure(text=f'Дурачок ты, {res}')


window = Tk()
window.title("Без дураков")
window.geometry('900x500')  #задать размер окна

lbl = Label(window,text='Здаров', font=('', 20))
lbl.grid(column=0, row=0)

btn = Button(window, text='Кто нажал, тот дурак', bg='red', fg='green', command=clicked, padx=7, pady=10)
btn.grid(column=1, row=1)

close = Button(window, text='Закрыть окно', command=lambda: window.destroy(), padx=5, pady=10)
close.grid(column=1, row=17)

txt = Entry(window, width=15, bg='green', fg='black')
txt.grid(column=0, row=1)
txt.focus()

combo = Combobox(window, postcommand=list)
combo['values'] = (1,2,3,'четыре', 'five' )
#combo.current(0)   по умолчанию
combo.grid(column=3, row=5)

def get_combobox(combo):
    val = combo.get()
    messagebox.askyesnocancel('Selection', val)

spisok_button = Button(window, command= lambda: get_combobox(combo), text="выпадающий список")
spisok_button.grid(column=3, row=6)


chk_state = BooleanVar()
chk_state.set(False)
check = Checkbutton(window, text="Дурак", variable=chk_state, onvalue=1, offvalue=0 )
check.grid(column=1, row=6)

lbl_2 = Label(window,text='Выбор', font=('', 20))
lbl_2.grid(column=1, row=7)

def upd(*args ):
    boolean = chk_state.get()
    if boolean == False:
        lbl_2.configure(text=f'Ты не Дурак')
    else:
        lbl_2.configure(text=f'Ты Дурак')

chk_state.trace('w', upd)


#Radio_buttons
def radio_output_func(*args):
    radio_output.configure(text=selected.get())

selected = StringVar()

radio_button_1 = Radiobutton(window, text='Дурак', variable=selected, value='Дурак')
radio_button_2 = Radiobutton(window, text='Дурачок', variable=selected, value='Дурачок')
radio_button_3 = Radiobutton(window, text='Дурында', variable=selected, value='Дурында')
radio_button_1.grid(column=0, row=11)
radio_button_2.grid(column=1, row=11)
radio_button_3.grid(column=2, row=11)
radio_button = Button(window, text='жмакай', font=('', 20), command=radio_output_func)
radio_button.grid(column=3, row=11)
radio_output = Label(window, text='', font=('', 15))
radio_output.grid(column=1, row=12)

#Скроллинг текста
scroll = scrolledtext.ScrolledText(window, width=40, height=10)
scroll.insert(INSERT, 'Текстовое поле \n'*100)
scroll.grid(column=0, row=10)


var = IntVar()
var.set(1)
spin = Spinbox(window, from_=0, to=10, width=5, textvariable=var) #spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0, row=15)


bar = Progressbar(window, length=200)
bar['value'] = 70
bar.grid(column=0, row=18)

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)


window.mainloop()


