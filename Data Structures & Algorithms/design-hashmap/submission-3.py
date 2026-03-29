class Node:
    def __init__(self):
        self.key = -1
        self.val = 0
        self.next = None
class MyHashMap:

    def __init__(self):
        self.keyStore = [Node() for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        hashed = key % len(self.keyStore)
        head = self.keyStore[hashed]
        prev = None
        while head:
            if head.key == key:
                head.val = value
                return
            prev = head
            head = head.next
        
        prev.next = Node()
        prev = prev.next
        prev.key = key
        prev.val = value
        
        return
        

    def get(self, key: int) -> int:
        hashed = key % len(self.keyStore)
        head = self.keyStore[hashed]
        prev = None
        while head:
            if head.key == key:
                return head.val 
                
            prev = head
            head = head.next
        return -1
        

        

    def remove(self, key: int) -> None:
        hashed = key % len(self.keyStore)
        head = self.keyStore[hashed]
        prev = None
        while head:
            if head.key == key:
                nxt = head.next
                prev.next = nxt
                return          
            prev = head
            head = head.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)