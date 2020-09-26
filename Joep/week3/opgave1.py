import itertools

def tests(permutation):
    if not permutation.index('E') > permutation.index('M'):
        return False
    if permutation[4] == 'L' or permutation[4] == 'N':
        return False
    if permutation[0] == 'M' or permutation[0] == 'N':
        return False
    if abs(permutation.index('J') - permutation.index('N')) <= 1:
        return False
    if abs(permutation.index('N') - permutation.index('M')) <= 1:
        return False
    return True


if __name__ == '__main__':
    floors = ['L', 'M', 'N', 'E', 'J']
    for permutation in list(itertools.permutations(floors)):
        if tests(permutation):
            print(permutation)
            break