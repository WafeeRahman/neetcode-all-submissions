# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        pos = 1
        prev = None
        cur = dummy
       

        while pos < left:
            cur = cur.next
            pos += 1
        
        
        prev = None
        prev2 = cur
        cur = cur.next
        newHead = cur
        cur2=cur
        while pos < right:
            cur2 = cur2.next
            pos+=1
        nextRight = cur2.next
        
        pos = left
        while pos <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            pos += 1
        
        prev2.next = prev
        newHead.next = nextRight

        return dummy.next
