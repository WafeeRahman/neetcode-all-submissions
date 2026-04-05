class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskMap = defaultdict(int)
        taskSet = set()
        taskHeap=[]
        cycles = 0
        q = deque()
        #buildTaskHeap:
        for task in tasks:
            taskMap[task] += 1

        for key, val in taskMap.items():
            heapq.heappush(taskHeap, [-val, key])

    
        while q or taskHeap:
            
            if taskHeap:
                enqueTask = heapq.heappop(taskHeap)
                enqueTask[0] += 1
            else:
                enqueTask = None

            if enqueTask and enqueTask[0] < 0:
                q.append((enqueTask, cycles+n))
      
            if q and cycles == q[0][1]:
                finishedTask = q.popleft()[0]
                print(finishedTask[1])
        
                if finishedTask[0] < 0:
                    heapq.heappush(taskHeap, finishedTask)
         
            cycles += 1
        return cycles



                
        