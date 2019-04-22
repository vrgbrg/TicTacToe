from random import randint

players = {'player_one': '', 'player_two': ''}
symbols = ['O', 'X']
end = False
again = True


def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print("")


def find_cell(board, cell):
    for row, col in enumerate(board):
        try:
            column = col.index(cell)
        except ValueError:
            continue
        return row, column
    return -1


def winner_check(board, symbol, player):
    global end
    for row in board:
        r = [symbol, symbol, symbol, 's']
        for i, col in enumerate(row):
            if col == r[0]:
                r.pop(0)
            if len(r) == 1:
                print(f'The Winner is {player}')
                end = True
    for i, row in enumerate(board):
        r = [symbol, symbol, symbol, 's']
        for j, col in enumerate(row):
            if board[j][i] == r[0]:
                r.pop(0)
            if len(r) == 1:
                print(f'The Winner is {player}')
                end = True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        print(f'The Winner is {player}')
        end = True
    elif board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol:
        print(f'The Winner is {player}')
        end = True


def next_player():
    global current_player
    if not end:
        if current_player == 'player_one':
            current_player = 'player_two'
            return current_player
        else:
            current_player = 'player_one'
            return current_player


def replay():
    global again
    global end
    play_again = input('Again? Y or N: ').upper()
    while play_again not in ['Y', 'N']:
        play_again = input('Incorrect, Y or N? ').upper()
    if play_again == 'N':
        again = False
        return again


while again:
    end = False
    cells = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    print('Hello players!')

    input('Random start, press any button')

    start = randint(1, 2)

    current_player_index = start
    current_player = ''

    if start == 1:
        current_player = 'player_one'
        players['player_one'] = input('PlayerOne starts, choose symbol! X or O? ').upper()
        while players['player_one'] not in symbols:
            players['player_one'] = input('Incorrect, choose symbol! X or O? ').upper()
        if players['player_one'] == 'X':
            players['player_two'] = 'O'
        else:
            players['player_two'] = 'X'
    else:
        current_player = 'player_two'
        players['player_two'] = input('PlayerTwo starts, choose symbol! X or O? ').upper()
        while players['player_two'] not in symbols:
            players['player_two'] = input('Incorrect, choose symbol! X or O? ').upper()
        if players['player_two'] == 'X':
            players['player_one'] = 'O'
        else:
            players['player_one'] = 'X'

    print_board(cells)
    while not end:
        print('Current player: ' + current_player)
        choose = input(f'{current_player}, give me a number from the board! ')
        while choose not in numbers:
            choose = input('Incorrect, give me a number from the board! ')
        row, col = find_cell(cells, choose)
        cells[row][col] = players[current_player]
        print_board(cells)
        numbers.remove(choose)
        winner_check(cells, players[current_player], current_player)
        if end:
            replay()
        next_player()
