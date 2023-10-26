from collections import deque


def solution(places):
    answer = []

    def bfs(place, row, col):
        que = deque()
        que.append((row, col, 0))
        visited = [[False for _ in range(5)] for _ in range(5)]
        visited[row][col] = True
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = 0

        while que:
            cur_row, cur_col, cur_distance = que.popleft()

            if cur_distance > 2:
                continue
            if cur_distance != 0 and place[cur_row][cur_col] == "P":
                return False

            for r, c in direction:
                next_row = r + cur_row
                next_col = c + cur_col
                if next_row < 0 or next_row > 4 or next_col < 0 or next_col > 4:
                    continue
                if visited[next_row][next_col]:
                    continue
                if place[next_row][next_col] == "X":
                    continue
                visited[next_row][next_col] = True
                que.append((next_row, next_col, cur_distance + 1))
        return True

    def check(place):
        for row in range(5):
            for col in range(5):
                if place[row][col] == "P":
                    if bfs(place, row, col) == False:
                        return False
        return True

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer