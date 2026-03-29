# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        nl = ListNode(0, None)
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow2 = slow.next
        slow.next = None

        #At this point, slow is at the point right at the halfway point
        prev, curr = None, slow2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        slow2 = prev

        while slow2:
            tmp = head.next
            tmp2 = slow2.next 
            
            head.next = slow2
            head=head.next
            
            head.next = tmp
            head = head.next

            slow2=tmp2
 
    

  
    

        





        
        
        