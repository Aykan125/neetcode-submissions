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

        copyMap = {None:None} 
        dummy = head
        while head:
            copy = Node(head.val)  
            copyMap[head] = copy
            head = head.next
        head = dummy
        while head:
            copy = copyMap[head]
            copy.next = copyMap[head.next]
            copy.random=copyMap[head.random]
            head = head.next
        return copyMap[dummy]