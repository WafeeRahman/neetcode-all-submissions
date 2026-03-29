class Node:

    def __init__(self):
        self.val = -1
        self.next = None


class MyHashSet:

    def __init__(self):
        self.keyStore = [Node() for _ in range(10**4)] 
        
    def add(self, key: int) -> None:
        hashRes = key % len(self.keyStore)
        head = self.keyStore[hashRes]
        cur = head.next
        prev = head
        while cur:
            if cur.val == key:
                return
            prev = cur
            cur = cur.next
        prev.next = Node()
        prev = prev.next
        prev.val = key
        return

    def remove(self, key: int) -> None:
        hashRes = key % len(self.keyStore)
        head = self.keyStore[hashRes]
        cur = head.next
        prev = head
        while cur:
            if cur.val == key:
                nxt = cur.next
                prev.next = nxt 
            prev = cur
            cur = cur.next

        

    def contains(self, key: int) -> bool:
        hashRes = key % len(self.keyStore)
        cur = self.keyStore[hashRes]

        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)