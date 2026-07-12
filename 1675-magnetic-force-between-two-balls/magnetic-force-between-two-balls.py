class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        p.sort()
        left = 1
        right = p[len(p)-1]-p[0]
        while left<right:
            mid = (left+right+1)//2
            b = 1
            last = p[0]

            for i in range(1, len(p)):
                if p[i]-last>=mid:
                    b+=1
                    last = p[i]

            if b >= m:
                left = mid
            else:
                right = mid - 1

        return left