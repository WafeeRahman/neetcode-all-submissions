"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ptrMap = {}
        
        cur = head

        while cur:
            ptrMap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            ptrMap[cur].next = ptrMap[cur.next] if cur.next else None
            ptrMap[cur].random = ptrMap[cur.random] if cur.random else None
            cur = cur.next
        return ptrMap[head]