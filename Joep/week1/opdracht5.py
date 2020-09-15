# This file creates a sliding puzzle board and shuffles it, and then solves it with an implementation of the A*
# algorithm.

import sys
import random
from math import floor

n = 3
# n = int(sys.argv[1])
visitedStates = []

#TODO(calculate steps taken in cost)
def solvePuzzle(currentState, goalState):
    while currentState != goalState:
        nextStates = findNextStates(currentState)
        # costToGoal calculates the manhattan distance of all pieces in relation to their respective goalState
        # , and sets the currentState as the state with the lowest costToGoal
        # TODO(calculate linear conflict for cost)
        costToGoal = 1000
        winningState = []
        for nextState in nextStates:
            newCostToGoal = 0
            for index in range(len(nextState)):
                if nextState[index] != 0:
                    linearConflict = 0

                    goalIndex = goalState.index(nextState[index])
                    newCostToGoal += abs(floor(index / n) - floor(goalIndex / n) + abs((index % n) - (index % n))) + linearConflict
            if newCostToGoal < costToGoal and nextState not in visitedStates:
                costToGoal = newCostToGoal
                winningState = nextState
        if winningState == []:
            currentState = visitedStates[visitedStates.index(currentState) - 1]
            print("done 1 steps back")
            print()
        else:
            currentState = winningState
            visitedStates.append(currentState)

        for i in range(n):
            print(currentState[i * n: i * n + n])
        print()

    print("Solved in: " + str(len(visitedStates)) + " steps")


def findNextStates(currentState):
    states = []
    indexOfZero = currentState.index(0)

    toCheckIndexes = [indexOfZero + 1, indexOfZero - 1, indexOfZero - n, indexOfZero + n]
    # check if right border
    if indexOfZero % n == n - 1:
        toCheckIndexes.pop(toCheckIndexes.index(indexOfZero + 1))

    # check if left border
    if indexOfZero % n == 0:
        toCheckIndexes.pop(toCheckIndexes.index(indexOfZero - 1))
    # check if top border
    if floor(indexOfZero / n) == 0:
        toCheckIndexes.pop(toCheckIndexes.index(indexOfZero - n))
    # check if bottom border
    if floor(indexOfZero / n) == n - 1:
        toCheckIndexes.pop(toCheckIndexes.index(indexOfZero + n))

    # replaces all values of the allowedindexes with the index of the empty square and stores it in childstates
    for index in toCheckIndexes:
        newState = currentState[:]
        newState[indexOfZero] = currentState[index]
        newState[index] = 0
        states.append(newState)

    return states


if __name__ == '__main__':
    goalState = []
    #calculates the goal state for size = n
    for x in range(n * n):
        if x == n * n - 1:
            goalState.append(0)
        else:
            goalState.append(x + 1)

    #sets and shuffles the initial state
    startState = goalState[:]
    random.shuffle(startState)

    visitedStates.append(startState)
    solvePuzzle(startState, goalState)
