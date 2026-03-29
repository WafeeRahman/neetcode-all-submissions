class ListNode:
    def __init__(self):
        self.key = None
        self.val = 0
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.tail = ListNode()
        self.head = ListNode()

        self.tail.next = self.head
        self.head.prev = self.tail
        

    def get(self, key: int) -> int:
        if key in self.cache:
           node = self.cache[key]
           self.delete(node)
           self.insert(node)
           return node.val
        else:
            return -1
           

    def delete(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.head.prev
        self.head.prev = node
        prev.next = node
        node.prev = prev
        node.next = self.head

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
           newNode = self.cache[key]
           newNode.val = value
           self.delete(newNode)
           self.insert(newNode)
           return
        
        
        elif len(self.cache) == self.cap:
            delNode = self.tail.next
            self.delete(self.tail.next)
            del(self.cache[delNode.key])
    
        newNode = ListNode()
        newNode.key = key
        newNode.val = value
        self.cache[key]=newNode
        self.insert(newNode)        

        
