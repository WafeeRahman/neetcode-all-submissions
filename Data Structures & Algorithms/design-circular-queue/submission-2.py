class Node:
    def __init__(self):
        self.next = None
        self.val = -1
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.length = 0
        self.cap = k
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def enQueue(self, value: int) -> bool:
        if self.length == self.cap:
            return False

        prev = self.tail.prev
        newNode = Node()
        newNode.val = value

        self.tail.prev = newNode
        newNode.prev = prev
        newNode.next = self.tail
        prev.next = newNode
        self.length+=1
        return True
        

    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.length -= 1
        return True      

    def Front(self) -> int:
        return self.head.next.val
        

    def Rear(self) -> int:
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()