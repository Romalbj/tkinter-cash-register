from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import scrolledtext


global total

total = 0

global total_for_file

total_for_file = 0

global count
count = 0

global all_orders_total

all_orders_total = 0

global history_of_orders_str

history_of_orders_str = ''




window = Tk()
window.title('Заказ фруктов')
window.geometry('600x400')




tab_control = ttk.Notebook(window)
tab_control.pack(expand=True, fill=BOTH)

#Делаю вкладки
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab1.pack(fill=BOTH, expand=True)
tab2.pack(fill=BOTH, expand=True)

tab_control.add(tab1, text='Текущий заказ')
tab_control.add(tab2, text='История заказов')

#вкладка заказы
scroll = scrolledtext.ScrolledText(tab2)
scroll.pack(side=TOP)

label_all_orders_total = Label(tab2)
label_all_orders_total.pack(side=TOP)



products = {
    "Яблоки": 70,
    "Персики": 150,
    "Огурцы": 100,
    "Помидоры": 120
}


order = dict()
history_of_orders = dict()


list_of_products = ttk.Combobox(tab1)
list_of_products['values'] = tuple(products.keys())

amount = Entry(tab1, width=10, bg='white', fg='black')
promo = Entry(tab1, width=10, bg='white', fg='black')


label_pr = Label(tab1, text='Продукт')
label_am = Label(tab1, text='Кол-во кг')
label_order = Label(tab1)
label_total = Label(tab1)
label_promo = Label(tab1, text='\n' + 'Введите промокод:')
label_itogo = Label(tab1, text='Итого:')
label_discount = Label(tab1)


def get_product(*args):

    global total
    global count

    #Добавляем продукты в словарь order

    if list_of_products.get() in order.keys():

        order[list_of_products.get()][0] = round(order[list_of_products.get()][0] + float(amount.get()), 2)
        order[list_of_products.get()][1] = round(order[list_of_products.get()][1] + float(amount.get())*products[list_of_products.get()], 2)
    else:
        order[list_of_products.get()] = (str(round(float(amount.get()), 2)) + ' ' + str(round(float(amount.get()), 2)*products[list_of_products.get()]))
        order[list_of_products.get()] = order[list_of_products.get()].split()
        order[list_of_products.get()][0] = float(order[list_of_products.get()][0])
        order[list_of_products.get()][1] = float(order[list_of_products.get()][1])
        #чтобы не было бесконечной дроби
        order[list_of_products.get()][1] = float('%.1f' % (order[list_of_products.get()][1]))

 #  print(order)

    #обнулить значения
    list_of_products.set('')
    amount.delete(0, END)

    global order_str

    order_str = ''

    total = 0

    #вывод "итого" и "заказ"

    for k,v in order.items():

        total += (v[1])
        label_total.configure(text=str(total)+' руб.', font=('', 15))

        order_str += str(k) + ' ' + str(v[0]) + 'кг ' + str(v[1]) + ' руб.' + '\n'
    label_order.configure(text=(order_str), font=('', 15))


def show_order(*args):

    global order_str
    global all_orders_total
    global count
    global total
    global total_for_file
    global history_of_orders_str

  # удалить все виджеты
  #  for widget in window.winfo_children():
   #     widget.destroy()

    #Вспывающее окно подтверждения заказа
    messagebox.askyesnocancel('Подтверждение покупки', str('Итого: ' + str(total) + ' руб.'))
    count += 1

    #Очистка всех надписей
    label_order.configure(text='')
    label_total.configure(text='')
    label_discount.configure(text='')
    promo.delete(0, END)


    all_orders_total += total

    #Создание списка с историей заказов
    history_of_orders[f'{count} заказ'] = order_str


    #Вывод истории операций на второй вкладке
    for k,v in history_of_orders.items():
        history_of_orders_str = f'\n{k}:\n\n{v} \nИтого с учетом скидки: {total} руб.\n\n'

    scroll.insert(INSERT, history_of_orders_str)
    label_all_orders_total.configure(text=f'Общий доход {all_orders_total} руб.')

    total_for_file = total

    #обнуляем итого и словарь order
    total = 0
    order.clear()


def confirm_promo(*args):
    global total

    before_promo = total

    if promo.get() == 'скидка 20':
        total = round(float(total) * 0.8, 2)
        label_total.configure(text=f'{total} руб.', font=('', 15))
        label_discount.configure(text=f'Скидка составила: \n\n {round((before_promo-total),2)} руб.')


def save_history_of_operations(*args):

    history_of_orders_for_save = ''

    for k,v in history_of_orders.items():
        history_of_orders_for_save += f'\n{k}:\n\n{v} \nИтого с учетом скидки: {total_for_file} руб.\n\n'


    print(history_of_orders_for_save)

    history_of_operations_file = open('Operations.txt', 'w+')
    history_of_operations_file.write(str(history_of_orders_for_save))
    history_of_operations_file.close()


#создаю кнопки
confirm = Button(tab1, text='Добавить', command=get_product)
finish_order = Button(tab1, text='Завершить заказ', command=show_order)
promo_button = Button(tab1, text='Применить промокод', command=confirm_promo)


#добавляю пункты и подпункты меню
main_menu = Menu(window)
window.configure(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Сохранить историю операций', command=save_history_of_operations)
main_menu.add_cascade(label='Файл', menu=file_menu)

#размещаю все виджеты в окне
label_pr.grid(column=0, row=0)
label_am.grid(column=1, row=0)
list_of_products.grid(column=0, row=1)
amount.grid(column=1, row=1)
confirm.grid(column=1, row=4)
label_promo.grid(column=1, row=5)
promo.grid(column=1, row=6)
promo_button.grid(column=1, row=7)
label_order.grid(column=0, row=8)
finish_order.grid(column=2, row=4)
label_itogo.grid(column=2, row=5)
label_total.grid(column=2, row=6)
label_discount.grid(column=2, row=8)


window.mainloop()

