class ListNode:
    def __init__(self):
        self.next = None
        self.val = None
class MyHashSet:

    def __init__(self):
        self.arr = [-1] * 1000001
    
        

    def add(self, key: int) -> None:
        
        hashed = key % len(self.arr)
        

        node = ListNode()
        node.val = key
        
        if self.arr[hashed] == -1:
            self.arr[hashed] = node
            return
        
        head = self.arr[hashed]
        prev = None
        
        while head:
            if head.val == key:
                return
            
            prev = head
            head = head.next
        
        prev.next = node


        

    def remove(self, key: int) -> None:
        hashed = key % len(self.arr)
        if self.arr[hashed] == -1:
            return
        
        head = self.arr[hashed]
        
        if head.val == key:
            self.arr[hashed] = head.next if head.next else -1
            return
        
        prev = None
        while head:
            if head.val == key:
                prev.next = head.next
            
            prev = head
            head = head.next
        return


        

    def contains(self, key: int) -> bool:
        hashed = key % len(self.arr)
        if self.arr[hashed] == -1:
            return False
        head = self.arr[hashed]
        while head:
            if head.val == key:
                return True
            head = head.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)