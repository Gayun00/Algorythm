from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         다익스트라. 그래프 만들기
        graph = defaultdict(list)
        pq = []
        costs = {}
        
        for source, target, time in times:
            graph[source].append((time, target))
            
        heapq.heappush(pq, (0, k))
        
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cur_node not in costs:
                next_cost = 0
                costs[cur_node] = cur_cost
                
                for cost, next_node in graph[cur_node]:
                    next_cost = cost+cur_cost
                    heapq.heappush(pq, (next_cost, next_node))
                    
                    
        for i in range(1, n+1):
            if i not in costs:
                return -1
            
        return max(costs.values())