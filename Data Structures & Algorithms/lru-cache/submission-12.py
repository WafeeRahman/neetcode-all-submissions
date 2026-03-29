class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cacheMap = {}
        self.cap = capacity
        self.left = Node(0, 0)  #Dummy Left
        self.right = Node (0, 0) #Dummy Right
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        #Remove Linkages Between Prev and Next of Current Node To Remove It

    def insert(self, node):
        prev = self.right.prev
        right = self.right
        prev.next = right.prev = node
        node.prev = prev
        node.next = right
    
    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key]) #Remove Node and Place it to the Before Right
            self.insert(self.cacheMap[key]) 
            return self.cacheMap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if (key in self.cacheMap):
            self.remove(self.cacheMap[key]) #Remove Existing Key within Linked List (So we can move it to the right)
        self.cacheMap[key] = node #Replace/Insert Key
        self.insert(node)
        if (self.cap < len(self.cacheMap)):
            lru = self.left.next
            self.remove(lru)
            del self.cacheMap[lru.key]



            
        
