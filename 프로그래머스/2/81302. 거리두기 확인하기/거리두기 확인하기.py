from collections import deque

def bfs(row, col, place):
    que = deque()
    que.append((row, col, 0))
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[False] * 5 for _ in range(5)]
    visited[row][col] = True
    
    while que:
        cur_row, cur_col, cur_distance = que.popleft()
        if cur_distance > 2:
            continue
        if cur_distance != 0 and place[cur_row][cur_col] == "P":
            return False
        
        for r, c in direction:
            next_row = cur_row + r
            next_col = cur_col + c
            
            if next_row < 0 or next_row >= 5 or next_col < 0 or next_col >= 5 or visited[next_row][next_col]:
                continue
            if place[next_row][next_col] == "X":
                continue
            que.append((next_row, next_col, cur_distance + 1))
            visited[next_row][next_col] = True
            
    return True

def check(place):
    n = len(place)
    
    for row in range(n):
        for col in range(n):
            if place[row][col] == "P":
                if not bfs(row, col, place):
                    return False
    return True

def solution(places):
    answer = []
    
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    
    print(answer)
    return answer