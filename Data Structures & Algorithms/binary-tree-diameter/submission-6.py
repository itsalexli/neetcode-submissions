# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diameter

        
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)

        curr_d = left + right
        self.diameter = max(self.diameter, curr_d)

        self.dfs(node.left)
        self.dfs(node.right)
    
    
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

