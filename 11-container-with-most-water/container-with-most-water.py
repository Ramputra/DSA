class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        j = len(height)-1
        i = 0
        maxi = 0
        while (i!=j):
            if height[i]<=height[j]:
                s = height[i]*(j-i)
            else:
                s = height[j]*(j-i)
            if maxi<s:
                maxi = s
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        
        return maxi
        