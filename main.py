from tkinter import *
from tkinter import messagebox as mb

def drinki():
    from subprocess import call
    call(["python", "drink.py"])

def converter():
    from subprocess import call
    call(["python", "Converter.py"])

def kalk():
    from subprocess import call
    call(["python", "kalk.py"])

def knb():
    from subprocess import call
    call(["python", "KNB.py"])

def zm():
    from subprocess import call
    call(["python", "zmeika.py"])

def kn():
    from subprocess import call
    call(["python", "krnol.py"])

def exit():
    choice = mb.askyesno("Выход", "Вы действительно хотите выйти?")
    if choice:
        root.destroy()

def spravka():
    new_window_1 = Toplevel(root)
    new_window_1.geometry("450x150")
    new_window_1.title("Справка")
    label_function_1 = Label(new_window_1, text="Это приложение было придумано как итоговый проект за курс PYTHON.")
    label_function_1.place(x=20, y=20)
    label_function_2 = Label(new_window_1, text="Осипчик Максим")
    label_function_2.place(x=20, y=40)



root = Tk()
root.geometry("400x350")
root.title("Выбор приложения")
root['bg'] = 'gray50'
mainmenu = Menu(root)
root.config(menu=mainmenu)

game = Label(root, text = "Выбор игр")
game.grid(row=0, column=0, padx=10, pady=10)
okbtn = Button(root, text = "Камень, ножницы, бумага", bg='black', fg='white', command= knb)
okbtn.grid(row=1, column=0, padx=10, pady=10)
okbtn = Button(root, text = "Змейка", bg='black', fg='white', command= zm)
okbtn.grid(row=2, column=0, padx=10, pady=10)
okbtn = Button(root, text = "Kрестики нолики", bg='black', fg='white', command= kn)
okbtn.grid(row=3, column=0, padx=10, pady=10)
pril = Label(root, text = "Выбор приложений")
pril.grid(row=0, column=1, padx=10, pady=10)
okbtn = Button(root, text = "Пей правильно", bg='black', fg='white', command= drinki)
okbtn.grid(row=1, column=1, padx=10, pady=10)
okbtn = Button(root, text = "Конвертер", bg='black', fg='white', command= converter)
okbtn.grid(row=2, column=1, padx=10, pady=10)
okbtn = Button(root, text = "Калькулятор", bg='black', fg='white', command= kalk)
okbtn.grid(row=3, column=1, padx=10, pady=10)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Выход", command=exit)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="О программе", command=spravka)

mainmenu.add_cascade(label="Файл",
                     menu=filemenu)
mainmenu.add_cascade(label="Справка",
                     menu=helpmenu)
root.mainloop()