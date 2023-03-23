import copy
from typing import Optional


class ShipVariable:
    type: str
    topleft: Optional[tuple]
    orientation: Optional[str]
    legnth: int
    domain: list[tuple]

    def __init__(self, type):
        self.topleft = None
        self.orientation = None
        self.type = type
        if type == "sub":
            self.length = 1
        elif type == "destroyer":
            self.length = 2
        elif type == "cruiser":
            self.length = 3
        elif type == "battleship":
            self.length = 4

    def is_assigned_coord(self):
        return self.topleft is not None

    def is_assigned_orientation(self):
        return self.orientation is not None

    def assign(self, topleft, orientation):
        self.topleft = topleft
        self.orientation = orientation

    def get_coords(self):
        if self.orientation == "h":
            return [(self.topleft[0], self.topleft[1] + i) for i in range(self.length)]
        elif self.orientation == "v":
            return [(self.topleft[0] + i, self.topleft[1]) for i in range(self.length)]

    def get_parts(self):
        parts = {}
        if self.type == "sub":
            parts[(self.topleft[0], self.topleft[1])] = "S"
        elif self.orientation == "h":
            parts[(self.topleft[0], self.topleft[1])] = "<"
            for i in range(1, self.length - 1):
                parts[(self.topleft[0], self.topleft[1] + i)] = "M"
            parts[(self.topleft[0], self.topleft[1] + self.length - 1)] = ">"
        elif self.orientation == "v":
            parts[(self.topleft[0], self.topleft[1])] = "^"
            for i in range(1, self.length - 1):
                parts[(self.topleft[0] + i, self.topleft[1])] = "M"
            parts[(self.topleft[0] + self.length - 1, self.topleft[1])] = "v"
        return parts




class Csp:
    def __init__(self, board):
        self.row_const = board[0]
        self.col_const = board[1]
        self.ship_const = board[2]
        self.board = board[3:]
        self.variables = create_ships(self.ship_const)


def select_unassigned_variable(assignment, csp):
    for var in csp.variables:
        if var not in assignment:
            return var


def revise_domain(domain, var, csp, assignment):
    """Return a revised domain for the variable var, based on:
    1. Impossible values (out of bounds)
    2. Already filled coordinates
    """
    revised_domain = domain[:]
    filled_coords = []
    for var in assignment:
        for coord in var.get_coords():
            filled_coords.append(coord)
    for value in domain:
        if value[2] == "h":
            if value[1] + var.length > len(csp.board[0]):
                revised_domain.remove(value)
        elif value[2] == "v":
            if value[0] + var.length > len(csp.board):
                revised_domain.remove(value)
        elif (value[0], value[1]) in filled_coords:
            revised_domain.remove(value)
    return revised_domain


def order_domain_values(var, csp, assignment):
    domain = [(row, col, orientation) for row in range(len(csp.board)) for col in range(len(csp.board[0])) for orientation in ["h", "v"]]
    revised_domain = revise_domain(domain, var, csp, assignment)
    return revised_domain


def check_not_touching_ships(i, j, all_parts):
    part = all_parts[(i, j)]
    if part == 'S':
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
            try:
                if (x, y) in all_parts.keys():
                    return False
            except IndexError:
                pass
    elif part == '<':
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i - 1, j - 1), (i + 1, j - 1)]:
            try:
                if (x, y) in all_parts.keys():
                    return False
            except IndexError:
                pass
    elif part == '>':
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j + 1), (i - 1, j + 1), (i + 1, j + 1)]:
            try:
                if (x, y) in all_parts.keys():
                    return False
            except IndexError:
                pass
    elif part == '^':
        for (x, y) in [(i, j - 1), (i, j + 1), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1)]:
            try:
                if (x, y) in all_parts.keys():
                    return False
            except IndexError:
                pass
    elif part == 'v':
        for (x, y) in [(i, j - 1), (i, j + 1), (i + 1, j), (i + 1, j - 1), (i + 1, j + 1)]:
            try:
                if (x, y) in all_parts.keys():
                    return False
            except IndexError:
                pass
    elif part == 'M':
        try:
            if all_parts[(i - 1, j)] not in ['^', 'M'] or all_parts[(i + 1, j)] not in ['v', 'M']:
                return False
        except KeyError:
            pass
        try:
            if all_parts[(i, j - 1)] not in ['<', 'M'] or all_parts[(i, j + 1)] not in ['>', 'M']:
                return False
        except KeyError:
            pass
    return True


def is_consistent(csp, assignment):
    # dump the assignment into a list of filled coordinates
    filled_coords = []
    for var in assignment:
        for coord in var.get_coords():
            filled_coords.append(coord)
    # check row constraint
    for i in range(len(csp.row_const)):
        if len([coord for coord in filled_coords if coord[0] == i]) > int(csp.row_const[i]):
            return False
    # check col constraint
    for i in range(len(csp.col_const)):
        if len([coord for coord in filled_coords if coord[1] == i]) > int(csp.col_const[i]):
            return False
    # dump the assignment into a dictionary of filled coordinates mapping them to their part
    all_parts = {}
    for var in assignment:
        for coord, part in var.get_parts().items():
            all_parts[coord] = part
    # check assignment matches hints
    for i in range(len(csp.board)):
        for j in range(len(csp.board[0])):
            if (i, j) in all_parts.keys() and csp.board[i][j] not in [all_parts[(i, j)], '0']:
                return False
    # check surrounded by water
    for (i, j) in all_parts.keys():
        if not check_not_touching_ships(i, j, all_parts):
            return False
    return True


def create_ships(ship_const):
    ships = []
    # create submarines
    for i in range(int(ship_const[0])):
        new_sub = ShipVariable("sub")
        ships.append(new_sub)
    for i in range(int(ship_const[1])):
        new_destroyer = ShipVariable("destroyer")
        ships.append(new_destroyer)
    for i in range(int(ship_const[2])):
        new_cruiser = ShipVariable("cruiser")
        ships.append(new_cruiser)
    for i in range(int(ship_const[3])):
        new_battleship = ShipVariable("battleship")
        ships.append(new_battleship)
    return ships


def read_puzzle_board(filename):
    with open(filename) as f:
        board = [line.strip() for line in f]
    return board


def backtrack(assignment, csp: Csp):
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, csp, assignment):
        assignment[var] = value
        var.assign((value[0], value[1]), value[2])
        if is_consistent(csp, assignment):
            # inferences = inference(var, value, assignment, csp)
            # if inferences != False:
            #     assignment.update(inferences)
                result = backtrack(assignment, csp)
                if result != False:
                    return result
        assignment.pop(var)
    return False


def run_backtracking_search(csp):
    return backtrack({}, csp)


def make_board(puzzle_board, assignment):
    board = []
    for i in range(len(puzzle_board)):
        board.append([])
        for j in range(len(puzzle_board[0])):
            board[i].append('.')
    for var in assignment:
        for coord, part in var.get_parts().items():
            board[coord[0]][coord[1]] = part
    return board


def run_program(filename):
    puzzle_board = read_puzzle_board(filename)
    csp = Csp(puzzle_board)
    result = run_backtracking_search(csp)
    board = make_board(puzzle_board, result)
    for row in board:
        print(''.join(row))


if __name__ == '__main__':
    run_program('test_files/board.txt')