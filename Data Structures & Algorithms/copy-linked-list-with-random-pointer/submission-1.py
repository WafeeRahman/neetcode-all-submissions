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
        newToCopy = {}
        cur = head
        while cur:
            val = cur.val
            newToCopy[cur] = Node(val, None, None)
            cur = cur.next

        for i in newToCopy.keys():
            print(i)
            nxt = i.next
            rdm = i.random
            node = newToCopy[i]

            node.next = newToCopy[nxt] if nxt else None
            node.random = newToCopy[rdm] if rdm else None
        return newToCopy[head] if newToCopy else head
