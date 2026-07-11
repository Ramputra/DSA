class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        i = 1
        j = max(p)

        while i<j:
            mid = (i+j)//2
            ho = 0
            for pu in p:
                ho+=(pu+mid-1)//mid

            if ho<=h:
                j = mid
            else:
                i = mid+1

        return i