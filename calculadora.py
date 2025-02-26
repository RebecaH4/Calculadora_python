#Create by
#Rebeca HdC

import tkinter as tk
from tkinter import ttk

x = 0
def suma():
    entry_num2["state"]=tk.NORMAL
    entry_num1["state"]=tk.DISABLED
    global x
    x = 0
    x = x + 1

def resta():
    entry_num2["state"]=tk.NORMAL
    entry_num1["state"]=tk.DISABLED
    global x
    x = 0
    x = x + 2

def multi():
    entry_num2["state"]=tk.NORMAL
    entry_num1["state"]=tk.DISABLED
    global x
    x = 0
    x = x + 3

def divi():
    entry_num2["state"]=tk.NORMAL
    entry_num1["state"]=tk.DISABLED
    global x
    x = 0
    x = x + 4

def igual():
    match x:
        case 1:
            num1=int(entry_num1.get())
            num2=int(entry_num2.get())
            resultado=num1+num2
            resul.insert(0, resultado) 
        case 2:
            num1=int(entry_num1.get())
            num2=int(entry_num2.get())
            resultado=num1-num2
            resul.insert(0, resultado)
        case 3:
            num1=int(entry_num1.get())
            num2=int(entry_num2.get())
            resultado=num1*num2
            resul.insert(0, resultado)
        case 4:
            num1=int(entry_num1.get())
            num2=int(entry_num2.get())
            resultado=num1/num2
            resul.insert(0, resultado)

def lim():

    entry_num2.delete(0, tk.END)
    entry_num2["state"]=tk.DISABLED
    entry_num1["state"]=tk.NORMAL
    entry_num1.delete(0, tk.END)
    resul.delete(0, tk.END)

def cerrar():
    cal.destroy()

def cero():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "0")
    largo2 = len(entry_num2.get())
    entry_num2.insert(largo2, "0")

def uno():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "1")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "1")

def dos():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "2")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "2")

def tres():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "3")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "3")

def cuatro():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "4")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "4")

def cinco():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "5")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "5")

def seis():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "6")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "6")

def siete():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "7")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "7")

def ocho():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "8")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "8")

def nueve():
    largo1 = len(entry_num1.get())
    entry_num1.insert(largo1, "9")
    largo2 = len(entry_num1.get())
    entry_num2.insert(largo2, "9")

cal = tk.Tk()
cal.title("Calculadora")
cal.configure(background="#FFF0F5")

label_num1=tk.Label(text="primer numero", background="#FFF0F5")
entry_num1=tk.Entry()
entry_num1.configure(background="#CDF0F2")

label_num2=tk.Label(text="segundo numero", background="#FFF0F5")
entry_num2=tk.Entry()
entry_num2.configure(background="#CDF0F2")
entry_num2["state"]=tk.DISABLED

label_resultado = tk.Label(text="Resultado", background="#FFF0F5")
resul=tk.Entry()
resul.configure(background="#DDEDEA")

button_suma=tk.Button(text="+", command=suma, background="#76D1D0")
button_resta=tk.Button(text="-", command=resta, background="#A2EBEB")
button_multi=tk.Button(text="*", command=multi, background="#CCEFF0")
button_divi=tk.Button(text="/", command=divi, background="#FBBDBC")
button_igual=tk.Button(text="=", command=igual, background="#FCDCDB")
button_limpiar=tk.Button(text="AC", command=lim, background="#FFF7F5")
button_cerrar=tk.Button(text="Salir",command=cerrar, background="#FDEEED")

button_0=tk.Button(text="0", command=cero, background="#F4A09F")
button_1=tk.Button(text="1", command=uno, background="#FBBCBB")
button_2=tk.Button(text="2", command=dos, background="#FDD6D4")
button_3=tk.Button(text="3", command=tres, background="#FDEEED")
button_4=tk.Button(text="4", command=cuatro, background="#FFF7F5")
button_5=tk.Button(text="5", command=cinco, background="#FFF7F5")
button_6=tk.Button(text="6", command=seis, background="#FDEEED")
button_7=tk.Button(text="7", command=siete, background="#FDD6D4")
button_8=tk.Button(text="8", command=ocho, background="#FBBCBB")
button_9=tk.Button(text="9", command=nueve, background="#F4A09F")

button_suma.place(x=265, y=15, width=35, height=30)
button_resta.place(x=265, y=50, width=35, height=30)
button_multi.place(x=265, y=85, width=35, height=30)
button_divi.place(x=265, y=120, width=35, height=30)
button_igual.place(x=265, y=155, width=35, height=30)
button_limpiar.place(x=265, y=190, width=35, height=30)
button_cerrar.place(x=265, y=225, width=35, height=35)

button_0.place(x=20, y=15, width=40, height=40)
button_1.place(x=65, y=15, width=40, height=40)
button_2.place(x=110, y=15, width=40, height=40)
button_3.place(x=155, y=15, width=40, height=40)
button_4.place(x=200, y=15, width=40, height=40)

button_5.place(x=20, y=60, width=40, height=40)
button_6.place(x=65, y=60, width=40, height=40)
button_7.place(x=110, y=60, width=40, height=40)
button_8.place(x=155, y=60, width=40, height=40)
button_9.place(x=200, y=60, width=40, height=40)

entry_num1.place(x=20, y=120, width=100, height=30)
label_num1.place(x=20, y=155)
entry_num2.place(x=150, y=120, width=100, height=30)
label_num2.place(x=150, y=155)

label_resultado.place(x=110, y=190)
resul.place(x=90, y=210, width=100, height=30)

cal.geometry("310x275")
cal.mainloop()
