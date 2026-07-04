class Solution:
    def totalFruit(self, f: List[int]) -> int:
        j = 0
        maxi = 0
        d = {}

        for i in range(len(f)):
            d[f[i]] = d.get(f[i], 0) + 1

            while len(d) > 2:
                d[f[j]] -= 1
                if d[f[j]] == 0:
                    del d[f[j]]
                j += 1

            maxi = max(maxi, i - j + 1)

        return maxi