import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("crosszero")
window.geometry("300x350")

current_player = "X"
buttons = []

def check_winner():
   for i in range(3):
       if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
           return True
       if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
           return True

   if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
       return True
   if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
       return True

   return False


def on_click(row, col):
   global current_player

   if buttons[row][col]['text'] != "":
       return

   buttons[row][col]['text'] = current_player

   if check_winner():
       messagebox.showinfo("Игра окончена",f"Игрок {current_player} победил!")

   current_player = "0" if current_player == "X" else "X"


for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
       btn.grid(row=i, column=j)
       row.append(btn)
   buttons.append(row)

# Создание главного окна
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("300x400")

current_player = "X"  # Текущий игрок
buttons = []  # Список кнопок игрового поля

# Счетчики побед и ничьих
score_x = 0
score_o = 0
score_draw = 0  # Счетчик ничьих
winning_score = 3  # Сколько побед нужно для завершения игры

# Метка для отображения счета
score_label = tk.Label(window, text=f"X: {score_x} | O: {score_o} | Draws: {score_draw}", font=("Arial", 14))
score_label.grid(row=3, column=0, columnspan=3)

# Метка для отображения текущего игрока
player_label = tk.Label(window, text=f"Current Player: {current_player}", font=("Arial", 14))
player_label.grid(row=4, column=0, columnspan=3)


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
    global current_player, score_x, score_o, score_draw

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player
    buttons[row][col]['fg'] = "blue" if current_player == "X" else "red"

    if check_winner():
        if current_player == "X":
            score_x += 1
        else:
            score_o += 1
        score_label.config(text=f"X: {score_x} | O: {score_o} | Draws: {score_draw}")

        # Проверяем, достиг ли кто-то 3 побед
        if score_x == winning_score or score_o == winning_score:
            messagebox.showinfo("Game Over",
                                f"Player {current_player} wins the series!\nFinal Score:\nX: {score_x} | O: {score_o} | Draws: {score_draw}")
            disable_board()
            return

        messagebox.showinfo("Game Over",
                            f"Player {current_player} wins this round!\n\nScore:\nX: {score_x} | O: {score_o} | Draws: {score_draw}")
        reset_board()
        return

    # Проверка на ничью
    if all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
        score_draw += 1  # Увеличиваем счетчик ничьих
        score_label.config(text=f"X: {score_x} | O: {score_o} | Draws: {score_draw}")
        messagebox.showinfo("Game Over", f"Draw!\n\nScore:\nX: {score_x} | O: {score_o} | Draws: {score_draw}")
        reset_board()
        return

    # Смена игрока
    current_player = "O" if current_player == "X" else "X"
    player_label.config(text=f"Current Player: {current_player}")


# Функция для очистки игрового поля (без сброса счета)
def reset_board():
    global current_player
    current_player = "X"
    player_label.config(text=f"Current Player: {current_player}")
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["fg"] = "black"
    enable_board()


# Функция для полной перезагрузки игры (с обнулением счета)
def reset_game():
    global score_x, score_o, score_draw
    score_x = 0
    score_o = 0
    score_draw = 0  # Сбрасываем счетчик ничьих
    score_label.config(text=f"X: {score_x} | O: {score_o} | Draws: {score_draw}")
    reset_board()


# Функция для блокировки игрового поля после победы в серии
def disable_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["state"] = "disabled"


# Функция для разблокировки игрового поля при новом раунде
def enable_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["state"] = "normal"


# Функция для выбора символа (X или O)
def choose_symbol():
    def select_x():
        global current_player
        current_player = "X"
        player_label.config(text=f"Current Player: {current_player}")
        selection_window.destroy()

    def select_o():
        global current_player
        current_player = "O"
        player_label.config(text=f"Current Player: {current_player}")
        selection_window.destroy()

    selection_window = tk.Toplevel(window)
    selection_window.title("Choose Symbol")
    selection_window.geometry("200x100")
    tk.Label(selection_window, text="Choose your symbol:", font=("Arial", 12)).pack(pady=10)
    tk.Button(selection_window, text="X", font=("Arial", 14), command=select_x).pack(side=tk.LEFT, padx=20)
    tk.Button(selection_window, text="O", font=("Arial", 14), command=select_o).pack(side=tk.RIGHT, padx=20)


# Создание игрового поля (3x3 кнопки)
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Кнопка полного сброса (обнуляет и счет)
reset_button = tk.Button(window, text="Reset Game", font=("Arial", 14), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3, pady=10)

# Вызов выбора символа при старте
window.after(100, choose_symbol)

# Запуск главного цикла программы
window.mainloop()