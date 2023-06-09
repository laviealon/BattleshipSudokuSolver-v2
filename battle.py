import copy

SYMBOLS = ['S', 'M', '^', 'v', '<', '>', '.']


def count_ships(board):
    ship_count = {'sub': 0, 'destroyer': 0, 'cruiser': 0, 'battleship': 0}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                ship_count['sub'] += 1
            elif board[i][j] == '^':
                try:
                    if board[i - 1][j] == 'v':
                        ship_count['destroyer'] += 1
                    elif board[i - 1][j] == 'M' and board[i - 2][j] == 'v':
                        ship_count['cruiser'] += 1
                    elif board[i - 1][j] == 'M' and board[i - 2][j] == 'M' and board[i - 3][j] == 'v':
                        ship_count['battleship'] += 1
                except IndexError:
                    pass
            elif board[i][j] == '<':
                try:
                    if board[i][j + 1] == '>':
                        ship_count['destroyer'] += 1
                    elif board[i][j + 1] == 'M' and board[i][j + 2] == '>':
                        ship_count['cruiser'] += 1
                    elif board[i][j + 1] == 'M' and board[i][j + 2] == 'M' and board[i][j + 3] == '>':
                        ship_count['battleship'] += 1
                except IndexError:
                    pass
    return ship_count
                        
                
            
    

def read_board(filename):
    with open(filename) as f:
        board = []
        for line in f:
            board.append(line.strip())
        return board


def surrounded_by_water(copy_board, i, j, symbol, orientation=None):
    if symbol == 'M':
        if orientation == 'h':
            if i == 0:
                if copy_board[i + 1][j] not in ['.', '0']:
                    return False
            elif i == len(copy_board) - 1:
                if copy_board[i - 1][j] not in ['.', '0']:
                    return False
            else:
                if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0']:
                    return False
        elif orientation == 'v':
            if j == 0:
                if copy_board[i][j + 1] not in ['.', '0']:
                    return False
            elif j == len(copy_board) - 1:
                if copy_board[i][j - 1] not in ['.', '0']:
                    return False
            else:
                if copy_board[i][j + 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0']:
                    return False
    elif symbol == '<':
        if i == 0 and j == 0:
            if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0']:
                return False
        elif i == 0:
            if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0']:
                return False
        elif i == len(copy_board) - 1 and j == 0:
            if copy_board[i - 1][j] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0']:
                return False
        elif i == len(copy_board) - 1:
            if copy_board[i - 1][j] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0']:
                return False
        elif j == 0:
            if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0']:
                return False
        else:
            if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0']:
                return False
    elif symbol == '>':
        if i == 0 and j == len(copy_board) - 1:
            if copy_board[i + 1][j] not in ['.', '0']:
                return False
        elif i == 0:
            if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0']:
                return False
        elif i == len(copy_board) - 1 and j == len(copy_board) - 1:
            if copy_board[i - 1][j] not in ['.', '0']:
                return False
        elif i == len(copy_board) - 1:
            if copy_board[i - 1][j] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0']:
                return False
        elif j == len(copy_board) - 1:
            if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0']:
                return False
        else:
            if copy_board[i + 1][j] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j + 1] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0']:
                return False
    elif symbol == '^':
        if i == 0 and j == 0:
            if copy_board[i][j + 1] not in ['.', '0']:
                return False
        elif i == 0 and j == len(copy_board) - 1:
            if copy_board[i][j - 1] not in ['.', '0']:
                return False
        elif i == 0:
            if copy_board[i][j + 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0']:
                return False
        elif j == 0:
            if copy_board[i][j + 1] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0']:
                return False
        elif j == len(copy_board) - 1:
            if copy_board[i][j - 1] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0']:
                return False
        else:
            if copy_board[i][j + 1] not in ['.', '0'] or copy_board[i - 1][j] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i - 1][j - 1] not in ['.', '0'] or copy_board[i - 1][j + 1] not in ['.', '0']:
                return False
    elif symbol == 'v':
        if i == len(copy_board) - 1 and j == 0:
            if copy_board[i][j + 1] not in ['.', '0']:
                return False
        elif i == len(copy_board) - 1 and j == len(copy_board) - 1:
            if copy_board[i][j - 1] not in ['.', '0']:
                return False
        elif i == len(copy_board) - 1:
            if copy_board[i][j + 1] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0']:
                return False
        elif j == 0:
            if copy_board[i][j + 1] not in ['.', '0'] or copy_board[i + 1][j] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0']:
                return False
        elif j == len(copy_board) - 1:
            if copy_board[i][j - 1] not in ['.', '0'] or copy_board[i + 1][j] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0']:
                return False
        else:
            if copy_board[i][j + 1] not in ['.', '0'] or copy_board[i + 1][j] not in ['.', '0'] or copy_board[i][j - 1] not in ['.', '0'] or copy_board[i + 1][j - 1] not in ['.', '0'] or copy_board[i + 1][j + 1] not in ['.', '0']:
                return False
    return True


def is_valid(copy_board, row, col, row_const, col_const, ship_const):
    """Checks if the symbol is valid at the given row and column."""
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
    ship_count = {'sub': 0, 'destroyer': 0, 'cruiser': 0, 'battleship': 0}
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
            elif copy_board[i][j] == '<':
                if j == len(copy_board) - 1:
                    return False
                if copy_board[i][j + 1] not in ['>', 'M', '0']:
                    return False
                if not surrounded_by_water(copy_board, i, j, '<'):
                    return False
                if copy_board[i][j + 1] == '>':
                    if not surrounded_by_water(copy_board, i, j + 1, '>'):
                        return False
                    else:
                        ship_count['destroyer'] += 1
                # or that it is followed by 'M' and '>' and both are surrounded by water (and count 1x3).
                if copy_board[i][j + 1] == 'M':
                    if j + 1 == len(copy_board) - 1:
                        return False
                    if copy_board[i][j + 2] not in ['>', 'M', '0']:
                        return False
                    if not surrounded_by_water(copy_board, i, j + 1, 'M', orientation='h'):
                        return False
                    if copy_board[i][j + 2] == '>':
                        if not surrounded_by_water(copy_board, i, j + 2, '>'):
                            return False
                        else:
                            ship_count['cruiser'] += 1
                    # or that it is followed by 'M', 'M', and '>' and both are surrounded by water (and count 1x4).
                    elif copy_board[i][j + 2] == 'M':
                        if j + 2 == len(copy_board) - 1:
                            return False
                        if copy_board[i][j + 3] not in ['>', '0']:
                            return False
                        if not surrounded_by_water(copy_board, i, j + 2, 'M', orientation='h'):
                            return False
                        if copy_board[i][j + 3] == '>':
                            if not surrounded_by_water(copy_board, i, j + 3, '>'):
                                return False
                            else:
                                ship_count['battleship'] += 1
        # if you find '^' make sure it is followed by 'v' and both are surrounded by water (and count 1x2),
            elif copy_board[i][j] == '^':
                if i == len(copy_board) - 1:
                    return False
                if copy_board[i + 1][j] not in ['v', 'M', '0']:
                    return False
                if not surrounded_by_water(copy_board, i, j, '^'):
                    return False
                if copy_board[i + 1][j] == 'v':
                    if not surrounded_by_water(copy_board, i + 1, j, 'v'):
                        return False
                    else:
                        ship_count['destroyer'] += 1
                # or that it is followed by 'M' and 'v' and both are surrounded by water (and count 1x3).
                elif copy_board[i + 1][j] == 'M':
                    if i + 1 == len(copy_board) - 1:
                        return False
                    if copy_board[i + 2][j] not in ['v', 'M', '0']:
                        return False
                    if not surrounded_by_water(copy_board, i + 1, j, 'M', orientation='v'):
                        return False
                    if copy_board[i + 2][j] == 'v':
                        if not surrounded_by_water(copy_board, i + 2, j, 'v'):
                            return False
                        else:
                            ship_count['cruiser'] += 1
                    # or that it is followed by 'M', 'M', and 'v' and all are surrounded by water (and count 1x4).
                    elif copy_board[i + 2][j] == 'M':
                        if i + 2 == len(copy_board) - 1:
                            return False
                        if copy_board[i + 3][j] not in ['v', '0']:
                            return False
                        if not surrounded_by_water(copy_board, i + 2, j, 'M', orientation='v'):
                            return False
                        if copy_board[i + 3][j] == 'v':
                            if not surrounded_by_water(copy_board, i + 3, j, 'v'):
                                return False
                            else:
                                ship_count['battleship'] += 1
        # if you find an 'M' ... should be handled by '<' case and 'v' case above, but just in case keep this here
        # if you find a 'v' ... should be handled by '^' case above, but just in case keep this here
        # if you find a '>' ... should be handled by '<' case above, but just in case keep this here
    # check ship constraint
        # make sure number of ships aligns with ship constraint
    if ship_count['sub'] > int(ship_const[0]) or ship_count['destroyer'] > int(ship_const[1]) or \
            ship_count['cruiser'] > int(ship_const[2]) or ship_count['battleship'] > int(ship_const[3]):
        return False

    return True


def is_valid_solution(board, row_const, col_const, ship_const):
    for row in range(len(board)):
        count = 0
        for ch in board[row]:
            if ch not in ['.', '0']:
                count += 1
        if count != int(row_const[row]):
            return False
    for col in range(len(board)):
        count = 0
        for i in range(len(board)):
            if board[i][col] not in ['.', '0']:
                count += 1
        if count != int(col_const[col]):
            return False
    ship_count = count_ships(board)
    if ship_count['sub'] != int(ship_const[0]) or ship_count['destroyer'] != int(ship_const[1]) or \
            ship_count['cruiser'] != int(ship_const[2]) or ship_count['battleship'] != int(ship_const[3]):
        return False
    return True




def backtracking_search(puzzle_board):
    """Solves the battleship sudoku board using backtracking search.

    TODO: does this work??
    """
    seen = set()
    row_const, col_const, ship_const = puzzle_board[0], puzzle_board[1], puzzle_board[2]
    board = puzzle_board[3:]
    dimension = len(board)
    is_complete = True
    for row in range(dimension):
        for col in range(dimension):
            if board[row][col] == '0':
                is_complete = False
                break
        if not is_complete:
            break
    if is_complete:
        return puzzle_board
    for row in range(dimension):
        for col in range(dimension):
            if board[row][col] == '0':
                for symbol in SYMBOLS:  # can potentially switch to revise_domain(board, row, col, symbol)
                    copy_board = board[:]
                    copy_board[row] = copy_board[row][:col] + symbol + copy_board[row][col + 1:]
                    if str(copy_board) in seen:
                        seen.add(str(copy_board))
                        continue
                    is_valid_candidate = is_valid(copy_board, row, col, row_const, col_const, ship_const)
                    if is_valid_candidate:
                        puzzle_board[3:] = copy_board
                        result = backtracking_search(puzzle_board)
                        if result is not None and is_valid_solution(result[3:], row_const, col_const, ship_const):
                            return result
    return None


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)
    board = read_board('test_files/board.txt')
    board = backtracking_search(board)
    for row in board:
        print(row)