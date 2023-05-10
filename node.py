class Node:
    '''Node class representing a position on the grid
        x:int = x pos on grid
        y:int = y pos on grid
        g:int = distance traveled on grid so far
        parent:Node = pointer to parent node for animation
        repr:str = string representation of Node on grid. '*' = free space, 'O' = start/end, 'X' = obstacle
    '''
    def __init__(self, x: int, y: int, g: int = 0, h: int = 0, parent: 'Node' = None, repr: str = "*") -> None:
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = parent
        self.repr = repr
    
    '''Overload methods for priority queue.'''
    def __repr__(self) -> str:
        return f'Node({self.x},{self.y}) {self.g=} {self.h=}'

    def __lt__(self, other):
        return self.h < other.h
    
    def __gt__(self, other):
        return self.h > other.h
    
    def __eq__(self, other):
        return self.h == other.h and self.x == other.x and self.y == other.y

    def __le__(self, other):
        return self.h <= other.h
    
    def __ge__(self, other):
        return self.h >= other.h