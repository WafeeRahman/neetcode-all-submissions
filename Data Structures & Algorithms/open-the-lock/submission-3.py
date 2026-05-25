class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        visit = set("0000")
        q = deque(["0000"])
        level = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return level
                
                for i in range(4):
                    digit = int(curr[i])
                    
                    for nextState in [-1,1]:
                        nxt = (digit + nextState) % 10
                        nxtStr = curr[:i] + str(nxt) + curr[i+1:]
                        
                        if not nxtStr in visit and not nxtStr in dead:
                            visit.add(nxtStr)
                            q.append(nxtStr)
            level += 1
        return -1