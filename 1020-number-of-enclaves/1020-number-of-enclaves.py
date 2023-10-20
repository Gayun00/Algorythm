class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        
        land = 0
        borderedLand = 0
        visited = set()

        def dfs(row, col):
            count = 1
            
            if row < 0 or row == ROWS or col < 0 or col == COLS or not grid[row][col] or (row, col) in visited: 
                return 0
            for dr, dc in dir:
                visited.add((row, col))
                count += dfs(row + dr, col + dc)

            
            return count
        
        
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    land += 1
                if grid[row][col] == 1 and (col in [0,COLS-1] or row in [0, ROWS-1]):
                    borderedLand += dfs(row, col)
        
        
        return land - borderedLand

                    
        