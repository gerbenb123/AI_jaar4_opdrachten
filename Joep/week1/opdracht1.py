leftSide = ["F", "C", "G", "W"]
goalState = ["F", "C", "G", "W"]
rightSide = []
possibleCombinations = [["F", "C", "G", "W"], ["F", "C", "W"], ["F", "G"], ["G"], ["W"], ["C"]]
allowedMoves = [["F"], ["F", "C"], ["F", "G"], ["F", "W"]]
rememberstates = []

def findAllPaths(currentState, path):
    path.append(currentState)

    if currentState[1] == set(goalState):
        return path


    paths = []

    for state in nextStates(currentState):
        if state not in path:
            newPaths = findAllPaths(state, path)
            for newPath in newPaths:
                paths.append(newPath)

    return paths


def nextStates(currentState):
    nextStates = []
    for move in allowedMoves:
        #currentState[2] is the last direction
        #TODO: no copied code
        if currentState[2] == 1 and all(x in currentState[0] for x in move):
            newLeftSide, newRightSide = currentState[0].copy(), currentState[1].copy()
            for item in move:
                newLeftSide.remove(item)
                newRightSide.add(item)
            for combination in possibleCombinations:
                if newLeftSide == set(combination) or newRightSide == set(combination):
                    newDirection = currentState[2] * -1
                    nextStates.append([newLeftSide, newRightSide, newDirection])

        if currentState[2] == -1 and all(x in currentState[1] for x in move):
            newLeftSide, newRightSide = currentState[0].copy(), currentState[1].copy()
            for item in move:
                newLeftSide.add(item)
                newRightSide.remove(item)
            for combination in possibleCombinations:
                if newLeftSide == set(combination) or newRightSide == set(combination):
                    newDirection = currentState[2] * -1
                    nextStates.append([newLeftSide, newRightSide, newDirection])

    return nextStates


if __name__ == "__main__":
    direction = 1
    initState = [set(leftSide), set(rightSide), direction]
    path = []
    allPaths = findAllPaths(initState, path)

    for path in allPaths:
        print("".join(path[0]) + "|" + "".join(path[1]))
