class Solution:
    def firstOccurence(self,txt,pat):
        
        for i in range(len(txt)-len(pat)+1):
            if txt[i:i+len(pat)]==pat:
                return i
        return -1