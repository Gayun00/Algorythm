class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        solve_sudoku(board)

def solve_sudoku(grid):
    row, col = find_empty_cell(grid)
    if row == -1:
        return True

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = str(num)

            if solve_sudoku(grid):
                return True

            grid[row][col] = '.'

    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == '.':
                return (i, j)

    return (-1, -1)

def is_safe(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == str(num):
            return False

    for i in range(9):
        if grid[i][col] == str(num):
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == str(num):
                return False

    return True