class ListNode:
    def __init__(self):
        self.key = None
        self.val = None
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
    
    def insert(self, Node):
        prev = self.head.prev
        prev.next = Node
        Node.prev = prev
        Node.next = self.head
        self.head.prev = Node
    
    def delete(self, Node):
        prev = Node.prev
        nxt = Node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
    
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.delete(node)
            self.insert(node)
        else:
            if len(self.cache) == self.cap:
                node=self.tail.next
                del(self.cache[node.key])
                self.delete(self.tail.next)
            
            node = ListNode()
            node.key = key
            node.val = value
            self.cache[key] = node
            self.insert(node)
        

        
