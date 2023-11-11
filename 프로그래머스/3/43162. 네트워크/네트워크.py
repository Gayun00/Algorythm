from collections import deque

def solution(n, computers):
    visited = [False] * n  # Use a single list to track visited computers.
    answer = 0

    def bfs(start):
        que = deque([start])
        while que:
            computer = que.popleft()
            visited[computer] = True
            for connect in range(n):  # Check all computers for a connection.
                if computers[computer][connect] == 1 and not visited[connect]:
                    que.append(connect)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1  # Increment network count for each BFS call.

    return answer