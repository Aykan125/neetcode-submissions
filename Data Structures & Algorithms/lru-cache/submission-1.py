class ListNode:
    def __init__(self, next=None, prev=None, val=None, key=None):
        self.next = next
        self.val = val
        self.prev = prev
        self.key = key
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.left = ListNode()
        self.right = ListNode()
        self.left.next, self.right.prev = self.right, self.left

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = node
        nxt.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.add(self.mapping[key])
            return self.mapping[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.mapping[key] = ListNode(None,None,value, key)
            self.add(self.mapping[key])
        else:
            if len(self.mapping) == self.capacity:
                del self.mapping[self.left.next.key]
                self.remove(self.left.next)
            self.mapping[key] = ListNode(None, None, value, key)
            self.add(self.mapping[key])

