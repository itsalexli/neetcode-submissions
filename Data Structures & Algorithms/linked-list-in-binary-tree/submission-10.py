import sys
sys.setrecursionlimit(10000)

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

   
        def match(node, list_node):
            if not list_node:
                return True
            if not node or node.val != list_node.val:
                return False
            
            return match(node.left, list_node.next) or match(node.right, list_node.next)
      
            
        def dfs(node, list_node):
            if not node:
                return False
            if match(node, list_node): #check if head is a new match!
                return True
            return dfs(node.left, list_node) or dfs(node.right, list_node)
        
        return dfs(root, head)

        
       
            
            
            
            