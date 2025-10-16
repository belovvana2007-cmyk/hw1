#6
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

selected_file = False

#график

def select_file():
    global file
    file = filedialog.askopenfilename()

def MNK(*args):
    global file
    df = pd.read_csv(file)
    x = list(df['x'])
    y = list(df['y'])

    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, color = 'blue', label = 'Исходные точки')

    mnk = np.polyfit(x, y, 1)
    z = np.poly1d(mnk)
    plt.plot(x, z(x), 'r-', linewidth = 2, label = f'Уравнение прямой: y = {mnk[0]:.4f}*x {mnk[1]:.4f}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.title('y(x)')
    plt.tight_layout()
    plt.legend()
    plt.show()

#интерфейс

root = Tk()

icon = PhotoImage(file = "C:/Users/User/Downloads/heart1.png")
root.iconphoto(False, icon)

root.title('Создание графика МНК')
root.geometry("700x300")
mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text = "Программа для построения графика МНК по входным данным", font = ("Arial", 16, "bold")).grid(column=0, row=0, pady=40)
ttk.Button(mainframe, text="Выбрать файл", command=select_file, width = 20).grid(column=0, row=1, pady=20)
ttk.Button(mainframe, text="Построить график", command=MNK, width = 20).grid(column=0, row=2, pady=10)

root.resizable(False, False) 
root.maxsize(960, 1080) 
root.mainloop()