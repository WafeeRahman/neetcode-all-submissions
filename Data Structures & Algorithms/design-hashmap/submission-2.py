class ListNode:
    
    def __init__(self):
        self.key = None
        self.next = None
        self.val = None

class MyHashMap:

    def __init__(self):
        self.arr = [0] * 10000001
        

    def put(self, key: int, value: int) -> None:
        #Hash function (modulus)
        hashed = key % len(self.arr)
        node = ListNode()
        node.key = key
        node.val = value
        if self.arr[hashed] == 0:    
            self.arr[hashed] = node
        else:
            head = self.arr[hashed]
            while head:
                if head.key == key:
                    head.val = value
                    return
                prev = head
                head = head.next
            prev.next = node

        

    def get(self, key: int) -> int:
        hashed = key % len(self.arr) 
        if self.arr[hashed] == 0:
            return -1
        else:
            head = self.arr[hashed]
            while head:
                if head.key == key:
                    return head.val
        return -1
        

    def remove(self, key: int) -> None:
        hashed =  key % len(self.arr)
        if self.arr[hashed] == 0:
            return 
        
        else:
            head = self.arr[hashed]
            cur = head
            prev = None

            if cur.key == key:
                self.arr[hashed] = cur.next if cur.next else 0
                return 

            prev = None
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    return
                prev = cur
                cur = cur.next
                
        return
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)