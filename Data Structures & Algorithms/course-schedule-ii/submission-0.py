class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
      
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])

        res = []
        visit = set()
        cycleCheck = set()

        def dfs(node, visit, cycleCheck):
            nonlocal res
            if node in cycleCheck:
                return False
            if node in visit:
                return True
            
            cycleCheck.add(node)
            for neighbour in adjList[node]:
                if not dfs(neighbour, visit, cycleCheck):
                    return False
            
            cycleCheck.remove(node)
            visit.add(node)
            res.append(node)
           
            return True
        
        for i in range(numCourses):
            if not dfs(i,visit,cycleCheck):
                return []
        return res

        
        
                