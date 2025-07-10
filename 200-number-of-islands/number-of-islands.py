class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row, col = q.popleft()
                coordinates = [(1, 0), (-1, 0), (0, -1), (0, 1)]
                for dr, dc in coordinates:
                    nRow  = dr + row
                    nCol = dc + col
                    if (nRow in range(ROWS) and nCol in range(COLS) and grid[nRow][nCol] == "1" and 
                    (nRow, nCol) not in visited):
                        visited.add((nRow, nCol))
                        q.append((nRow, nCol))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r, c)
                    res += 1
                
        return res
