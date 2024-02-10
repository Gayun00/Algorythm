from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        que = []
        costs = {}
        
        for source, target, time in times:
            graph[source].append((time, target))
            
        heapq.heappush(que, (0, k))
        
        while que:
            cur_time, source = heapq.heappop(que)
            if source not in costs:
                costs[source] = cur_time
                for next_time,target in graph[source]:
                    heapq.heappush(que, (cur_time + next_time, target)) 
        
        for i in range(1, n+1):
            if i not in costs:
                return -1
        return max(costs.values())