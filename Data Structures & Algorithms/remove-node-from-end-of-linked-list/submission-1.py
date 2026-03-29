# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Linear Time Solution in Two Passes, Count the Amount of Nodes
        first = head
        nodes = 0 
        while first:
            nodes += 1
            first = first.next

        #After The First Pass, Find the Value Before the Nth from End Value
        #Remove its linkage by linking the preceding value to the value after it
        second = head
        count = 0
        #If the amount of nodes we have is less than or equal to n, then we know
        if nodes <= n:
            head = head.next
    
        while second:
            #Pre increment will make sure we find the value that precedes what we want to remove
            n+=1 
            if (count == nodes-n):
                nxt = second.next.next
                second.next = nxt
            else:
                second = second.next
        return head 
        