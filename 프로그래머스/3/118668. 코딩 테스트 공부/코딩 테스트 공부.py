def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
        
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp+1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0
        
    for row in range(alp, max_alp+1):
        for col in range(cop, max_cop+1):
            if row < max_alp:
                dp[row + 1][col] = min(dp[row+1][col], dp[row][col]+1)
            if col < max_cop:
                dp[row][col + 1] = min(dp[row][col+1], dp[row][col]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if  row >= alp_req and col >= cop_req:
                    new_alp = min(row+alp_rwd, max_alp)  
                    new_cop = min(col+cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[row][col] + cost)
    
    
    return dp[max_alp][max_cop]