# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nl = ListNode()
        head = nl
        nodeOne = list1
        nodeTwo = list2

        while nodeOne and nodeTwo:
            print(nodeOne.val, nodeTwo.val)
           
            if nodeOne.val <= nodeTwo.val:
                nl.next = nodeOne
                nl = nl.next
                nodeOne=nodeOne.next
            else:
                nl.next = nodeTwo
                nl = nl.next
                nodeTwo=nodeTwo.next
        
        if nodeOne:
            nl.next = nodeOne
        if nodeTwo:
            nl.next = nodeTwo
        
        return head.next

        