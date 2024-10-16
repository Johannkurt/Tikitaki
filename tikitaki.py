def draw_board(board):
    # Функция для отображения игрового поля
    print("  0 1 2")  # Нумерация столбцов
    for idx, row in enumerate(board):
        print(f"{idx} " + " ".join(row))  # Нумерация строк


def check_winner(board, player):
    # Функция для проверки победителя
    # Проверка строк
    for row in board:
        if row.count(player) == 3:
            return True

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_draw(board):
    # Функция для проверки на ничью (если нет пустых клеток)
    for row in board:
        if " " in row:
            return False
    return True


def player_move(board, player):
    # Функция для хода игрока
    while True:
        move = input(f"Игрок {player}, введите координаты (столбец строка, например 00 или 12): ")

        # Проверка правильного формата ввода
        if len(move) != 2 or not move.isdigit():
            print("Неправильный ввод. Введите две цифры: столбец и строку.")
            continue

        col, row = int(move[0]), int(move[1])

        # Проверка на корректные индексы
        if col not in [0, 1, 2] or row not in [0, 1, 2]:
            print("Неверные координаты. Столбец и строка должны быть 0, 1 или 2.")
            continue

        # Проверка, что выбранная клетка пуста
        if board[row][col] != " ":
            print("Клетка уже занята, выберите другую.")
            continue

        # Если всё корректно, делаем ход
        board[row][col] = player
        break


def tic_tac_toe():
    # Основная функция игры
    board = [[" " for _ in range(3)] for _ in range(3)]  # Игровое поле
    current_player = "X"

    while True:
        draw_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player):
            draw_board(board)
            print(f"Игрок {current_player} победил!")
            break

        if check_draw(board):
            draw_board(board)
            print("Ничья!")
            break

        # Меняем игрока
        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()