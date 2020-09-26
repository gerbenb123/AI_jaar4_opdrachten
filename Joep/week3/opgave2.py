# a) 1. Het aantal permutaties is 8! / (8 - 4)! = 1680
#    2.
# c) huh?

import itertools


def tests(permutation):
    neighbours = [[6], [5], [4, 6, 9], [5, 10], [5, 10], [6, 9, 11, 14], [10], [10]]

    index = -1

    for (key, value) in permutation.items():
        index += 1
        if value == "":
            continue
        if value not in [permutation[i] for i in neighbours[index]]:
            continue
        if value == 'A' and 'K' in [permutation[i] for i in neighbours[index]]:
            continue
        if value == 'K' and 'Q' in [permutation[i] for i in neighbours[index]]:
            continue
        if value == 'Q' and 'J' in [permutation[i] for i in neighbours[index]]:
            continue
        if value == 'A' and 'Q' not in [permutation[i] for i in neighbours[index]]:
            continue
        return False
    # Returns true if the for loop has finished
    return True


def solve(dictionary, cards, current_index):
    valid_indices = [2, 4, 5, 6, 9, 10, 11, 14]
    if tests(dictionary):
        if "" not in dictionary.values():
            print(dictionary)
            return True
        current_index += 1
        current_key = valid_indices[current_index]

        for card in cards:
            dictionary[current_key] = card
            new_cards = cards.copy()
            new_cards.remove(card)
            if solve(dictionary, new_cards, current_index):
                return True

            dictionary[current_key] = ""


def brute_force(valid_indices, cards):
    for permutation in list(itertools.permutations(cards)):
        dict_permutation = dict(zip(valid_indices, permutation))
        if tests(dict_permutation):
            print(permutation)


if __name__ == '__main__':
    # A = Ace, K = King, Q = Queen, J = Jack
    cards = ['A', 'A', 'K', 'K', 'Q', 'Q', 'J', 'J']
    valid_indices = [2, 4, 5, 6, 9, 10, 11, 14]
    start_dictionary = dict(zip(valid_indices, ["", "", "", "", "", "", "", ""]))

    solve(start_dictionary, cards, -1)
