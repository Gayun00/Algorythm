class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
#       set n+1 length to use for-in range statement
        min_costs = [-1] * (n+1)
        
#       initialize values of base cases
        min_costs[0] = 0
        min_costs[1] = 0
        
#       record minimum cost to reach each step
        for i in range(2, n+1):
#           minimum cost to reach previous step + cost to reach current step 
            min_costs[i] = min(min_costs[i-1] + cost[i-1], min_costs[i-2] + cost[i-2])
        
        return min_costs[n]