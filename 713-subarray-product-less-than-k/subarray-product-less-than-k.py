class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        j = 0
        t = 0
        p = 1
        if k<1:
            return 0

        for i in range(len(nums)):
            p*=nums[i]
            while p>=k:
                p//=nums[j]
                j+=1
            t += i-j+1
            
        return t  
