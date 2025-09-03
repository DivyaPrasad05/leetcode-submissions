from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.food = food
        self.foodI = 0
        self.score = 0

        # snake body
        self.length = 1
        self.head = (0,0)
        self.body = deque([(0, 0)])
        self.dead = False
        self.occupied = {(0,0)}

        # game mechanics
        self.movements = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

    def move(self, direction: str) -> int:
        # validate the game is valid
        if self.dead:
            return -1
        
        # validate next move
        dr, dc = self.movements[direction]
        r, c = self.head
        nr, nc = r + dr, c + dc

        # bounds check
        if nr < 0 or nr >= self.height or nc < 0 or nc >= self.width:
            self.dead = True
            return -1

        # eating
        eating = (self.foodI < len(self.food) and 
        nr == self.food[self.foodI][0] and
        nc == self.food[self.foodI][1]) 

        # tail handling and self collision
        tail = self.body[-1]
        if not eating:
            self.occupied.remove(tail)
        if (nr, nc) in self.occupied:
            self.dead = True
            return -1

        # commit the move
        self.head = (nr, nc)
        self.body.appendleft(self.head)
        self.occupied.add(self.head)
        if eating:
            self.length += 1
            self.score += 1
            self.foodI += 1
        else:
            self.body.pop()
        
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

"""
Plan:
Initialize:
- height
- weight
- food
- score
- length
    - note: longest a snake can be is 1 + len(food)
- pos of snakes head
- snake's body: dequeue (head grows, tail shrinks)
- dead flag

Move:
- change the pos of the snake's head 
    - change the pos of snakes body
- check if it ate the food
    - increase score 
    - increase the length
validation checkers:
- if it moved out of bounds
- if it moved onto itself
- index into food
"""