# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        nodes = 0 
        while first:
            nodes += 1
            first = first.next
            
        second = head
        count = 0
        if nodes == n:
            head = head.next
    
        while second:
            n+=1
            if (count == nodes-n):
                print(second.val, "HIIII")
                nxt = second.next.next
                second.next = nxt
            else:
                second = second.next
        return head 
        