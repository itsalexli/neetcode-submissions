class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        
        for i in range(numCourses):
            preMap[i] = []

        #set up pre map
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False    
            
            if not preMap[course]:
                return True
            
            visited.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            preMap[course] = []
            return True
            
            
            return True
        
        for course in preMap:
            if not dfs(course):
                    return False
        return True

            

            

