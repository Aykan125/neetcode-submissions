# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        s, f = dummy, dummy
        for i in range(0, n+1):
            f = f.next
        while f:
            s = s.next
            f = f.next
        tmp = s.next
        s.next = s.next.next
        tmp.next = None
        return dummy.next
        