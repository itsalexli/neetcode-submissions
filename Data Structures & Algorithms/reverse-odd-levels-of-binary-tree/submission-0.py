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
                for i in range(n - 1, -1, -1):
                    node = q.popleft()
                    reversed_arr[i] = node.val
                    q.append(node)
            
            print(reversed_arr)

            curr_num = 0

            for i in range(n):
                node = q.popleft()              
                
                if level % 2 != 0: #if level is even
                    node.val = reversed_arr[curr_num]
                    curr_num += 1
                    
                #append children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return root
        
                

                
        


        