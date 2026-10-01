class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #set up adjecency list
        adj_list = {}
        whole_set = set()
        for i in range(n):
            adj_list[i] = []
            whole_set.add(i)
        
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        def dfs(node):

            visited.add(node)

            for neighbor in adj_list[node]:
                
                if neighbor not in visited:
                    dfs(neighbor)
         
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count


        


            

            

            

