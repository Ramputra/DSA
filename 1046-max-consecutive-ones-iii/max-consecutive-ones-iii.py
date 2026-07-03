class Solution(object):
    def longestOnes(self, nums, k):
        z = 0
        j = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            while z>k:
                if nums[j]==0:
                    z-=1
                j+=1
            
            maxi = max(maxi, i-j+1)

        return maxi