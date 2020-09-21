import random
import threading
from multiprocessing import Process
"""

Othello is a turn-based two-player strategy board game.

-----------------------------------------------------------------------------
Board representation

We represent the board as a 100-element list, which includes each square on
the board as well as the outside edge. Each consecutive sublist of ten
elements represents a single row, and each list element stores a piece. 
An initial board contains four pieces in the center:

    ? ? ? ? ? ? ? ? ? ?
    ? . . . . . . . . ?
    ? . . . . . . . . ?
    ? . . . . . . . . ?
    ? . . . o @ . . . ?
    ? . . . @ o . . . ? 
    ? . . . . . . . . ?
    ? . . . . . . . . ?
    ? . . . . . . . . ?
    ? ? ? ? ? ? ? ? ? ?

This representation has two useful properties:

1. Square (m,n) can be accessed as `board[mn]`. This is because size of square is 10x10,
   and mn means m*10 + n. This avoids conversion between square locations and list indexes.
2. Operations involving bounds checking are slightly simpler.
"""

# The outside edge is marked ?, empty squares are ., black is @, and white is o.
# The black and white pieces represent the two players.
EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11

# 8 directions; note UP_LEFT = -11, we can repeat this from row to row
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

def squares():
    # list all the valid squares on the board.
    # returns a list [11, 12, 13, 14, 15, 16, 17, 18, 21, ...]; e.g. 19,20,21 are invalid
    # 11 means first row, first col, because the board size is 10x10
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

def initial_board():
    # create a new board with the initial black and white positions filled
    # returns a list ['?', '?', '?', ..., '?', '?', '?', '.', '.', '.', ...]
    board = [OUTER] * 100
    for i in squares():
        board[i] = EMPTY
    
    # the middle four squares should hold the initial piece positions.
    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE
    return board

def print_board(board):
    # get a string representation of the board
    # heading '  1 2 3 4 5 6 7 8\n'
    rep = ''
    rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
    # begin,end = 11,19 21,29 31,39 ..
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
    return rep

# -----------------------------------------------------------------------------
# Playing the game

# We need functions to get moves from players, check to make sure that the moves
# are legal, apply the moves to the board, and detect when the game is over.

# Checking moves. # A move must be both valid and legal: it must refer to a real square,
# and it must form a bracket with another piece of the same color with pieces of the
# opposite color in between.

def is_valid(move):
    # is move a square on the board?
    # move must be an int, and must refer to a real square
    return isinstance(move, int) and move in squares()

def opponent(player):
    # get player's opponent piece
    return BLACK if player is WHITE else WHITE

def find_bracket(square, player, board, direction):
    # find and return the square that forms a bracket with `square` for `player` in the given
    # `direction`
    # returns None if no such square exists
    bracket = square + direction
    if board[bracket] == player:
        return None
    opp = opponent(player)
    while board[bracket] == opp:
        bracket += direction
    # if last square board[bracket] not in (EMPTY, OUTER, opp) then it is player
    return None if board[bracket] in (OUTER, EMPTY) else bracket

def is_legal(move, player, board):
    # is this a legal move for the player?
    # move must be an empty square and there has to be is an occupied line in some direction
    # any(iterable) : Return True if any element of the iterable is true
    hasbracket = lambda direction: find_bracket(move, player, board, direction)
    return board[move] == EMPTY and any(hasbracket(x) for x in DIRECTIONS)

# Making moves
# When the player makes a move, we need to update the board and flip all the
# bracketed pieces.

def make_move(move, player, board):
    # update the board to reflect the move by the specified player
    # assuming now that the move is valid
    board[move] = player
    # look for a bracket in any direction
    for d in DIRECTIONS:
        make_flips(move, player, board, d)
    return board

def make_flips(move, player, board, direction):
    # flip pieces in the given direction as a result of the move by player
    bracket = find_bracket(move, player, board, direction)
    if not bracket:
        return
    # found a bracket in this direction
    square = move + direction
    while square != bracket:
        board[square] = player
        square += direction

# Monitoring players

# define an exception
class IllegalMoveError(Exception):
    def __init__(self, player, move, board):
        self.player = player
        self.move = move
        self.board = board
    
    def __str__(self):
        return '%s cannot move to square %d' % (PLAYERS[self.player], self.move)

def legal_moves(player, board):
    # get a list of all legal moves for player
    # legals means : move must be an empty square and there has to be is an occupied line in some direction
    return [sq for sq in squares() if is_legal(sq, player, board)]

def any_legal_move(player, board):
    # can player make any moves?
    return any(is_legal(sq, player, board) for sq in squares())

# Putting it all together

# Each round consists of:
# - Get a move from the current player.
# - Apply it to the board.
# - Switch players. If the game is over, get the final score.
def play(black_strategy, white_strategy):
    # play a game of Othello and return the final board and score
    return False

def next_player(board, prev_player):
    # which player should move next?  Returns None if no legal moves exist
    return False

def get_move(strategy, player, board):
    # call strategy(player, board) to get a move
    return False

def score(player, board):
    score = 0
    if player == BLACK:
        for i in squares():
            #grotere score voor links en rechts
            if i in range(11,19):
                if board[i] == '@':
                    score += 25
            elif i in range(81,89):
                if board[i] == '@':
                    score += 25
            else:
                if board[i] == '@':
                    score += 1
    else:
        for i in squares():
            if i in range(11,19):
                if board[i] == 'o':
                    score += 25
            elif i in range(81,89):
                if board[i] == 'o':
                    score += 25
            else:
                if board[i] == '0':
                    score += 1
              
    
    return score

def score_opdrachtC(player, board):
    score = 0
    if player == BLACK:
        for i in squares():
            if board[i] == '@':
                score += 1
    else:
        for i in squares():
            if board[i] == 'o':
                score += 1
    
    return score


#Play strategies

#opdracht simpele random version:
def opdracht_A(bord,currentplayer):

    if any_legal_move(currentplayer, bord):
        
        possible_moves = legal_moves(currentplayer,bord)
        move = random.choice(possible_moves)
        make_move(move, currentplayer, bord)
        currentplayer = opponent(currentplayer)
        opdracht_A(bord,currentplayer)
    else:
        currentplayer = opponent(currentplayer)
        if not any_legal_move(currentplayer,bord):
            print("score voor:" + currentplayer + " is:" + str(score(currentplayer,bord)))
            print(print_board(bord))
        else:
            opdracht_A(bord,currentplayer)
        

def opdracht_B(bord,currentplayer,depth):

    while legal_moves(currentplayer,bord):
        possible_moves = legal_moves(currentplayer,bord)
        scoreval=-100000000
        best_move = 0
        
        for i in possible_moves:
            #print(possible_moves)
            func_score = negamax_fuction(bord,currentplayer,depth,i)
            if func_score > scoreval:
                scoreval = func_score
                best_move = i
        
        make_move(best_move, currentplayer, bord)
    
        print("beste move:" + str(best_move))
        scoreval=-100000000
        
        currentplayer = opponent(currentplayer)
    else:
        currentplayer = opponent(currentplayer)
        if any_legal_move(currentplayer, bord):
            opdracht_B(bord,currentplayer,depth)
        else:
            print(print_board(bord))
            endscore = str(score(currentplayer,bord))
            print("score voor:" + currentplayer + " is:" + endscore )
   

def negamax_fuction(bord, currentplayer,depth,move):
    #timer starten hier en depth waarde meegeven?


    #return score when depth has been reached
    if (depth ==0 or not any_legal_move(currentplayer,bord)):
       return score(currentplayer,bord)

    scores = -1000000
    
    bord_copy= list(bord)  
    make_move(move,currentplayer,bord_copy)
    currentplayer = opponent(currentplayer)
    moves = legal_moves(currentplayer,bord_copy)
    for i in moves:
            calc = negamax_fuction(bord_copy,currentplayer,depth-1,i)
            calc = calc *-1
            if( calc > scores):
                scores = calc
                
    return scores

def get_depth(arg):
    print(str(arg))

#opdracht_A(initial_board(),BLACK)
#opdracht_B(initial_board(),BLACK,5)

#opdracht_C: er zijn een aantal sleutelposities die je eigenlijk wilt hebben zie hieronder volgorde van belangrijk naar minder:
# hoekposities
# hoeken net buiten start positie
# randen van het speelveld
# daarnaast zijn er nog heel veel extra dingen mogelijk, want met alleen hogere scores voor sleutelposities red je het niet.
# beste oplossing zou machinelearning zijn tegen echte mensen, dit was ook het resultaat van project 2.4.

#opdracht_D:
#Er is een timer toegeveogd aan het begin van de negamax functie.
#Hiermee wordt na drie seconden als het goed is de depth variable geprint via get_depth() functie.
global depth1
def opdracht_D():
    depth1 = 5
    t = threading.Timer(3, get_depth,[depth1])
    t.start()
    x = threading.Thread(target = opdracht_B, args=(initial_board(),BLACK,depth1))

    x.start()
    t.join()
    x.join()

#handmatig gecheckt met een breakpoint bij de functie print na drie seconden 
#komt tot depth 2 en niet niet bij 1.
opdracht_D()


