class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        values = nums
        values = sorted(values)

        for i, v in enumerate(values):
            if v > 0: 
                continue
            
            if i>1 and v == values[i-1]:
                continue

        
            l = i+1
            r = len(values)-1

            while l<r:

                if v +  values[l] + values[r] > 0:
                    r-=1
                elif v+ values[l] + values[r] < 0:
                    l+=1
                
                else:
                    if not ( [v,values[l],values[r]] in res):
                        res.append([v, values[l], values[r]])   
                    r-=1
                    l+=1
                    
                    while l < r and values[l] == values[l-1]:
                        l+=1
                            
        return res
                        

            