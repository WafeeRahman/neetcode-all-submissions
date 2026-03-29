# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next

        while fast and fast.next:
            #base case, if slow == fast, we know we have a cycle.
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        #If either of these two pointers become null, then we dont have a cycle
        return False