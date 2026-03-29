class Node():
    def __init__(self, key):
        self.prev = None
        self.next = None
        self.key = key
        self.val = 0

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        cache = self.cache
        if not key in cache:
            return -1
        
        else:
            node = cache[key]
            self.remove(node)
            self.insert(node)
            
            return node.val

    def put(self, key: int, value: int) -> None:
        cache = self.cache
        
        if key in cache:
            node = cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        else: 
            if len(cache) == self.capacity:
                LR = self.left.next
                self.remove(LR)
                print(LR, LR.key, LR.val)
                del(cache[LR.key])
            
            node = Node(key)
            node.val = value
            
            cache[key] = node
            self.insert(node)
        
        
            
        
        
        
