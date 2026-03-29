# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = ListNode(0)
        dummy = ListNode(0, cur)
        carry = 0 

        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val3 = val1 + val2 + carry
            carry = 0
            if val3 >= 10:
                carry = val3 // 10
                val3 =  val3 % 10
            
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            cur.val = val3
            
            if l1 or l2 or carry:
                cur.next=ListNode(0)
                cur = cur.next
        
        return dummy.next
            
            
        

