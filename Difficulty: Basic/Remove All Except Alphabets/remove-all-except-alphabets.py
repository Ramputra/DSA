class Solution:
    def removeChars(self, s: str) -> str:
        return ''.join(ch for ch in s if ch.isalpha())
        