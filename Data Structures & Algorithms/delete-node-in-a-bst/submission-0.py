class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Step 1: search for the key
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # Step 2: found it. Zero or one child: replace with the other side
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Step 3: two children. Swap in the smallest value from the right,
        # then delete that value from the right subtree
        successor = self.min_node(root.right)
        root.val = successor.val
        root.right = self.deleteNode(root.right, successor.val)
        return root

    def min_node(self, node):
        while node.left:
            node = node.left
        return node