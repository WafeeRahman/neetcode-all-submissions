# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKth(node, k):
            while k > 0:
                k-=1
                node = node.next if node else None
            return node
        dummy = ListNode(0, head)
        cur = head
        prevGroup = dummy
        prev = dummy
        while cur:
            kth = getKth(prevGroup, k)
            if not kth:
                break
            
            connection = cur
            prevGroup.next = kth
            next = kth.next
            
            while cur != next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            prevGroup = connection
            connection.next = cur

            
          
            
            

           
        return dummy.next
