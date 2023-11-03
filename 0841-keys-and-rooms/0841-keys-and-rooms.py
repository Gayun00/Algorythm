from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        que = deque()
        visited = [False] * n
        visited[0] = True
        que.append(0)
        
        while que:
            cur_room = que.popleft()
            
            for key in rooms[cur_room]:
                if not visited[key]:
                    que.append(key)
                    visited[key] = True
                    
        return all(visited)
            
            
        
