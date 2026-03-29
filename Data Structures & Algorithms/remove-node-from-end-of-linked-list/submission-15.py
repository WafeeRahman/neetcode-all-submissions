# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nth = head
        while n > 0:
            nth = nth.next 
            n-=1
        cur = dummy
        while nth:
            prev = cur
            cur = cur.next
            nth = nth.next

        cur.next = cur.next.next
        
        return dummy.next
