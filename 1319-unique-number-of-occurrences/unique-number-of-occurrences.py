from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        l = set()
        for k, v in d.items():
            l.add(v)

        if len(l)<len(d):
            return False

        return True