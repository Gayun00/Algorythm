from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
       # 기본 그래프 만들기
        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append((time[2], time[1]))

        pq = []
        costs = {}

        # 우선순위큐로 pq에 첫번째 값 넣기. 정렬된 상태로 추가 및 삭제
        #cost가 적은 순으로 우선순위 정렬이 되어야 한다. 
        # 그래야 최소 비용 기준으로 계산이 가능
        heapq.heappush(pq, (0, k))

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            # 이동 총 비용 계산
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                # 다음 큐에 푸시 - 해당 노드를 아직 순회하지 않았으니 순회할 것들을 큐에 푸시해둔다.
                # 단, 현재까지 이동한 것에 대한 비용은 더해준다.
                for cost,next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_node))

        # 계산이 끝난 후에도 모든 노드가 시그널을 받지 못했다면 -1을 반환한다.
        # 순회하면서 Costs에 기록해두었으니 Costs에 없다는 것은 시그널을 받지 못했다는 것을 의미한다.
        for node in range(1, n + 1):
            if node not in costs:
                return -1

        # 각 노드를 순회하는데 필요한 총 비용은 costs의 가장 최댓값과 같다.
        return max(costs.values())
