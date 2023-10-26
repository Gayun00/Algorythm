from heapq import heappush, heappop
from collections import defaultdict

def solution(n, paths, gates, summits):
    graph = defaultdict(set)
    for source,target,time in paths:
        graph[source].add((time,target))
        graph[target].add((time,source))
        
    intensities = [float('inf')] * (n + 1)
    heap = []
    
    for gate in gates:
        intensities[gate] = 0
        heappush(heap,(0, gate))
        
    while heap:
        cur_time, cur_node = heappop(heap)
        if intensities[cur_node] < cur_time or cur_node in summits:
            continue
        for next_time, next_node in graph[cur_node]:
            time = max(cur_time, next_time)
            if intensities[next_node] > time:
                intensities[next_node] = time
                heappush(heap,(time, next_node))
                
    summits = set(summits)
    answer = [-1, float('inf')]
    
    for summit in sorted(summits):
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]
    return answer
                