from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = calculation.get()
        answer.set(str(eval(value)))
        
    except ZeroDivisionError:
        answer.set("Ошибка!")

root = Tk()
root.title("Калькулятор")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


calculation = StringVar()
calculation_entry = ttk.Entry(mainframe, width=7, textvariable=calculation)
calculation_entry.grid(column=2, row=1, sticky=(W, E))

answer = StringVar()
ttk.Label(mainframe, textvariable=answer).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Вычислить", command=calculate).grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="Выражение:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Ответ:").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

calculation_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()

