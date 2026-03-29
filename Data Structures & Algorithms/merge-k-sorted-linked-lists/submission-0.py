# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                listOne = lists[i]
                listTwo = lists[i+1] if i+1 < len(lists) else []
                mergedLists.append(self.mergeLists(listOne, listTwo))
            lists = mergedLists
        return lists[0]

            

    def mergeLists(self, list1, list2): 
        dummy = ListNode()
        tail = dummy

        nodeOne = list1
        nodeTwo = list2

        while nodeOne and nodeTwo:

            if nodeOne.val <= nodeTwo.val:
                tail.next = nodeOne
                tail = tail.next
                nodeOne = nodeOne.next
            else:
                tail.next = nodeTwo
                tail = tail.next
                nodeTwo = nodeTwo.next
        
        if nodeOne:
            tail.next = nodeOne
        if nodeTwo:
            tail.next = nodeTwo
        return dummy.next
            
