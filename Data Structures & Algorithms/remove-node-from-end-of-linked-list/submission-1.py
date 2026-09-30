class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        
        count = 0

        # Special case: if removing the head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        # Move fast to the end, slow will be one before the node to remove
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from end
        slow.next = slow.next.next
        return head