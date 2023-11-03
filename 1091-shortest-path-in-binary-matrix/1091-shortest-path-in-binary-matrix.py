from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        que = deque()
        que.append((0, 0, 1))
        directions = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,-1),(-1,1)]
        distance = [[float('inf')] * COLS for _ in range(ROWS)]
        distance[0][0] = 1
        
        while que:
            cur_row, cur_col, cur_distance = que.popleft()
            if grid[cur_row][cur_col]:
                return -1
            
            for r, c in directions:
                next_row = r + cur_row
                next_col = c + cur_col
                
                next_distance = cur_distance + 1
                
                if next_row < 0 or next_row >= ROWS or next_col < 0 or next_col >= COLS:
                    continue
                if grid[next_row][next_col]:
                    continue
                if distance[next_row][next_col] <= next_distance:
                    continue
                distance[next_row][next_col] = next_distance
                que.append((next_row, next_col, next_distance))
                
                
        if distance[-1][-1] == inf:
            return -1
        else:
            return distance[-1][-1]
                
                
                
            