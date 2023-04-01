

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

board_map = {
    'a1': board[0],
    'a2': board[1],
    'a3': board[2],
    'b1': board[3],
    'b2': board[4],
    'b3': board[5],
    'c1': board[6],
    'c2': board[7],
    'c3': board[8],
}

key_list = list(board_map.keys())

players = {'p1': 'X', 'p2': 'O'}

initial_board = "    a     b     c\n"\
         "      |     |     \n"\
         f"1 {board_map['a1']}   |  {board_map['a2']}  |  {board_map['a3']}  \n"\
         " _____|_____|_____\n"\
         "      |     |     \n"\
         f"2  {board_map['b1']}  |  {board_map['b2']}  |  {board_map['b3']}  \n"\
         " _____|_____|_____\n"\
         "      |     |     \n"\
         f"3  {board_map['c1']}  |  {board_map['c2']}  |  {board_map['c3']}  \n"\
         "      |     |     "


def update_board(loc, p):
    board_map[loc] = players[p]
    updated_board = "    1     2     3\n" \
                    "      |     |     \n" \
                    f"a {board_map['a1']}   |  {board_map['a2']}  |  {board_map['a3']}  \n" \
                    " _____|_____|_____\n" \
                    "      |     |     \n" \
                    f"b  {board_map['b1']}  |  {board_map['b2']}  |  {board_map['b3']}  \n" \
                    " _____|_____|_____\n" \
                    "      |     |     \n" \
                    f"c  {board_map['c1']}  |  {board_map['c2']}  |  {board_map['c3']}  \n" \
                    "      |     |     "
    print(updated_board)
    return board_map


def rows(b, player):
    if b['a1'] == b['a2'] == b['a3'] == players[player] or b['b1'] == b['b2'] == b['b3'] == players[player] or b['c1'] \
            == b['c2'] == b['c3'] == players[player]:
        return True


def columns(b, player):
    if b['a1'] == b['b1'] == b['c1'] == players[player] or b['a2'] == b['b2'] == b['c2'] == players[player] or b['a3'] \
            == b['b3'] == b['c3'] == players[player]:
        return True


def diagonal(b, player):
    if (b['a1'] == b['b2'] == b['c3'] == players[player]) or (b['a3'] == b['b2'] == b['c1'] == players[player]):
        return True


def has_won(b, player):
    if rows(b, player) or columns(b, player) or diagonal(b, player):
        return True


print(initial_board)
updated = {}
Flag = False
for key in board_map:
    if not Flag:
        cell = input("choose a cell to put an X:")
        if cell in key_list and board_map[cell] == '-':
            updated = update_board(cell, 'p1')
            Flag = True
            if has_won(updated, 'p1'):
                print(f"Player 1 is the winner!")
                break
        else:
            print("Not a valid cell, try again!")
    if not has_won(updated, 'p1') and not has_won(updated, 'p2') and '-' not in board_map.values():
        print('DRAW!!!')
        break
    if Flag:
        cell = input("choose a cell to put an O:")
        if cell in key_list and board_map[cell] == '-':
            updated = update_board(cell, 'p2')
            Flag = False
            if has_won(updated, 'p2'):
                print(f"Player 2 is the winner!")
                break
        else:
            print("Not a valid cell, try again!")

