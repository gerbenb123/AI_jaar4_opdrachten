import random
import itertools
import math

MAX_DEPTH = 2


def merge_left(b):
    # merge the board left
    # this is the funcyoin that is reused in the other merges
    # b = [[0, 2, 4, 4], [0, 2, 4, 8], [0, 0, 0, 4], [2, 2, 2, 2]]    
    def merge(row, acc):
        # recursive helper for merge_left

        # if len row == 0, return accumulator
        if not row:
            return acc

        # x = first element
        x = row[0]
        # if len(row) == 1, add element to accumulator
        if len(row) == 1:
            return acc + [x]

        # if len(row) >= 2
        if x == row[1]:
            # add row[0] + row[1] to accumulator, continue with row[2:]
            return merge(row[2:], acc + [2 * x])
        else:
            # add row[0] to accumulator, continue with row[1:]
            return merge(row[1:], acc + [x])

    new_b = []
    for row in b:
        # merge row, skip the [0]'s
        merged = merge([x for x in row if x != 0], [])
        # add [0]'s to the right if necessary
        merged = merged + [0] * (len(row) - len(merged))
        new_b.append(merged)
    # return [[2, 8, 0, 0], [2, 4, 8, 0], [4, 0, 0, 0], [4, 4, 0, 0]]
    return new_b


def merge_right(b):
    # merge the board right
    # b = [[0, 2, 4, 4], [0, 2, 4, 8], [0, 0, 0, 4], [2, 2, 2, 2]]
    def reverse(x):
        return list(reversed(x))

    # rev = [[4, 4, 2, 0], [8, 4, 2, 0], [4, 0, 0, 0], [2, 2, 2, 2]]
    rev = [reverse(x) for x in b]
    # ml = [[8, 2, 0, 0], [8, 4, 2, 0], [4, 0, 0, 0], [4, 4, 0, 0]]
    ml = merge_left(rev)
    # return [[0, 0, 2, 8], [0, 2, 4, 8], [0, 0, 0, 4], [0, 0, 4, 4]]
    return [reverse(x) for x in ml]


def merge_up(b):
    # merge the board upward
    # note that zip(*b) is the transpose of b
    # b = [[0, 2, 4, 4], [0, 2, 4, 8], [0, 0, 0, 4], [2, 2, 2, 2]]
    # trans = [[2, 0, 0, 0], [4, 2, 0, 0], [8, 2, 0, 0], [4, 8, 4, 2]]
    trans = merge_left(zip(*b))
    # return [[2, 4, 8, 4], [0, 2, 2, 8], [0, 0, 0, 4], [0, 0, 0, 2]]
    return [list(x) for x in zip(*trans)]


def merge_down(b):
    # merge the board downward
    # b = [[0, 2, 4, 4], [0, 2, 4, 8], [0, 0, 0, 4], [2, 2, 2, 2]]
    # trans = [[0, 0, 0, 2], [0, 0, 2, 4], [0, 0, 8, 2], [4, 8, 4, 2]]
    trans = merge_right(zip(*b))
    # return [[0, 0, 0, 4], [0, 0, 0, 8], [0, 2, 8, 4], [2, 4, 2, 2]]
    return [list(x) for x in zip(*trans)]


# location: after functions
MERGE_FUNCTIONS = {
    'left': merge_left,
    'right': merge_right,
    'up': merge_up,
    'down': merge_down
}


def move_exists(b):
    # check whether or not a move exists on the board
    # b = [[1, 2, 3, 4], [5, 6, 7, 8]]
    # move_exists(b) return False
    def inner(b):
        for row in b:
            for x, y in zip(row[:-1], row[1:]):
                # tuples (1, 2),(2, 3),(3, 4),(5, 6),(6, 7),(7, 8)
                if x == y or x == 0 or y == 0:
                    return True
        return False

    if inner(b) or inner(zip(*b)):
        return True
    else:
        return False


def start():
    # make initial board
    b = [[0] * 4 for _ in range(4)]
    add_two_four(b)
    add_two_four(b)
    return b


def play_move(b, direction):
    # get merge functin an apply it to board
    b = MERGE_FUNCTIONS[direction](b)
    add_two_four(b)
    return b


def add_two_four(b):
    # add a random tile to the board at open position.
    # chance of placing a 2 is 90%; chance of 4 is 10%
    rows, cols = list(range(4)), list(range(4))
    random.shuffle(rows)
    random.shuffle(cols)
    distribution = [2] * 9 + [4]
    for i, j in itertools.product(rows, rows):
        if b[i][j] == 0:
            b[i][j] = random.sample(distribution, 1)[0]
            return (b)
        else:
            continue


def game_state(b):
    for i in range(4):
        for j in range(4):
            if b[i][j] >= 2048:
                return 'win'
    return 'lose'


def test():
    b = [[0, 2, 4, 4], [0, 2, 4, 8], [0, 0, 0, 4], [2, 2, 2, 2]]
    assert merge_left(b) == [[2, 8, 0, 0], [2, 4, 8, 0], [4, 0, 0, 0], [4, 4, 0, 0]]
    assert merge_right(b) == [[0, 0, 2, 8], [0, 2, 4, 8], [0, 0, 0, 4], [0, 0, 4, 4]]
    assert merge_up(b) == [(2, 4, 8, 4), (0, 2, 2, 8), (0, 0, 0, 4), (0, 0, 0, 2)]
    assert merge_down(b) == [(0, 0, 0, 4), (0, 0, 0, 8), (0, 2, 8, 4), (2, 4, 2, 2)]
    assert move_exists(b) == True
    b = [[2, 8, 4, 0], [16, 0, 0, 0], [2, 0, 2, 0], [2, 0, 0, 0]]
    assert (merge_left(b)) == [[2, 8, 4, 0], [16, 0, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0]]
    assert (merge_right(b)) == [[0, 2, 8, 4], [0, 0, 0, 16], [0, 0, 0, 4], [0, 0, 0, 2]]
    assert (merge_up(b)) == [(2, 8, 4, 0), (16, 0, 2, 0), (4, 0, 0, 0), (0, 0, 0, 0)]
    assert (merge_down(b)) == [(0, 0, 0, 0), (2, 0, 0, 0), (16, 0, 4, 0), (4, 8, 2, 0)]
    assert (move_exists(b)) == True
    b = [[0, 7, 0, 0], [0, 0, 7, 7], [0, 0, 0, 7], [0, 7, 0, 0]]
    g = Game()
    for i in range(11):
        g.add_two_four(b)


def get_random_move():
    return random.choice(list(MERGE_FUNCTIONS.keys()))


def calculate_board(b):
    # checks if rows are all values or if rows are all zeros
    check_rows = []
    for row in b:
        check_elements = []
        for element in row:
            if row[0] == 0:
                if element == 0:
                    check_elements.append(True)
                else:
                    check_elements.append(False)
            else:
                if element != 0:
                    if (row.index(element) > 0 and row[row.index(element) - 1] != element) or (
                            row.index(element) < 3 and row[row.index(element) + 1] != element):
                        check_elements.append(True)
                else:
                    check_elements.append(False)
        check_rows.append(all(check_elements))
    if all(check_rows):
        # TODO maybe should be negative because this is a very bad state
        return 0

    indices = range(16)
    indices_values = sorted(zip(indices, b[0] + b[1] + b[2] + b[3]), key=lambda x: x[1], reverse=True)

    # importance_score is 2^16
    importance_score = 65_536
    score = 0

    # determines where the highest values should be on the board in the correct order
    highest_value_order = [13, 14, 15, 16, 12, 11, 10, 9, 5, 6, 7, 8, 4, 3, 2, 1]

    # checks if board only has full rows.

    for i in indices_values:
        if i[0] == highest_value_order[indices_values.index(i)]:
            score += importance_score
        score /= 2

    return score

# checks all possible states that can lead from a state 'b' and the probability of this happening
def check_possible_states(b):
    possible_states = []
    amount_of_zeros = 0
    chance = 0
    for row in b:
        for element in row:
            if element == 0:
                amount_of_zeros += 1
    if amount_of_zeros != 0:
        chance = 1 / amount_of_zeros

    for row_index, row in enumerate(b):
        for element_index, element in enumerate(row):
            if element == 0:
                new_state_2 = [row[:] for row in b]
                new_state_2[row_index][element_index] = 2
                new_state_2_with_change = [chance * 0.9, new_state_2]
                new_state_4 = [row[:] for row in b]
                new_state_4[row_index][element_index] = 4
                new_state_4_with_change = [chance * 0.1, new_state_4]
                possible_states.append(new_state_2_with_change)
                possible_states.append(new_state_4_with_change)

    return possible_states


def get_expectimax_move(b, depth):
    if depth == 0:
        return calculate_board(b)

    highest_score = 0
    winning_move = 'up'
    for move_key, move_value in MERGE_FUNCTIONS.items():
        if move_key != 'up' and move_value(b) != b:
            score_of_move = 0
            for state in check_possible_states(move_value(b)):
                # get's the calculated board times the chance of that state happening
                score_of_move += (get_expectimax_move(state[1], depth - 1) * state[0])
            if highest_score < score_of_move:
                highest_score = score_of_move
                winning_move = move_key

    if depth != MAX_DEPTH:
        return highest_score
    else:
        return winning_move
