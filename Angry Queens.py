from random import choice

def board2row(pos):
    nums = [[j + (i * 8) for j in range(8)] for i in range(8)]
    row = []
    for lst in nums:
        row = [num for num in lst] if pos in lst else row
    return row

def board2column(pos):
    nums = [[i + (j * 8) for j in range(8)] for i in range(8)]
    column = []
    for lst in nums:
        column = [num for num in lst] if pos in lst else column
    return column

def board2diagonal(pos):
    row = pos // 8
    col = pos % 8
   
    diagonal_1 = []
    diagonal_2 = []
   
    r = row
    c = col
    while r >= 0 and c >= 0:
        diagonal_1.append((r * 8) + c)
        r -= 1
        c -= 1
   
    r = row
    c = col
    while r < 8 and c < 8:
        diagonal_1.append((r * 8) + c)
        r += 1
        c += 1
   
    r = row
    c = col
    while r >= 0 and c < 8:
        diagonal_2.append((r * 8) + c)
        r -= 1
        c += 1
   
    r = row
    c = col
    while r < 8 and c >= 0:
        diagonal_2.append((r * 8) + c)
        r += 1
        c -= 1
   
    return diagonal_1, diagonal_2

def queen_attack_patern(pos):
    row = board2row(pos)
    column = board2column(pos)
    diag1, diag2 = board2diagonal(pos)
    total = row + column + diag1 + diag2
    return total

def generate_board():
    board = [0 for _ in range(64)]
    while 0 in board:
        free_pos = [i for i in range(64) if not board[i]]
        cell_id = choice(free_pos)
        for num in queen_attack_patern(cell_id):
            board[num] = 1
        board[cell_id] = 2
    return [1 if i == 2 else 0 for i in board]

def render_board(board):
    for i in range(8):
        row = ''
        for j in range(8):
            row += ' Q' if board[j + (i * 8)] else ' #'
        print(row)
 
board = generate_board()
render_board(board)