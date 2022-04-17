from tkinter import *

unit_dict = {
    "см" : 0.01,
    "метры" : 1.0,
    "км": 1000.0,
    "мили": 1609.344,
    "дюймы": 0.0254,
    "граммы" : 1.0,
    "кг" : 1000.0,
    "центнеры": 100000.0,
    "тон" : 1000000.0,
    "фунты" : 453.592,
    "кв. м" : 1.0,
    "кв. км": 1000000.0,
    "ар" : 100.0,
    "гектар" : 10000.0,
    "акры": 4046.856,
    "кв. мили" : 2590000.0,
    "куб. см" : 0.001,
    "литр" : 1.0,
    "милилитры" : 0.001,
    "галон": 3.785
}

lengths = ["см", "метры", "км", "мили", "дюймы"]
weights = ["кг", "граммы", "центнеры", "тон", "фунты"]
temps = ["Цельсии", "Фаренгейт"]
areas = ["кв. м", "кв. км", "ар", "гектар", "акры", "кв. мили"]
volumes = ["куб. см", "литр", "милилитры", "галон"]


OPTIONS = ["сделайте выбор",
           "см",
           "метры",
           "км",
           "мили",
           "дюймы",
           "граммы",
           "кг",
           "центнеры",
           "тон",
           "фунты",
           "кв. м",
           "кв. км",
           "ар",
           "гектар",
           "акры",
           "кв. мили",
           "куб. см",
           "литр",
           "милилитры",
           "галон"]


root = Tk()
root.geometry("400x350")
root.title("Конвертер")
root['bg'] = 'blue violet'

def ok():
    inp = float(inputentry.get())
    inp_unit = inputopt.get()
    out_unit = outputopt.get()

    cons = [inp_unit in lengths and out_unit in lengths,
    inp_unit in weights and out_unit in weights,
    inp_unit in temps and out_unit in temps,
    inp_unit in areas and out_unit in areas,
    inp_unit in volumes and out_unit in volumes]

    if any(cons):
        if inp_unit == "Цельсии" and out_unit == "Фаренгейт":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp * 1.8) + 32)
        elif inp_unit == "Фаренгейт" and out_unit == "Цельсии":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp - 32) * (5/9))
        else:
            outputentry.delete(0, END)
            outputentry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))

    else:
        outputentry.delete(0, END)
        outputentry.insert(0, "ERROR")

inputopt = StringVar()
inputopt.set(OPTIONS[0])

outputopt = StringVar()
outputopt.set(OPTIONS[0])


inputlabel = Label(root, text = "Введите данные")
inputlabel.grid(row = 0, column = 0, pady = 20)

inputentry = Entry(root, justify = "center", font = "bold")
inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

inputmenu = OptionMenu(root, inputopt, *OPTIONS)
inputmenu.grid(row = 1, column = 1)
inputmenu.config(font = "Arial 10")

outputlabel = Label(root, text = "Вывод")
outputlabel.grid(row = 2, column = 0, pady = 20)

outputentry = Entry(root, justify = "center", font = "bold")
outputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)

outputmenu = OptionMenu(root, outputopt, *OPTIONS)
outputmenu.grid(row = 3, column = 1)
outputmenu.config(font = "Arial 10")

okbtn = Button(root, text = "OK", command = ok, padx = 80, pady = 2)
okbtn.grid(row = 4, column = 0, columnspan = 2, pady = 50)

root.mainloop()