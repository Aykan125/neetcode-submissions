# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev = groupNext
            # head = groupPrev.next
            while head != groupNext:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        return dummy.next


        
    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr