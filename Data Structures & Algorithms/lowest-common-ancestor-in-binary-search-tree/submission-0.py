# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        low, high = min(p.val,q.val), max(p.val,q.val)

        def dfs(node):
            if node.val == low or node.val == high:
                return node
            if low < high < node.val:
                return dfs(node.left) 
            if high > low > node.val:
                return dfs(node.right)
            if low < node.val < high:
                return node
        
        return dfs(root)
            
            


            
            



        