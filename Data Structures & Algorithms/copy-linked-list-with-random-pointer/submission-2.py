"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #copy node set it to equal next
        #
        if not head:
            return None

        dummy = head
        while head:
            tmpNext, tmpRand = head.next, head.random
            headcpy = Node(head.val)
            head.next = headcpy
            headcpy.next = tmpNext
            headcpy.random = tmpRand
            head = headcpy.next
        newHead = dummy
        newHead = newHead.next

        while newHead:
            if newHead.next:
                newHead.next = newHead.next.next
            if newHead.random:
                newHead.random = newHead.random.next
            newHead = newHead.next
        return dummy.next
            

        