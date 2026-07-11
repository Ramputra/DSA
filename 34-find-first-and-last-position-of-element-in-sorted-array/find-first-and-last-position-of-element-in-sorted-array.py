class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        i = 0
        j = len(nums)-1
        a = []
        while i<j:
            mid = (i+j)//2
            if nums[mid]>=target:
                j = mid
            else:
                i = mid+1

        a.append(j)
        j = len(nums)-1
        i = 0
        while i<j:
            mid = (i+j+1)//2
            if nums[mid]<=target:
                i = mid
            else:
                j = mid-1
        a.append(i)

        return a
        