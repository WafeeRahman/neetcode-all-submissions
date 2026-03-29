# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #When fast ends, slow is about halfway through the list. 
        #Motivation: Interleave First and Second Half of The List
      
        
        #Reverse the Linkages of the Second Half of the List, so that we can iterleave values starting from the last value of the second half
        #Set second to the first value of the second half, and make its next pointer to null (end of the linked list in reverse)
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        #Reverse Linkages
        
        second = prev
        first = head
        
        #Iterate through first and second and interleave them for each value in second
        while second:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second= nxt2

            

        