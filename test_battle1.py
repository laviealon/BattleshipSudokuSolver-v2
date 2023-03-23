from battle1 import *


def test_check_not_touching_ships():
    puzzle_board = read_puzzle_board('test_files/check_not_touching_ships_test_board.txt')
    csp = Csp(puzzle_board)
    csp.variables[0].assign((0, 1), None)
    csp.variables[1].assign((2, 2), 'v')
    csp.variables[2].assign((5, 0), 'h')
    csp.variables[3].assign((0, 5), 'v')
    all_parts = {}
    for var in csp.variables:
        for coord, part in var.get_parts().items():
            all_parts[coord] = part
    for (i, j) in all_parts.keys():
        assert check_not_touching_ships(i, j, all_parts)

