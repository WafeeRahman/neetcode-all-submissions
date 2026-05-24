class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = {}
        for i in range(numCourses):
            preqs[i] = []
        
        for a,b in prerequisites:
            preqs[a].append(b)
        
        visit = set()
        path = []
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for nei in preqs[course]:
                print(nei)
                if not dfs(nei):
                    return False
            cycle.remove(course)
            visit.add(course)
            path.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        if len(visit) == numCourses:
                return path
        else:
            return []



        