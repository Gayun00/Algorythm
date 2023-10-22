class Status():
    INITIAL = 1
    IN_PROGRESS = 2
    FINISHED = 3


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        
        for pre, crs in prerequisites:
            graph[crs].append(pre)
            
        statuses = {i: Status.INITIAL for i in range(numCourses)}
            
        def can_finish(crs):
            if statuses[crs] == Status.IN_PROGRESS:
                return False
            if statuses[crs] == Status.FINISHED:
                return True
        
            statuses[crs] = Status.IN_PROGRESS
            
            for pre in graph[crs]:
                if not can_finish(pre):
                    return False
            statuses[crs] = Status.FINISHED
            return True
        
        return all(can_finish(src) for src in graph)
            
        print(graph)