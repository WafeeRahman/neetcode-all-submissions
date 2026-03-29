# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        count = 0
        preceding = dummy
        cur = head  
        while cur:
            if count >= n:
                preceding = preceding.next
            cur = cur.next
            count += 1 

           

        preceding.next = preceding.next.next

        return dummy.next
        