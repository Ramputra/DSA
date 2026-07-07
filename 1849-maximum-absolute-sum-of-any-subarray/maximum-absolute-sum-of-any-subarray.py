class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi = 0
        mini = min(nums)
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            maxi = max(maxi, s)
            s = max(0, s)
        
        for i in range(len(nums)):
            s+=nums[i]
            mini = min(mini, s)
            s = min(s, nums[i])


        return max(maxi, abs(mini))
            