class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        if nums[i]==target:
            return i
        if nums[i]==target:
            return j
        while i<=j:
            mid = (j+i)//2
            if nums[mid]>target:
                j = mid-1
            elif nums[mid]<target:
                i=mid+1
            else:
                return mid
        
        return -1

