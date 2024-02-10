from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        count = 0
        directions = [(1,0), (0,1), (-1,0),(0,-1)]

        def countIslands(row, col):
            que = deque()
            que.append((row, col))
            
            while que:
                cur_row, cur_col = que.popleft()
                
                for row, col in directions:
                    next_row, next_col = row + cur_row, col + cur_col

                    if next_row <0 or next_row >=ROWS or next_col < 0 or next_col >= COLS or visited[next_row][next_col] or grid[next_row][next_col] =="0":
                        continue
                    visited[next_row][next_col] = True
                    que.append((next_row, next_col))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not visited[i][j]:
                    countIslands(i, j)
                    count += 1
        
        return count