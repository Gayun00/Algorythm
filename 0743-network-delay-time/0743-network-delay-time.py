from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            [source, target, time] = time
            graph[source].append((time, target))

        pq = []
        heappush(pq, (0, k))
        times = {}
        count = 0

        while pq:
            cur_time, cur_node = heappop(pq)

            if cur_node not in times:
                times[cur_node] = cur_time

                for next_time, next_node in graph[cur_node]:
                    heappush(pq, (next_time + cur_time, next_node))

        for i in range(1, n + 1):
            if not i in times:
                return -1    
        
        return max(times.values())