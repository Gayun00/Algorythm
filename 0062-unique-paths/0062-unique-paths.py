class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_count = [[0] * n for _ in range(m)]
        
        for i in range(n):
            path_count[0][i] = 1
        
        for j in range(m):
            path_count[j][0] = 1
            
        for i in range(1, n):
            for j in range(1, m):
                
                path_count[j][i] = path_count[j-1][i] + path_count[j][i-1]
                
        return path_count[m-1][n-1]