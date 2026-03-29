class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##Quick Select Solution
        #Kth index is at length Nums-K
        kth = len(nums) - k
        vec = nums
        #We can do it in place, but I just used vec
        #Quick Select, Modifiied Quick Sort Algorithm
        def quickSelect(l, r):
            #Base Case, if Left == Right, then we sorted the entire array/subarr
            #Meaning that left == right == k
            if l == r:
                return vec[l]
            
            #PPVT, and Pivot for iterating and swapping
            ppvt = l
            pivot = vec[r]
            
            #For each value within the left and right range
            for i in range(l, r):
                #If the value encountered is less than pivot, swap it with ppvt
                if vec[i] <= pivot:
                    vec[i], vec[ppvt] = vec[ppvt], vec[i]
                    ppvt+=1
            
            #Final Swap, Swap PPVT value w/ Pivot Value
            #This way, everything to the left of ppvt is less, and everything 
            #To the Right is Greater.
            vec[r] = vec[ppvt]
            vec[ppvt] = pivot

            #If PPVT is at the KTH position of the array, it is the kth value
            if ppvt == kth:
                return vec[ppvt]
            #If its less than kth, then kth is on the right subbarray, and we continue to sort it
            elif ppvt < kth:
                return quickSelect(ppvt+1, r)
            else:
                return quickSelect(l, ppvt-1)
                

        return quickSelect(0, len(nums)-1)

            
            