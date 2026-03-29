class Node:
    def __init__ (self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if not (key in self.cache.keys()):
            return -1
        else:
            res = self.cache[key]
            self.remove(res)
            self.insert(res)
            return res.val
        

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.cache.keys():
            self.remove(self.cache[key])
        
        self.cache[key] = newNode
        
        if len(self.cache) > self.capacity:
            nodeToRemove = self.left.next
            del(self.cache[nodeToRemove.key])
            self.remove(nodeToRemove)
        
        
        
        self.insert(newNode)
        

        
            