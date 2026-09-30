"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_hashmap = {}

        def dfs(node: Optional['Node']) -> None:
            if not node:
                return None
            if node in node_hashmap:
                return node_hashmap[node]
            
            new_node = Node(node.val)
            node_hashmap[node] = new_node

        
            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)
            
            return new_node
        
        dfs(node)
        
        return node_hashmap[node] if node else None
            

            



        