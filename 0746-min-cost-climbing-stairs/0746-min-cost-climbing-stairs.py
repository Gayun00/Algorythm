class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def dp(n):
            if n == 0:
                return 0 
            if n == 1:
                return 0
            if n not in memo:
                memo[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
            return memo[n]
            
        result = dp(len(cost))
        return result
