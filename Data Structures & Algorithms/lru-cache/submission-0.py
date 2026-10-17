class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hMap = {}
        self.right, self.left = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self, node):
        nxt = self.right
        nxt.prev.next = node
        node.prev = nxt.prev
        nxt.prev = node
        node.next = nxt   

    def get(self, key: int) -> int:
        if key in self.hMap:
            self.remove(self.hMap[key])
            self.insert(self.hMap[key])
            return self.hMap[key].value
        return -1        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.hMap:
            self.remove(self.hMap[key])
            self.insert(node)
            self.hMap[key] = node
        else:
            self.hMap[key] = node
            self.insert(node)
            if len(self.hMap)>self.cap:
                dNode = self.left.next
                self.remove(dNode)
                del self.hMap[dNode.key]
        return None

        
