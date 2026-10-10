class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        cycle = self.findCycle(edges)
        if not cycle:
            return []
        
        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a,b]

    


    def findCycle(self, edges):
        n = len(edges)
        adj = {i:[] for i in range(1, n + 1)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        cycle = set()

        parent = {}
        
        def dfs(node: int, par: int):
            
            visited.add(node)
            parent[node] = par

            for nei in adj[node]:
                if nei == par:
                    continue              
                if nei in visited:
                    cycle.add(nei)
                    curr = node
                    
                    while curr != nei:
                        cycle.add(curr)
                        curr = parent[curr]
                    return True

                if dfs(nei, node):
                    return True
            
            return False
        
        dfs(1,-1)
        return cycle
    





            




        