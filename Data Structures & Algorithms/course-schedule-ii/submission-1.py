class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        res = []
        cycle = set()
        visit = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for course in preMap:
            if not dfs(course):
                return []
        
        return res
        

            

        


        


        