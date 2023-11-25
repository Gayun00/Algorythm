from collections import defaultdict, deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict()
        visited = [False] * len(rooms)
        for room, keys in enumerate(rooms):
            graph[room] = keys
        que = deque()
        que.append(0)

        while que:
            cur_room = que.popleft()
            if visited[cur_room]:
                continue
            visited[cur_room] = True

            for key in graph[cur_room]:
                que.append(key)

        return all(visited)