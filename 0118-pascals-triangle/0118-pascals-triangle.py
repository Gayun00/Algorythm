class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            prevRow = memo[i - 1]
            curRow = memo[i]

            for j in range(1, len(memo[i]) - 1):
                curRow[j] = prevRow[j] + prevRow[j - 1]

        return memo
        