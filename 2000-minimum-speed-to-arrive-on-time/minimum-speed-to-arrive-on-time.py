class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        i = 1
        j = 10**7

        while i<j:
            mid = (i+j)//2
            a = 0
            for idx in range(len(dist)):
                if idx == len(dist) - 1:
                    a += dist[idx] / mid
                else:
                    a += (dist[idx] + mid - 1) // mid           
            
            if a>hour:
                i = mid+1
            else:
                j = mid

        if hour <= len(dist) - 1:
            return -1

        return i

