class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        s = 1
        p = 1
        for i in range(len(nums)):
            if i!=0:
                ans.append(p*nums[i-1])
                p*=nums[i-1]
            else:
                ans.append(p)
        
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= s
            s *= nums[i]
      
    
    

    
        return ans


        

