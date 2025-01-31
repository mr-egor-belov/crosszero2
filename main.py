import tkinter as tk
from tkinter import messagebox

# Создание главного окна
window = tk.Tk()
window.title("Крестики-нолики")  # Заголовок окна
window.geometry("300x350")  # Размер окна

current_player = "X"  # Текущий игрок ("X" или "0")
buttons = []  # Список кнопок игрового поля


# Функция для проверки победителя
def check_winner():
    # Проверка по строкам
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True

    # Проверка по столбцам
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Проверка по диагоналям
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


# Функция обработки нажатия на кнопку
def on_click(row, col):
    global current_player

    # Если клетка уже занята, ничего не делаем
    if buttons[row][col]['text'] != "":
        return

    # Устанавливаем символ текущего игрока в кнопку
    buttons[row][col]['text'] = current_player

    # Проверяем, выиграл ли текущий игрок
    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        return

    # Меняем игрока
    current_player = "0" if current_player == "X" else "X"


# Создание игрового поля (3x3 кнопки)
for i in range(3):
    row = []
    for j in range(3):
        # Создание кнопки с заданными параметрами шрифта, размера и обработчика нажатия
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)  # Размещение кнопки в сетке окна
        row.append(btn)
    buttons.append(row)  # Добавление строки кнопок в общий список

# Запуск главного цикла программы
window.mainloop()