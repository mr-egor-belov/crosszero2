import tkinter as tk
from tkinter import messagebox

# Создание главного окна
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("300x400")

current_player = "X"  # Текущий игрок
buttons = []  # Список кнопок игрового поля

# Счетчики побед
score_x = 0
score_o = 0

# Метка для отображения счета
score_label = tk.Label(window, text=f"X: {score_x} | O: {score_o}", font=("Arial", 14))
score_label.grid(row=3, column=0, columnspan=3)

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
    global current_player, score_x, score_o

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        if current_player == "X":
            score_x += 1
        else:
            score_o += 1
        score_label.config(text=f"X: {score_x} | O: {score_o}")
        messagebox.showinfo("Game Over", f"Player {current_player} wins!\n\nScore:\nX: {score_x} | O: {score_o}")
        reset_board()
        return

    # Проверка на ничью
    if all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", f"Draw!\n\nScore:\nX: {score_x} | O: {score_o}")
        reset_board()
        return

    # Смена игрока
    current_player = "O" if current_player == "X" else "X"

# Функция для очистки игрового поля (без сброса счета)
def reset_board():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# Функция для полной перезагрузки игры (с обнулением счета)
def reset_game():
    global score_x, score_o
    score_x = 0
    score_o = 0
    score_label.config(text=f"X: {score_x} | O: {score_o}")
    reset_board()

# Создание игрового поля (3x3 кнопки)
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Кнопка полного (обнуляет и счет)
reset_button = tk.Button(window, text="Reset Game", font=("Arial", 14), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3)

# Запуск главного цикла программы :)
window.mainloop()
