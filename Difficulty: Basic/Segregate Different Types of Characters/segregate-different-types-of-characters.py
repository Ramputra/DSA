class Solution:
    def splitString(self, s): 
        d = ""
        ch = ""
        p = ""
        l = []
        for i in s:
            if i.isalpha():
               ch+=i
            elif i.isdigit():
                d+=i
            else:
                p+=i
        
        if len(ch)==0:
            ch+='-1'
        if len(d)==0:
            d+='-1'
        if len(p)==0:
            p+='-1'
        
        l.append(ch)
        l.append(d)
        l.append(p)
        
        return l
        
       