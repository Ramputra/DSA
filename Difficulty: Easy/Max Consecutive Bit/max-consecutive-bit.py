class Solution:
    def maxConsecBits(self, arr):
        j = 0
        maxi1 = 0
        maxi0 = 0
        count = 0
        for i in range(len(arr)):
            if arr[i]==1:
                count+=1
                maxi1 = max(maxi1, count)
            else:
                j = i
                count = 0
                
        count = 0
        for i in range(len(arr)):
            if arr[i]==0:
                count+=1
                maxi0 = max(maxi0, count)
            else:
                j = i
                count = 0
        
        return max(maxi1, maxi0)