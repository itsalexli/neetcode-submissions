# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        q = deque()
        q.append(root)
        level = 0
        while q:
            n = len(q)    

            reversed_arr = [0] * n
            if level % 2 != 0:
                l, r = 0, n - 1
                while l < r:
                    q[l].val, q[r].val = q[r].val, q[l].val #swap values
                    l += 1
                    r -= 1

            for i in range(n):
                node = q.popleft()              
                #append children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return root

        #O(n) time: goes through all the nodes once, O(n) space
        
        

                
        


        