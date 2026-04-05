class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        taskHeap = []
        for task in set(tasks):
            heapq.heappush(taskHeap, [-count[ord(task)-ord('A')], task])
        
        q = deque()
        cycles = 0
        while taskHeap or q:

            if taskHeap:
                newTask = heapq.heappop(taskHeap)
                newTask[0] += 1
                if newTask[0] < 0:
                    q.append((newTask, cycles+n))
                
            
      
            if q and cycles == q[0][1]:
                finished = q.popleft()[0]
                if finished[0] < 0:
                    heapq.heappush(taskHeap, finished)
            cycles+=1
        return cycles
        
            
        

        