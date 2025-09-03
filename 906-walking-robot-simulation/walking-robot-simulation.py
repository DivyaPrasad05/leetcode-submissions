class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Plan:
        - -2 (counterclockwise)
        - -1 (clockwise)
        - 1-9 move in the direction
        - max point from origin (ED)

        Variables / ds:
        - current pos (x, y)
        - direction: default (north)
        0 - N, 1 - E, 2 - S, 3 - W
        if 0 and -2 -> make it west
        - max pos 
        """
        obs = set()
        for o in obstacles:
            obs.add(tuple(o))
        
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]
        d = 0 # faces north
        x = y = 0
        best = 0

        for c in commands:
            if c == -2:
                d = (d - 1) % 4 # turn left + changes direction
            elif c == -1:
                d = (d + 1) % 4 # turn right + changes direction
            else:
                dx, dy = dirs[d]
                for i in range(c):
                    nx, ny = dx + x, dy + y
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    best = max(best, x * x + y * y)
        return best