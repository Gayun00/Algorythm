from collections import defaultdict

def solution(info, edges):
    graph = defaultdict(list)
    answer = 0
    
    for source, target in edges:
        graph[source].append(target)
          
    def dfs(idx, sheep, wolf, possible):
        nonlocal answer
        if info[idx] == 0:
            sheep += 1
            answer = max(answer, sheep)
            
        else:
            wolf += 1
        if wolf >= sheep:
            return
        possible.extend(graph[idx])
        
        for p in possible:
            dfs(p, sheep, wolf, [i for i in possible if i!=p])
    
    dfs(0,0,0,[])
    return answer
