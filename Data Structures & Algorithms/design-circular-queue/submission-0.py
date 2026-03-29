class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def enQueue(self, value: int) -> bool:
        if self.k == self.length:
            return False
        else:
            insertNode = ListNode(value)
            prev = self.tail.prev
            prev.next = insertNode
            insertNode.prev = prev
            insertNode.next = self.tail
            self.tail.prev = insertNode
            self.length+=1
            return True


    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        elif self.length == 1:
            Node=self.head.next
            self.head.next = self.tail
            self.tail.prev = self.head
            self.length-=1
            return True
        else:
            nxt = self.head.next.next
            self.head.next = nxt
            nxt.prev = self.head
            self.length-=1
            return True
        

    def Front(self) -> int:
        return self.head.next.val if self.length > 0 else -1
        

    def Rear(self) -> int:
        return self.tail.prev.val if self.length > 0 else -1
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.k==self.length
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()