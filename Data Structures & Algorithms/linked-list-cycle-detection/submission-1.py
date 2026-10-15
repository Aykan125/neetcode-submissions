# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s,fast = head, head
        while fast and fast.next:
            s = s.next
            fast = fast.next.next
            if s == fast:
                return True
        return False
        