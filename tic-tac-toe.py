# Инициализация карты
maps = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Вывод карты на экран
def conclusion():
    print('',*maps[0],'\n',*maps[1],'\n',*maps[2])
# Сделать ход в ячейку
def move(step, symbol):
    if 0 < step < 4:
        ind = maps[0].index(step)
        maps[0][ind] = symbol
    elif 3 < step < 7:
        ind = maps[1].index(step)
        maps[1][ind] = symbol
    elif 6 < step < 10:
        ind = maps[2].index(step)
        maps[2][ind] = symbol
    else:
        print('Число должно быть 1-9 (смотри на незаполненные поля)')
# Получить текущий результат игры
def result(meaning):
    for n in range(3):
        check_line(maps[n][0], maps[n][1], maps[n][2], meaning)
        check_line(maps[0][n], maps[1][n], maps[2][n], meaning)
    check_line(maps[0][0], maps[1][1], maps[2][2], meaning)
    check_line(maps[2][0], maps[1][1], maps[0][2], meaning)
def check_line(a1, a2, a3, meaning):
    if a1 == meaning and a2 == meaning and a3 == meaning:
        print (f'Поздравлаю победили {meaning}')
        global game_run
        game_run = False
# Основная программа
game_run = True
gamer = True
count = 0
while game_run:
    # 1. Показываем игровое поле
    conclusion()
    # 2. Кто делает ход
    if gamer:
        symbol = "X"
        step = int(input("Ходят Х: "))
        gamer = False
        count += 1
    else:
        symbol = "O"
        step = int(input("Ходят О: "))
        gamer = True
        count += 1
    move(step, symbol)  # делаем ход в указанную ячейку
    result(meaning=symbol)  # определим победителя
    if count == 9:
        print('Победила дружба )')
        break