class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        onTheIsland = set()


        people.sort()
        l = 0
        r = len(people)-1
        res = 0
        while len(onTheIsland) != len(people):
            curWeight = 0

            if people[l] + people[r] > limit:
                res+=1
                onTheIsland.add(r)
                r-=1
            elif people[l] + people[r] <= limit:
                res+=1
                onTheIsland.add(r)
                onTheIsland.add(l)
                l+=1
                r-=1
        return res

                
            


            

