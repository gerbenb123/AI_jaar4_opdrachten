# a) 1. Het aantal permutaties is 8! = 40320
#    2. 12795
#
# c) IN DEZE FOLDER ZITTEN OOK FOTO'S VAN DEZE OPDRACHT OP PAPIER WAARIN DE VOLGORDE VAN STAPPEN WORDT BESCHREVEN.
#
# Als 5 een boer is dan moeten 6 en 7 een vrouw zijn, omdat een Aas en een heer altijd respectievelijk
# aan een heer en een vrouw moeten zitten. Dit betekend dat de vrouwen op zijn, wat betekend dat een heer nooit aan een
# vrouw kan zitten.
#
# Als 5 een Vrouw is dan kunnen de omliggenden alleen een heer of een boer zijn, wat betekend dat alle heren en boeren
# op zijn. Nu zal er tussen 2 en 3 altijd een vrouw of aas naast een vrouw of aas liggen, wat niet kan.
#
# Als 5 een Aas is dan kunnen de omliggenden alleen een heer of boer zijn, wat dus hetzelfde resultaat oplevert als
# wanneer 5 een vrouw is.
#
#
#
# Als 0 een Aas is dan moet 3 een koning zijn, wat niet kan omdat 5 ook al een koning is.
#
# Als 0 een koningin is dan moet 3 een Boer zijn. 6 en 7 kunnen dan alleen een Aas of een Boer zijn, waardoor 4 een
# koningin moet zijn omdat de koning naast een koningin moet zitten. Dit betekend dat 2 een boer moet zijn wat niet
# kan omdat 3 ook al een boer is
#
# Als 0 een boer is dan zijn 6 en 7 een Aas omdat een koningin altijd naast een boer moet liggen en hier niet genoeg
# boeren voor zijn als 6 of 7 al een boer is. Dit betekend ook dat 3 een koningin moet zijn omdat boer en koning niet
# kunnen en alle Azen op zijn. Vervolgens moet 4 ook een koningin zijn omdat als 4 een boer is, dan moet 2 een koningin
# zijn, wat niet kan omdat 3 ook al een koningin is. Nu moet 2 een boer zijn omdat de koningin altijd naast een boer
# moet liggen. Nu blijft voor 1 alleen nog een koning over wat niet mogelijk is omdat een koning altijd naast een
# koningin moet liggen.

import itertools


def tests(permutation):
    neighbours = [[6], [5], [4, 6, 9], [2, 5, 10], [5, 10], [6, 9, 11, 14], [10], [10]]

    index = -1

    for (key, value) in permutation.items():
        index += 1
        neighbour_values = [permutation[i] for i in neighbours[index]]

        if value == "":
            continue
        if value in [permutation[i] for i in neighbours[index]]:
            return False
        if value == 'A' and 'K' not in neighbour_values and '' not in neighbour_values:
            return False
        if value == 'K' and 'Q' not in neighbour_values and '' not in neighbour_values:
            return False
        if value == 'Q' and 'J' not in neighbour_values and '' not in neighbour_values:
            return False
        if value == 'A' and 'Q' in neighbour_values:
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
    count = 0
    for permutation in list(itertools.permutations(cards)):
        dict_permutation = dict(zip(valid_indices, permutation))
        count += 1
        if tests(dict_permutation):
            print(permutation)


if __name__ == '__main__':
    # A = Ace, K = King, Q = Queen, J = Jack
    cards = ['A', 'A', 'K', 'K', 'Q', 'Q', 'J', 'J']
    valid_indices = [2, 4, 5, 6, 9, 10, 11, 14]
    start_dictionary = dict(zip(valid_indices, ["", "", "", "", "", "", "", ""]))

    solve(start_dictionary, cards, -1)
