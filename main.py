SYMBOLS = ['S', 'M', '^', 'v', '<', '>', '.']


def read_board(filename):
    with open(filename) as f:
        board = []
        for line in f:
            board.append(line.strip())
        return board


def is_valid(board, row, col, symbol, row_const, col_const, ship_const):
    """Checks if the symbol is valid at the given row and column."""
    # create copy board with symbol at row and col
    copy_board = board[:]
    copy_board[row] = copy_board[row][:col] + symbol + copy_board[row][col + 1:]
    # check if row and col constraints are met
    count = 0
    for ch in copy_board[row]:
        if ch not in ['.', '0']:
            count += 1
    if count > int(row_const[row]):
        return False
    count = 0
    for i in range(len(copy_board)):
        if copy_board[i][col] not in ['.', '0']:
            count += 1
    if count > int(col_const[col]):
        return False
    # check if ships are composed correctly, and count them
    ship_count = {'sub': 0, 'dest': 0, 'carr': 0, 'batt': 0}
    for i in range(len(copy_board)):
        for j in range(len(copy_board)):
            # if you find 'S' make sure it is surrounded by water (and count 1x1)
            if copy_board[i][j] == 'S':
                if i == 0 and j == 0:
                    if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                elif i == 0 and j == len(copy_board) - 1:
                    if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                elif i == len(copy_board) - 1 and j == 0:
                    if copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                elif i == len(copy_board) - 1 and j == len(copy_board) - 1:
                    if copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                elif i == 0:
                    if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                elif i == len(copy_board) - 1:
                    if copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                elif j == 0:
                    if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                elif j == len(copy_board) - 1:
                    if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
                else:
                    if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0']:
                        return False
                    else:
                        ship_count['sub'] += 1
        # if you find '<' make sure it is followed by '>' and both are surrounded by water (and count 1x2),
        # or that it is followed by 'M' and '>' and both are surrounded by water (and count 1x3).
        # or that it is followed by 'M', 'M', and '>' and both are surrounded by water (and count 1x4).
        # if you find '^' make sure it is followed by 'v' and both are surrounded by water (and count 1x2),
        # or that it is followed by 'M' and 'v' and both are surrounded by water (and count 1x3),
        # or that it is followed by 'M', 'M', and 'v' and both are surrounded by water (and count 1x4).
    # check ship constraint
        # make sure number of ships aligns with ship constraint
    return True


def backtracking_search(puzzle_board):
    """Solves the battleship sudoku board using backtracking search.

    TODO: does this work??
    """
    row_const, col_const, ship_const = puzzle_board[0], puzzle_board[1], puzzle_board[2]
    board = puzzle_board[3:]
    dimension = len(board)
    for row in range(dimension):
        for col in range(dimension):
            if board[row][col] == '0':
                for symbol in SYMBOLS:  # can potentially switch to revise_domain(board, row, col, symbol)
                    if is_valid(board, row, col, symbol, row_const, col_const, ship_const):
                        board[row] = board[row][:col] + symbol + board[row][col + 1:]
                        backtracking_search(puzzle_board)
                        board[row] = board[row][:col] + '0' + board[row][col + 1:]
                return


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(5000000)
    board = read_board('board.txt')
    backtracking_search(board)
    for row in board:
        print(row)