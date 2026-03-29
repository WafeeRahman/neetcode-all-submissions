# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i] if i <= len(lists)-1 else None
                l2 = lists[i+1] if i+1 <= len(lists) -1 else None
                mergedLists.append(self.mergeLists(l1, l2))
                print(mergedLists)
            lists = mergedLists
        return lists[0]
        
        



    def mergeLists(self, l1, l2):
        nl = ListNode(0, None)
        dummy = nl
        
        while l1 and l2:
            if l1.val <= l2.val:
                nl.next = l1
                l1=l1.next
            else:
                nl.next = l2
                l2=l2.next
            nl = nl.next
        
        if l1:
            nl.next = l1
        if l2:
            nl.next = l2
        
        return dummy.next
