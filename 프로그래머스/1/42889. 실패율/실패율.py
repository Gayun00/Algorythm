import operator

def solution(N, stages):
    users = len(stages)
    result = {}
    
    for i in range(1,N+1):
        if users != 0:
            clear = stages.count(i)
        
            result[i] = clear / users
            users -= clear
        else:
            result[i]=0
    answer = sorted(result, key=lambda x: result[x], reverse=True)
    return answer