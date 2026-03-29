# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None
        if len(lists) == 1:
            return lists[0]

        def merge(l1, l2):

            nl = ListNode()
            dummy = nl
            while l1 and l2:
                if l1.val <= l2.val:
                    nl.next = l1
                    l1 = l1.next
                else:
                    nl.next = l2
                    l2=l2.next
                nl = nl.next


            if l1:
                nl.next = l1
            if l2:
                nl.next = l2
            return dummy.next

        while len(lists) > 1:
            lists[0] = merge(lists[0], lists.pop())

        return lists[0] 
        