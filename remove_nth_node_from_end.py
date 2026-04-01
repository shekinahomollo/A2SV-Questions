class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        
        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next