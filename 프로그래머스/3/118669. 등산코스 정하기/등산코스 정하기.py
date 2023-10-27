from heapq import heappush, heappop
from collections import defaultdict

def solution(n, paths, gates, summits):
    graph = defaultdict(set)
    for source, target, time in paths:
        graph[source].add((time, target))
        graph[target].add((time, source))
        
    intensities = [float('inf')] * (n+1)

    que = []
    for gate in gates:
        intensities[gate] = 0
        heappush(que, (0, gate))
        
    while que:
        cur_time, cur_node = heappop(que)
        if intensities[cur_node] < cur_time or cur_node in summits:
            continue
        
        for next_time, next_node in graph[cur_node]:
            intensity = max(next_time, cur_time)
            
            if intensities[next_node] > intensity:
                intensities[next_node] = intensity
                heappush(que, (intensity, next_node))
        
    answer = [-1, float('inf')]
    
    summits = set(summits)
    for summit in sorted(summits):
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]
    
    return answer