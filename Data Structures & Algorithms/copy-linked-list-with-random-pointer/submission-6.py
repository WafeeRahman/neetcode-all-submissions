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
        nodeMap = {}
        cur = head

        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next

        
        for key in nodeMap:
            node = nodeMap[key]
            nxt = nodeMap[key.next] if key.next else None
            rdm = nodeMap[key.random] if key.random  else None

            print(node, nxt, rdm)
            node.next = nxt
            node.random = rdm
        
        return nodeMap[head] if nodeMap else None
