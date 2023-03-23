from battle import *


def test_surrounded_by_water():
    board = read_board('test_files/surrounded_by_water_test_board.txt')
    test_lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            test_lst.append(surrounded_by_water(board, i, j, board[i][j]))
    assert all(test_lst)


def test_is_valid():
    puzzle_board = read_board('test_files/is_valid_test_board.txt')
    row_const, col_const, ship_const = puzzle_board[0], puzzle_board[1], puzzle_board[2]
    board = puzzle_board[3:]
    test_lst = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            test_lst.append(is_valid(board, row, col, board[row][col], row_const, col_const, ship_const))
    assert all(test_lst)


if __name__ == '__main__':
    from pytest import main
    main(['test.py'])
