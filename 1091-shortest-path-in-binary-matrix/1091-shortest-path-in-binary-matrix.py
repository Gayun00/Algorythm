from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        que = deque()
        direction = [(0,1), (1,1), (1,0), (-1,-1), (0,-1), (-1,0), (-1,1), (1,-1)]
        
        que.append((0, 0, 1))
        visited = [[float('inf')] * n for _ in range(n)]
        visited[0][0] = 1
        
        
        while que:
            cur_row, cur_col, cur_distance = que.popleft()
            if grid[cur_row][cur_col]:
                return -1
            
            for row,col in direction:
                next_row, next_col = cur_row+row, cur_col+col
                next_distance = cur_distance + 1
                
                if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                    continue
                if grid[next_row][next_col]:
                    continue
                if visited[next_row][next_col] <= next_distance:
                    continue
                que.append((next_row, next_col, next_distance))
                visited[next_row][next_col] = next_distance
                    
        if visited[-1][-1] == inf:
            return -1
        else:
            return visited[-1][-1]
        