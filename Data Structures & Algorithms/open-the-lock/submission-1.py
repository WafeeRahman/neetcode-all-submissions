class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        q = deque(["0000"])
        
        visit = set("0000")
        res = 0 

        if "0000" in deadends:
            return -1
        while q:
            for _ in range(len(q)):
                
                curr = q.popleft()
                if curr == target:
                    return res
                for i in range(4):
                    digit = int(curr[i])

                    for move in [-1, 1]:
                        newMove = (digit+move) %10
                        nxt = curr[:i] + str(newMove) + curr[i+1:]

                        if not nxt in visit and nxt not in dead:
                            visit.add(nxt)
                            q.append(nxt)

            res += 1
        return -1
