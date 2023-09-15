class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)

        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for i in range(M + 1):
            dp[i][0] = i

        for j in range(N + 1):
            dp[0][j] = j

        for i in range(M):
            for j in range(N):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i][j])

        return dp[-1][-1]