class Solution:
    def shipWithinDays(self, w: List[int], d: int) -> int:
        i = max(w)
        j = sum(w)

        while i<j:
            mid = (i+j)//2
            t = 0
            n = 1
            for wo in w:
                if t+wo<=mid:
                    t+=wo
                else:
                    n+=1
                    t = wo

            if n<=d:
                j = mid
            else:
                i = mid+1

        return i