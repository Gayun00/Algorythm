class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        negative = set()
        positive = set()
        
        board = [['.'] * n for _ in range(n)]
        res = []
        
        def backtrack(row):
            if row == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            

            
            for col in range(n):
                if col in columns or row+col in positive or row-col in negative:
                    continue
                columns.add(col)
                negative.add(row-col)
                positive.add(row+col)
                board[row][col] = "Q"
                
                backtrack(row+1)
                
                columns.remove(col)
                negative.remove(row-col)
                positive.remove(row+col)
                board[row][col] = "."
                
        backtrack(0)
        return res
                
                
                
                
                
            