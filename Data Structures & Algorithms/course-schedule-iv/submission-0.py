from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        
        def dfs(node, target):
            if node in visited:
                return False

            if node == target:
                return True
            
            visited.add(node)
            
            for nei in adj[node]:
                if nei == node or nei in visited:
                    continue
                if dfs(nei, target):
                    return True
            
            return False
            
        res = []
        for start, target in queries:
            visited = set()
            res.append(dfs(start,target))
        
        return res

            
            

            

            