# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nl = ListNode()

        dummy = nl


        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
    
        cur = slow.next
        slow.next = None
        prev = None
        
        while cur:
            nxt= cur.next
            cur.next= prev
            prev = cur
            cur = nxt
    
        cur = head
        cur2 = prev


        while cur and cur2:
            nxt1 = cur.next
            nxt2 = cur2.next

            nl.next = cur
            nl = nl.next
            
            nl.next = cur2
            nl=nl.next

            cur = nxt1
            cur2 = nxt2

        if cur:
            nl.next = cur
        if cur2:
            nl.next = cur2
        
       


