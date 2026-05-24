class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = {}
        for i in range(numCourses):
            preqs[i] = []
        
        for a, b in prerequisites:
            preqs[a].append(b)
        

        visit = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course not in preqs or course in visit:
                return True
            
            cycle.add(course)
            visit.add(course)
            for nei in preqs[course]:
                if not dfs(nei):
                    return False
            cycle.remove(course)
            return True

        for course in preqs:
            if not dfs(course):
                return False

        return len(visit) == numCourses
                
