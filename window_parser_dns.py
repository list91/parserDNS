import os
from tkinter import *
import app
root = Tk()
root.title ("Парсер DNS")
root.iconbitmap('services_dns_icon_216293.ico')

def script():
    #os.system('app.py')
    app.script_pars(message_link.get(),spin_age.get())
    os.system('test.txt')
    #messagebox.showinfo("www", message.get())
    #print(message_link.get())
    return

message_link = StringVar()
spin_age=StringVar()

Label(text="Введите ссылку категории товаров и укажите количество \
страниц\n(например ссылку на раздел 'Электрочайники')")\
		.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E, pady=10, 
			padx=150)

Entry(width=90, textvariable=message_link)\
    .grid(row=1, column=0, columnspan=2, padx=10)


Spinbox(width=5, from_=1, to=50, textvariable=spin_age)\
    .grid(row=1, column=2, sticky=W, padx=10)

Button(text="Пуск", width=10, height=2,command=script).grid(row=2, column=1, \
	sticky=W+E, pady=30, padx=150)
root.mainloop()
