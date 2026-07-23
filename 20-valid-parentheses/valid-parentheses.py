class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        l = {'[':']', '(':')', '{':'}'}
        for i in s:
            if i in l:
                a.append(i)
            elif i==')' or i=='}' or i==']':
                if len(a)>0:
                    if l[a[-1]] == i:
                        a.pop()
                    else:
                        return False
                else:
                    return False

        if len(a)==0:
            return True
        return False