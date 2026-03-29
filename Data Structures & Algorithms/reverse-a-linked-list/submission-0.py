# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        
        #For the first instances of prev and cur, we have Null and the head
        #As we'll swap linkages with the first node, which has nothing preciding it, and will point to nothing as next
        
        while cur:
           
           #Store the next value, as we reverse the linkage to previous
           nxt = cur.next
           cur.next = prev

           #Make Previous Current, and move Cur pointer to Nxt
           prev = cur
           cur = nxt
        return prev