#2
from tkinter import *
from tkinter import ttk


def imt(*args):
    try:
        kg = float(weight_imt.get())
        m = float(height_imt.get())
        imt_intermediate = kg / m ** 2
        ind.set(imt_intermediate)

        if imt_intermediate <= 16:
            interpretation.set("Выраженный дефицит массы тела")
        elif 16 < imt_intermediate <= 18.5:
            interpretation.set("Недостаточная (дефицит) масса тела")
        elif 18.5 < imt_intermediate <= 25:
            interpretation.set("Норма")
        elif 25 < imt_intermediate <= 30:
            interpretation.set("Избыточная масса тела (предожирение)")
        elif 30 < imt_intermediate <= 35:
            interpretation.set("Ожирение 1 степени")
        elif 35 < imt_intermediate <= 40:
            interpretation.set("Ожирение 2 степени")
        else:
            interpretation.set("Ожирение 3 степени")
    except ZeroDivisionError:
        ind.set("Ошибка!")


root = Tk()
root.title("Рассчет ИМТ")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

weight_imt = StringVar()
weight_imt_entry = ttk.Entry(mainframe, width=7, textvariable=weight_imt)
weight_imt_entry.grid(column=2, row=1, sticky=(W, E))

height_imt = StringVar()
height_imt_entry = ttk.Entry(mainframe, width=7, textvariable=height_imt)
height_imt_entry.grid(column=2, row=2, sticky=(W, E))

ind = StringVar()
ttk.Label(mainframe, textvariable=ind).grid(column=2, row=3, sticky=(W, E))

interpretation = StringVar()
ttk.Label(mainframe, textvariable=interpretation).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Рассчитать", command=imt).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Масса (в кг)").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Рост (в м)").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="ИМТ").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Соответствие: ").grid(column=1, row=4, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

weight_imt_entry.focus()
root.bind("<Return>", imt)
root.mainloop()

