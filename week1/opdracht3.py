finished = False

s =[
[0,0,0,0,0,0,0,0,81],
[0,0,46,45,0,55,74,0,0], 
[0,38,0,0,43,0,0,78,0],
[0,35,0,0,0,0,0,71,0],
[0,0,33,0,0,0,59,0,0],
[0,17,0,0,0,0,0,67,0],
[0,18,0,0,11,0,0,64,0],
[0,0,24,21,0,1,2,0,0],
[0,0,0,0,0,0,0,0,0]
]

print(s)
neighbourlist=[]
#vindt een pad van 1 naar 81

def get_neighbours(x,y):
    neighbourlist=[]


    if x == 8:
          neighbourlist.append([x-1,y])
    elif x == 0:
        neighbourlist.append([x+1,y])
    else:
        neighbourlist.append([x-1,y])
        neighbourlist.append([x+1,y])
    
    if y == 8:
        neighbourlist.append([x,y-1])
    elif y == 0:
        neighbourlist.append([x,y+1])
    else:
        neighbourlist.append([x,y-1])
        neighbourlist.append([x,y+1])
        


    return neighbourlist


def print_endresult(board):
   
    for i in board:
        print(i)

    finished = True
    

#start met clue 1.
def solve(posx,posy,steps,clue,board):
    #in het board
    #zoek je mogelijke paden.
    

    board_copy1 = list(board)

    if board_copy1[posy][posx] == clue:
        #hier copy of list
        move_list = get_neighbours(posx,posy)
        
        #check if neighbours has next clue
        for i in move_list: 
            if board_copy1[i[1]][i[0]] == clue+1:
                if board_copy1[i[1]][i[0]] == 81:
                    print_endresult(board_copy1)

                return solve(i[0],i[1],steps+1,clue+1,board_copy1)
                
                
    
        for i in move_list:
            if board_copy1[i[1]][i[0]] == 0:
                board_copy1[i[1]][i[0]] = int(steps+1)
                if not solve(i[0],i[1],steps+1,clue+1,board_copy1):
                    board_copy1[i[1]][i[0]] = 0
            
        if finished == True:
            return True
        else:
            return False   

#find starting position 
for i in s:
    if 1 in i:
        
        print("x:" , i.index(1))
        print("y:" , s.index(i))
        solve(i.index(1),s.index(i),1,1,s)
    

