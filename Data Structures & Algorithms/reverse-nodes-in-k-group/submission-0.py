# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        tail = dummy
        while True:
            
            kth = self.getKth(dummy, k)
            if not (kth):
                break
        
            groupNext = kth.next
            prev, cur = kth.next, dummy.next
            
            while cur != groupNext:
                nxt = cur.next 
                cur.next = prev
                prev = cur
                cur = nxt
            tmp = dummy.next #1
            dummy.next = kth #3
            dummy = tmp
            
            print(dummy.val)
       

        return tail.next
                
    def getKth(self, node, k):
        cur = node
        while k > 0 and cur:
            k -= 1
            cur = cur.next
        return cur if k == 0 else None
            
        