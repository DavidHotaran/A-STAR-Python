from grid import create_grid, print_path, print_grid
from typing import List, Optional
from node import Node
import heapq

'''Constants'''
X = 5                         # Board width 
Y = 5                         # Board height
GOAL_X = X-1                  # Goal Node x position
GOAL_Y = Y-1                  # Goal Node y position
OBSTACLES = int((X*Y) * .20)  # Amount of nodes we want as obstacles (default 20% of nodes)

def a_star(grid: List[List[Node]], verbose=False) -> Optional[bool]:
    ''''A* algorithm. Compute the shortest path to end node from starting node.
    :param: grid: List[List[Node]] = the intial grid of nodes.
    :param: verbose: bool = if True print debugging information.

    return: Optional[bool] - if we did not find a path - return false, otherwise animate path.
    '''
    start = grid[0][0]     # starting node
    closed = []            # nodes that have been traversed already
    open = [(0, start)]    # priority queue
    distance_traveled = 0  # how far have we moved so far from the beginning

    while open:
        current = heapq.heappop(open)[1] # queue = [(manhattan, Node)]
        closed.append(current)
        distance_traveled += 1

        if verbose:
            print("current", current)

        if at_goal(current.x, current.y):
            if verbose:
                print("got to the goal")
            animate(current.parent)
            return

        neighbors = get_neighbors(current.x, current.y)
        for node in neighbors:
            if verbose:
                print("got node", node)
            heuristic = manhattan(node.x, node.y)
            node.g = distance_traveled
            node.h = heuristic
            
            if node in closed: # we do not want to add nodes to the queue that have already been discovered
                if verbose:
                    print(f'in closed: {node}')
                continue
            for item in open:
                if node == item[1]:
                    if node.g > open[0][1].g:
                        continue
            node.parent = current
            heapq.heappush(open, (heuristic, node))
    return False
        
def animate(node: Node) -> None:
    '''After we have found an answer, animate the path taken.
    :param: node: Node = the parent to the end node.
    '''
    stack = []
    while node.parent:
        stack.append(node)
        node = node.parent
    print_path(stack, grid)

def manhattan(x: int, y: int) -> int:
    '''Calculate manhattan distance.
    :param: x: int = the x position of a node.
    :param: y: int = the y position of a node.

    return: int = the manhattan distance of this node.
    '''
    return abs(x - GOAL_X) + abs(y - GOAL_Y)


def at_goal(x: int, y: int) -> bool:
    '''Return true if we are at the goal node, false otherwise.
    :param: x: int = the x position of a node.
    :param: y: int = the y position of a node.

    return: bool = T/F if we are at the goal node.
    '''
    if x == GOAL_X and y == GOAL_Y:
        return True
    return False

def get_neighbors(x: int, y: int) -> List[Node]:
    '''Return N,S,E,W neighbors of a node.
    :param: x: int = the x position of a node.
    :param: y: int = the y position of a node.

    return: List[Node] = a list of all neighbor nodes that are in bounds and not an obstacle.
    '''
    neighbors = []
    if y + 1 < Y and grid[x][y+1].repr != 'X': # S
        neighbors.append(grid[x][y+1])
    if x - 1 >= 0 and grid[x-1][y].repr != 'X': # E
        neighbors.append(grid[x-1][y])
    if y - 1 >= 0 and grid[x][y-1].repr != 'X': # N
        neighbors.append(grid[x][y-1])
    if x + 1 < X and grid[x+1][y].repr != 'X': # W
        neighbors.append(grid[x+1][y])

    return neighbors


if __name__ == '__main__':
    grid = create_grid(X, Y, OBSTACLES)
    print("\nIntial grid:")
    print_grid(grid)
    print("")
    print('*'*50, '\n')
    path_not_found = a_star(grid)
    if path_not_found:
        print("no path found :(")