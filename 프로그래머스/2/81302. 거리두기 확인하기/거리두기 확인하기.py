from collections import deque


def solution(places):
    answer = []

    def bfs(row, col, place):
        ROWS, COLS = len(place), len(place[0])

        que = deque()
        que.append((row, col, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * COLS for _ in range(ROWS)]

        while que:
            cur_row, cur_col, cur_distance = que.popleft()
            visited[cur_row][cur_col] = True
            if 0 < cur_distance <= 2 and place[cur_row][cur_col] == "P":
                return False
            for r, c in directions:
                next_row, next_col = r + cur_row, c + cur_col

                if next_row < 0 or next_row >= ROWS or next_col < 0 or next_col >= COLS:
                    continue

                if visited[next_row][next_col] or place[next_row][next_col] == "X":
                    continue

                que.append((next_row, next_col, cur_distance + 1))
        return True

    def checkPlace(place):
        ROWS, COLS = len(place), len(place[0])

        for row in range(ROWS):
            for col in range(COLS):
                if place[row][col] == "P":
                    if not bfs(row, col, place):
                        return False
        return True

    for place in places:
        if checkPlace(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer


