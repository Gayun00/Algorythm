import copy

def solution(triangle):
    ROWS = len(triangle)
    dp = copy.deepcopy(triangle)
    for row in range(ROWS - 1):
        for col in range(len(triangle[row])):
            dp[row + 1][col] = max(
                dp[row][col] + triangle[row + 1][col], dp[row + 1][col]
            )
            dp[row + 1][col + 1] = max(
                dp[row][col] + triangle[row + 1][col + 1], dp[row + 1][col + 1]
            )
    return max(dp[-1])


