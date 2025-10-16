#4
from tkinter import *
from tkinter import ttk

def color_selection(*args):
        color = str(color_input.get())
        s1 = hex(255 - int(color[1:3], 16))[2:].zfill(2)
        s2 = hex(255 - int(color[3:5], 16))[2:].zfill(2)
        s3 = hex(255 - int(color[5:7], 16))[2:].zfill(2)
        answer.set('#'  + str(s1) + str(s2) + str(s3))
        color_display(color, '#'  + str(s1) + str(s2) + str(s3))

def color_display(color_before, color_after):
    color_display_input.config(background=color_before)
    color_display_answer.config(background=color_after)


root = Tk()
root.title("Подбор комплементарного цвета")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


color_input = StringVar()
color_input_entry = ttk.Entry(mainframe, width=7, textvariable=color_input)
color_input_entry.grid(column=2, row=1, sticky=(W, E))
color_display_input = Frame(mainframe, width=50, height=25, relief=SUNKEN, borderwidth=1)
color_display_input.grid(column=3, row=1, padx=5, sticky=(W, E))


answer = StringVar()
ttk.Label(mainframe, textvariable=answer).grid(column=2, row=2, sticky=(W, E))
color_display_answer = Frame(mainframe, width=50, height=25, relief='sunken', borderwidth=1)
color_display_answer.grid(column=3, row=2, padx=5, sticky=(W, E))


ttk.Button(mainframe, text="Найти", command=color_selection).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Исходный цвет:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Комплементарный цвет:").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
     child.grid_configure(padx=5, pady=5)

color_input_entry.focus()
root.bind("<Return>", color_selection)
root.mainloop()