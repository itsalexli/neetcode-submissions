class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adj =  {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        visiting = set()
        finished = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if node in finished:
                return True

            visiting.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            finished.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
                
            

            

