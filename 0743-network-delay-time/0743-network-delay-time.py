class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 다익스트라 그래프 만들기
        graph = defaultdict(list)

        for source, target, time in times:
            graph[source].append((time, target))

        print(graph)

        # 최소 비용을 구해야 하니까, 비용 기준 우선순위 큐를 만들기
        pq = []
        heapq.heappush(pq, (0, k))

        # 비용 정보들을 기록해둘 costs 객체
        costs = {}

        # pq를 돌면서 비용 합계 구하기
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            # 새로운 노드라면 비용 기록. 체크용
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                # 현재 노드에서 연결되어 있는 다른 노드들을 순차적으로 방문해야 되므로, 연결된 다른 노드들 방문 예약
                # 여기에서 비용의 합계가 필요하므로 비용은 합산해서 pq에 넣어준다.
                for cost, next_node in graph[cur_node]:
                    next_cost = cost + cur_cost
                    heapq.heappush(pq, (next_cost, next_node))

        # 전체 노드들을 순회하면서 지금까지 방문한 서로 연결된 노드에 모두 포함되는지 확인한다.
        # 연결되지 않은 노드가 있다면, 즉 방문하지 못한 노드가 있다면 -1을 반환한다.
        for i in range(1, n + 1):
            if i not in costs:
                return -1

        # 가장 최소 비용으로 기록한 비용의 합계중 가장 큰 값을 반환해야 가장 먼 거리의 n, 최종 목적지인 노드까지의 비용을 구할 수 있다.
        return max(costs.values())
