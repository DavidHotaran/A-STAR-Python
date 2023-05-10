from typing import List
from random import randrange
from node import Node


def create_grid(x: int, y: int, OBSTACLES: int) -> List[List[Node]]:
    '''Create a grid given x and y size, with percentage of grid nodes represented
    as 'obstacles'.

    :param: x:int = length of grid in x axis
    :param: y:int = length of grid in y axis
    :param: OBSTACLES: int = number of nodes that will be an obstacle node (non-traversable)

    return: List[List[Node]] that serves as the grid.
    '''
    grid = []
    for i in range(x):
        grid.append([Node(i,j) for j in range(y)])
    
    for _ in range(OBSTACLES):
        i = randrange(x)
        j = randrange(y)
        grid[i][j].repr = "X"

    grid[0][0].repr = "O"
    grid[x-1][y-1].repr = "O"
    
    return grid

def print_grid(grid: List[List[Node]]) -> None:
    '''Print the board to the terminal, along with x/y axis markers.
    :param: grid: List[List[Node]] = the intial grid
    '''
    inc = 0
    for i in range(0, len(grid[0])):
        print('\t', i, end="")
    print("")
    for x in grid:
        print(inc, end='\t')
        inc += 1
        for y in x:
            print(f' {y.repr}', end='\t')
        print('\n')

def print_path(stack: List[Node], grid: List[List[Node]]) -> None:
    '''Print the board and the resulting path from the a_star() function.
    :param: stack: List[Node] = the path of nodes
    :param: grid: List[List[Node]] = the intial grid
    '''
    for node in stack:
        grid[node.x][node.y].repr = '@'
    print("Path:")
    print_grid(grid)