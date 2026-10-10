class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #always in order and exist for 1 - n?
        #will always be connected
        #always be an answer? what happens if doensn't
        #are self loops allowed?


        #1. find edges that have cycles
        #1, 3, 4 has cycle -> 

        #build adjacency list
        
        #run dfs, if reached node that's NOT parent, 
        #visiting
        #finished


        #return visited set -> "bad" nodes: creates cycles

        #2. remove last found edge of cycle
        #go backwards through array to find last combo of edges

        #check backwards if any of the nodes contain "bad" nodes.
        #return that one
        if not edges:
            return []

        cycle = self.findCycle(edges)

        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]
        return []

    
    def findCycle (self, edges: List[List[int]]) -> set():
        #find n
        n = len(edges)
        #adj list
        adj = [[] for _ in range(n + 1)]
        
        for a, b in edges:
            #MUST ADD BOTH
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        cycle = set()
        #undirected graph: only need visiting
     
        def dfs(node: int, parent: int) -> bool:

            if node in visited:
                return node
            
            visited.add(node)
            
            #go through all neighbours
            for nei in adj[node]:
                #if neighbours = parent, continue
                if nei == parent:
                    continue
                
                start = dfs(nei, node)
                if start is not None:
                    if start != -1:
                        cycle.add(node)
                        if node == start:
                            return -1
                    return start
            return None
        
        dfs(1, -1)
        return cycle


            

            
            
            





        




