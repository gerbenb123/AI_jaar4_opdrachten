import random
import heapq
import math
import config as cf

# global var
grid  = [[0 for x in range(cf.SIZE)] for y in range(cf.SIZE)]

class PriorityQueue:
    # to be use in the A* algorithm
    # a wrapper around heapq (aka priority queue), a binary min-heap on top of a list
    # in a min-heap, the keys of parent nodes are less than or equal to those
    # of the children and the lowest key is in the root node
    def __init__(self):
        # create a min heap (as a list)
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    # heap elements are tuples (priority, item)
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    # pop returns the smallest item from the heap
    # i.e. the root element = element (priority, item) with highest priority
    def get(self):
        return heapq.heappop(self.elements)[1]

def bernoulli_trial(app):
    return 1 if random.random() < int(app.prob.get())/10 else 0

def get_grid_value(node):
    # node is a tuple (x, y), grid is a 2D list [x][y]
    return grid[node[0]][node[1]]

def set_grid_value(node, value): 
    # node is a tuple (x, y), grid is a 2D list [x][y]
    grid[node[0]][node[1]] = value

def search(app, start, goal):
    #i = colomn verticaal
    #N = waardes van colomn verticaal
    for i in grid:
        xas = grid.index(i)
        for index, item in enumerate(i):
            
            print(index, item)
            if item == 'b':
                set_grid_value((xas,index),-100)
            else:
                #hier heuristic value neerzetten maybe iets van x + y zodat de waardes groter worden richting het eindpunt,
                #of juist zodat de nodes in het midden van het bord juist de beste scores houden.
                set_grid_value((xas,index), 10)
                
    
    for i in grid:
        #dit is [] met y=0 en x = 0 
        print(i)
         


    # plot a sample path for demonstration
    for i in range(cf.SIZE-1):

        app.plot_line_segment(i, i, i, i+1, color=cf.FINAL_C)
        app.plot_line_segment(i, i+1, i+1, i+1, color=cf.FINAL_C)
        app.pause()
