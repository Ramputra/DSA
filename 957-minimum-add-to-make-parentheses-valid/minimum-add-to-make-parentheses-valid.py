
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a = []

        for i in range(len(s)):
            if s[i]=='(':
                a.append(s[i])
            else:
                if len(a)>0:
                    if a[-1]=='(':
                        a.pop()
                    else:
                        a.append(s[i])
                else:
                    a.append(s[i])

        return len(a)