class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        s = sum(nums)
        for i in range(len(nums)):
            s-=nums[i]
            if l==s:
                return i
            else:
                if i == len(nums)-1:
                    return -1
                l+=nums[i]

                