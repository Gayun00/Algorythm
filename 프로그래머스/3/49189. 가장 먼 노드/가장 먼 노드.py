from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    INF = float('inf')
    
    for source, target in edge:
        graph[source].append(target)
        graph[target].append(source)
        
    que = deque()
    distance = [INF] * (n+1)
    distance[1] = 0
    que.append(1)
    
    while que:
        cur_node = que.popleft()
        
        for next_node in graph[cur_node]:
            if distance[next_node] == INF:
                distance[next_node] = distance[cur_node] + 1
                que.append(next_node)
                
    return distance[1:].count(max(distance[1:]))