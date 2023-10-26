from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        pq = []
        costs = {}
        for time in times:
            [source, target, distance] = time
            graph[source].append((distance, target))
        heap = heapq.heappush(pq, (0, k))
        
        while pq:
            cur_distance, cur_node = heapq.heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_distance
                next_cost = 0
                
                for next_distance, next_node in graph[cur_node]:
                    heapq.heappush(pq, (next_distance + cur_distance, next_node))    
        
        for i in range(1, n + 1):
            if not i in costs:
                return -1
            
        
        return max(costs.values())
        
        
