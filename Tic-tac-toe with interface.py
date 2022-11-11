from tkinter import *
from tkinter import messagebox

# Окно для программы
window = Tk()
window.title('Крестики нолики')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
# середина экрана
w = w // 2 - 300
h = h // 2 - 300
window.geometry(f'500x552+{w}+{h}')
window.resizable(0, 0)
gamer = 'X'
game_run = True
grid = []
count = 0


# Обработка нажатия кнопок
def new_game():
    for x in range(3):
        for y in range(3):
            grid[x][y]['text'] = ' '
            grid[x][y]['background'] = 'lavender'
    global game_run
    game_run = True
    global count
    count = 0


def after_pressing(x, y):
    global gamer
    global count
    if game_run and grid[x][y]['text'] == ' ' and gamer == 'X':
        grid[x][y]['text'] = gamer
        gamer = 'O'
        check_win('X')
        count += 1
    if game_run and grid[x][y]['text'] == ' ' and gamer == 'O':
        grid[x][y]['text'] = gamer
        gamer = 'X'
        check_win('O')
        count += 1


# Проверка победы
def check_win(meaning):
    global count
    global gamer
    for n in range(3):
        check_line(grid[n][0], grid[n][1], grid[n][2], meaning)
        check_line(grid[0][n], grid[1][n], grid[2][n], meaning)
    check_line(grid[0][0], grid[1][1], grid[2][2], meaning)
    check_line(grid[2][0], grid[1][1], grid[0][2], meaning)
    if not game_run:
        choice = messagebox.askokcancel("Поздравляю", f'Победили {meaning} сыграть еще раз ?')
        if choice:
            gamer = 'X'
            new_game()
            count -= 1
        else:
            exit(window)
    elif game_run == True and count == 8:
        choice = messagebox.askokcancel("НИЧЬЯ", f'Попытать удачу еще раз ?')
        if choice:
            gamer = 'X'
            new_game()
            count -= 1
        else:
            exit(window)


def check_line(a1, a2, a3, meaning):
    if a1['text'] == meaning and a2['text'] == meaning and a3['text'] == meaning:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False


# Интерфейс
for x in range(3):
    line = []
    for y in range(3):
        button = Button(window, text=' ', height=5, width=10,
                        font=("Helvetica", "20"),
                        background='lavender',
                        command=lambda x=x, y=y: after_pressing(x, y))
        button.grid(row=x, column=y)
        line.append(button)
    grid.append(line)
window.mainloop()
