class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         1. dp bottom-up

#         n = len(cost)
#         min_costs = [0] * (n + 1)
        
#         for i in range(2, n + 1):
#             min_costs[i] = min(min_costs[i-1]+ cost[i-1],min_costs[i-2]+ cost[i-2])

#         return min_costs[n]

#       2. dp top-down
        memo = {}
        
        def minCosts(n):
            if n == 0 or n == 1:
                return 0
            if n not in memo:
                memo[n] = min(minCosts(n-1) + cost[n-1], minCosts(n-2) + cost[n-2])
            return memo[n]
        
        minCosts(len(cost))
        return memo[len(cost)]
        
        
        