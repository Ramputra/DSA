class Solution:
    def removeChars (ob, s, c):
        return ''.join(ch for ch in s if ch not in c)