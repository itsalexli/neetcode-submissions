
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}

        def copy_nodes(node):
            if node in old_to_new:
                return
            old_to_new[node] = Node(node.val)
            for nei in node.neighbors:
                copy_nodes(nei)
        
        copy_nodes(node)

        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])
        
        return old_to_new[node]


        
        





        
            

            



        