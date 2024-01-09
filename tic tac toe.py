# Отображение приветственнной надписи
def greeting():
    print('\nДобро пожаловать в игру "Крестики нолики".\n'
          'Правила игры просты кто первый сможет поставить \n3 свои фигуры в ряд победит.\n')


# Отображение сетки в консоль
def field_display(_playing_field):
    print("  | a | b | c |")
    print("--+---+---+---+")
    for i, row in enumerate(_playing_field):
        print(i, '|', ' | '.join(row), '|')
        print("--+---+---+---+")


# Получение кординат от пользователя с проверкой коректного ввода значения
def entering_values():
    while True:
        _cord = input("Введите кординаты в формате (a1 или 1a): ")
        _cord = _cord.replace(' ', '')
        _cord = _cord.lower()

        # Проверяем что строка состоит из 2 символов
        if len(_cord) == 2:
            # Проверяем что строка содержит букву и цифру и не содержит символов
            if _cord.isalnum() and not _cord.isalpha() and not _cord.isdigit():
                # Проверяем содержание конкретных символов в строке
                if ('a' in _cord or 'b' in _cord or 'c' in _cord) and ('0' in _cord or '1' in _cord or '2' in _cord):
                    return _cord

        print("Вы ввели не коректное значение повторите попытку.")


# Конвертация значений из строки в кортеж (из вида 'a1' или '1a' в (1, 0))
def conversion(_cord):
    # Сорттируем строку чтобы цифра обозначающая строку стояла перед букво означающей колонку (a1 => 1a)
    _cord = ''.join(sorted(_cord))
    _cord = _cord.replace('a', '0')
    _cord = _cord.replace('b', '1')
    _cord = _cord.replace('c', '2')
    _cord = tuple(map(int, _cord))
    return _cord


# Проверка на победу
def checking_for_a_win(_playing_field, _player):
    win_cord = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)))
    for _cord in win_cord:
        # Если значения всех кординат равны между собой
        # а так же равны символу за который играет игрок
        # значит достигнута выйгрошная комбинация
        if (_playing_field[_cord[0][0]][_cord[0][1]]
                == _playing_field[_cord[1][0]][_cord[1][1]]
                == _playing_field[_cord[2][0]][_cord[2][1]]
                == _player):
            print(f"Победил игрок {_player}")
            return True
    return False


playing_field = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
step = 0
cord = None
player = None

field_display(playing_field)

# Выводим приветствие
greeting()
# Отображаем игровое поле
field_display(playing_field)

# Начало игры максимальное кол-во ходов в игре 9
while True:
    # Чередуем игроков
    if step % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    # Блок запрашивает у пользователя кординаты ячейки
    # и проверяет свободна ли ечейка на поле
    while True:
        print(f"\nХод игрока {player}.")
        # Получаем от первого игрока кординаты ячейки для записи символа
        cord = conversion(entering_values())
        # Проверяем доступность ячейки для записи если да переписываем
        # если нет просим пользователя повторить ввод
        if playing_field[cord[0]][cord[1]] == ' ':
            playing_field[cord[0]][cord[1]] = player
            break
        else:
            print(f"Это поле уже помечено {playing_field[cord[0]][cord[1]]} выберете свободное.")
    # Отображаем игровое поле с изменениями
    field_display(playing_field)
    # Проверяем на победу
    if checking_for_a_win(playing_field, player):
        break
    # Отслеживаем ходы
    step += 1
    # Если прошло 9 ходов без победителя тогда ничья
    if step == 9:
        print("Ничья")
        break