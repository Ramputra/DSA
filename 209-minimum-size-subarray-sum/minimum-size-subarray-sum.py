class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        s = 0
        k = 0
        p = sum(nums)
        if p<target:
            return 0

        for i in range(len(nums)):
            s += nums[i]
            k+=1
            while s>=target: 
                p = min(p, k)
                s-=nums[j]
                j+=1
                k-=1
                if s>=target:
                    p = min(p, k)

                    
                    
                
                       
        
    
        return p