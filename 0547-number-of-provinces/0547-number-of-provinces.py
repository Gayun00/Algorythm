class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            for index, connected in enumerate(isConnected[node]):
                if index not in visited and connected == 1:
                    dfs(index)

        for node in range(len(isConnected)):
            if node not in visited:
                count += 1
                dfs(node)
            
        return count