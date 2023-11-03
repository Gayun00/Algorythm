from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        answer = 0
        
        def bfs(row, col):
            que = deque()
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            visited[row][col] = True
            que.append((row, col))
            

            while que:
                cur_row, cur_col = que.popleft()

                for r, c in directions:
                    next_row = cur_row + r
                    next_col = cur_col + c

                    if next_row <0 or next_row >=ROWS or next_col < 0 or next_col >= COLS or visited[next_row][next_col] or grid[next_row][next_col] =="0":
                        continue
                    visited[next_row][next_col] = True
                    que.append((next_row, next_col))
    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and not visited[row][col]:
                    bfs(row, col)
                    answer += 1
                    
        return answer
                
            
        