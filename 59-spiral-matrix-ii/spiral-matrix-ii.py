class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = n+1
        lis = [[0]*n for _ in range(n)]
        l = 0
        r = n-1
        t = 0
        b = n-1
        c = 1
        while t<=b and l<= r:

            for i in range(l, r+1):
                lis[t][i] = c   
                c+=1
            t+=1

            for i in range(t, b+1):
                lis[i][r] = c
                c+=1
            r-=1

            if t<=b:
                for i in range(r, l-1, -1):
                    lis[b][i] = c
                    c+=1
                b-=1

            if l<=r:
                for i in range(b, t-1, -1):
                    lis[i][l] = c
                    c+=1
                l+=1

        return lis

