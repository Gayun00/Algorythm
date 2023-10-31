def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
        
    dp = [[float('inf')] * (max_cop + 1) for _ in range((max_alp + 1))]
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0
    
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if a < max_alp:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
            if c < max_cop:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and  c >= cop_req:
                    new_alp = min(a + alp_rwd, max_alp)
                    new_cop = min(c + cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[a][c] + cost)
    return dp[max_alp][max_cop]
                    
