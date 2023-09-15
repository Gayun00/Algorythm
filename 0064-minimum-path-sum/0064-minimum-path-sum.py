class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 첫번째 열과 행들을 미리 준비. sum한다.

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # 1,1부터 첫번째 열과 행들을 이용해 sum하는데, 최소 비용 구하기 시작
        # dp 활용
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
        