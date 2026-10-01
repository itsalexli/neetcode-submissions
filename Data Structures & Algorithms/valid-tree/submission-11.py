class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()

        adj_table = {}

        for i in range(n):
            adj_table[i] = []
        
        #place both tables
        for a, b in edges:
            adj_table[a].append(b)
            adj_table[b].append(a)

        def dfs(node, prev):
            if node in visited:
                return False
            
            #visited = {0, 
            visited.add(node)

            if not adj_table[node]:
                return True

            for neighbor in adj_table[node]:
                if prev == neighbor:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True
        
        if dfs(0, -1) and len(visited) == n:
            return True
        else:
            return False

        # 0: 1
        # 1: []
        # 2: 0
        # 3: 0
        # 4: 1, 4








        





        



        





            

            
