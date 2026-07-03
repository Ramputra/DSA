class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi = 0
        s = 0
        for i in range(len(nums)):
            if nums[i]==1:
                s+=1
                if maxi<s:
                    maxi=s
            else:
                s=0
        return maxi