# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        nl = ListNode(0)
        dummy = nl
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next=None
        
        prev = None
        cur = slow

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        head2 = prev
        cur = head
        while cur and head2:
            nl.next = cur
            cur = cur.next
            nl = nl.next
            nl.next = head2
            head2=head2.next
            nl=nl.next
            

        