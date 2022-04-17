from tkinter import *

# # Options menu
OPTIONS = ["Выберите напиток",
            "Вино: Старая келья, 12%",
            "Вино: Arta Vinia, 13.5%",
            "Вино: Кагор, 16%",
            "Пиво: Жигулевское, 3.8%",
            "Пиво: Corona Extra, 4.5%",
            "Пиво: Zatecky Gus, 4.6%",
            "Водка: Сваяк, 40%",
            "Водка: Налибоки, 40%",
            "Водка: Бульбашъ, 40%"]

dict_kk = {
    "Вино: Старая келья, 12%" : 85,
    "Вино: Arta Vinia, 13.5%" : 65,
    "Вино: Кагор, 16%" : 95,
    "Пиво: Жигулевское, 3.8%" : 37,
    "Пиво: Corona Extra, 4.5%" : 42,
    "Пиво: Zatecky Gus, 4.6%" : 41,
    "Водка: Сваяк, 40%" : 220,
    "Водка: Налибоки, 40%" : 220,
    "Водка: Бульбашъ, 40%" : 220
}

dict_bel = {
    "Вино: Старая келья, 12%" : 1.9,
    "Вино: Arta Vinia, 13.5%" : 1.5,
    "Вино: Кагор, 16%" : 2.5,
    "Пиво: Жигулевское, 3.8%" : 0.6,
    "Пиво: Corona Extra, 4.5%" : 0.3,
    "Пиво: Zatecky Gus, 4.6%" : 0,
    "Водка: Сваяк, 40%" : 0,
    "Водка: Налибоки, 40%" : 0,
    "Водка: Бульбашъ, 40%" : 0
}

dict_gir = {
    "Вино: Старая келья, 12%" : 0,
    "Вино: Arta Vinia, 13.5%" : 0,
    "Вино: Кагор, 16%" : 0,
    "Пиво: Жигулевское, 3.8%" : 0,
    "Пиво: Corona Extra, 4.5%" : 0,
    "Пиво: Zatecky Gus, 4.6%" : 0,
    "Водка: Сваяк, 40%" : 0,
    "Водка: Налибоки, 40%" : 0,
    "Водка: Бульбашъ, 40%" : 0
}

dict_ygl = {
    "Вино: Старая келья, 12%" : 6,
    "Вино: Arta Vinia, 13.5%" : 4,
    "Вино: Кагор, 16%" : 6,
    "Пиво: Жигулевское, 3.8%" : 4.8,
    "Пиво: Corona Extra, 4.5%" : 4,
    "Пиво: Zatecky Gus, 4.6%" : 3.6,
    "Водка: Сваяк, 40%" : 0,
    "Водка: Налибоки, 40%" : 0,
    "Водка: Бульбашъ, 40%" : 0
}

dict_krep = {
    "Вино: Старая келья, 12%" : 0.12,
    "Вино: Arta Vinia, 13.5%" : 0.135,
    "Вино: Кагор, 16%" : 0.16,
    "Пиво: Жигулевское, 3.8%" : 0.038,
    "Пиво: Corona Extra, 4.5%" : 0.045,
    "Пиво: Zatecky Gus, 4.6%" : 0.046,
    "Водка: Сваяк, 40%" : 0.4,
    "Водка: Налибоки, 40%" : 0.4,
    "Водка: Бульбашъ, 40%" : 0.4
}

# Функционал приложения
def button_raschet():
    new_window_1 = Toplevel(root)
    new_window_1.geometry("350x350")
    new_window_1.title("Расчет выпитого")

    name_u = name.get()
    alk_u = alk.get()
    masa = vees.get()
    isOption = inputopt.get()

    if name_u == "" and alk_u == "":
        label_function_1 = Label(new_window_1, text=f"Введите имя и количество выпитого!!!!")
        label_function_1.place(x=1, y=1)
    elif name_u == "":
        label_function_1 = Label(new_window_1, text=f"Введите имя !!!!")
        label_function_1.place(x=1, y=1)
    elif alk_u == "":
        label_function_1 = Label(new_window_1, text=f"Введите количество выпитого!!!!")
        label_function_1.place(x=1, y=1)
    else:
        label_function_1 = Label(new_window_1, text=f"{name_u}, вы выпили {alk_u} грамм {isOption}: ")
        label_function_1.place(x=1, y=1)
        k_kal = dict_kk[isOption]*int(alk_u)/100
        label_function_2 = Label(new_window_1, text=f"килакалории: {k_kal} ккал")
        label_function_2.place(x=20, y=20)
        k_bel = dict_bel[isOption] * int(alk_u)/100
        label_function_3 = Label(new_window_1, text=f"белки: {k_bel} г.")
        label_function_3.place(x=20, y=40)
        k_gir = dict_gir[isOption] * int(alk_u)/100
        label_function_4 = Label(new_window_1, text=f"жиры: {k_gir} г.")
        label_function_4.place(x=20, y=60)
        k_ygl = dict_ygl[isOption] * int(alk_u)/100
        label_function_5 = Label(new_window_1, text=f"углеводы: {k_ygl} г.")
        label_function_5.place(x=20, y=80)
        m_water = int(masa) * 0.7
        kol_vip = int(alk_u)*dict_krep[isOption]*0.79
        s_op_f = kol_vip/m_water
        s_op = round(s_op_f, 2)
        label_function_6 = Label(new_window_1, text=f"Ваша степень опьянения примерно: {s_op} промилле")
        label_function_6.place(x=20, y=120)

# Main window
root = Tk()
root.geometry("400x350")
root.title("Пей правильно")
root['bg'] = 'red3'
#
inputopt = StringVar()
inputopt.set(OPTIONS[0])
# # Widgets
inputmenu = OptionMenu(root, inputopt, *OPTIONS)
inputmenu.grid(row = 0, padx=5, pady=15)
inputmenu.config(font = "TimesNewRoman 10")

nam = Label(root, text = "Введите Ваше имя")
nam.grid(row = 1, column = 0,  pady = 1)
name = Entry(root, justify = "center", font = "bold")
name.grid(row = 2, column = 0, padx=100, ipady = 5)

agee = Label(root, text = "Введите Ваш возраст (в годах)")
agee.grid(row = 3, column = 0, pady = 1)
age = Entry(root, justify = "center", font = "bold")
age.grid(row = 4, column = 0, ipady = 5)

ves = Label(root, text = "Введите Ваш вес (в киллограмах)")
ves.grid(row = 5, column = 0, pady = 1)
vees = Entry(root, justify = "center", font = "bold")
vees.grid(row = 6, column = 0, ipady = 5)

alko = Label(root, text = "Укажите сколько выпили (в граммах)")
alko.grid(row = 7, column = 0, pady = 1)
alk = Entry(root, justify = "center", font = "bold")
alk.grid(row = 8, column = 0, ipady = 5)

okbtn = Button(root, text = "Рассчитать результат", bg='black', fg='white', command=button_raschet)
okbtn.grid(row = 9, column = 0, ipady = 10)

root.mainloop()