# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        cur = slow.next
        prev = slow.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        head1 = head
        head2 = prev

        while head1 and head2:
            nxt1 = head1.next
            nxt2 = head2.next 

            head1.next = head2
            head2.next = nxt1

            head1 = nxt1 
            head2 = nxt2
        