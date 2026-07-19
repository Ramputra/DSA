class Solution:
    def reverseWords(self, s):
        # 1. Split the string by dots.
        # We filter out empty strings to handle multiple/trailing/leading dots.
        words = [word for word in s.split('.') if word]
        
        # 2. Reverse the list of words.
        words.reverse()
        
        # 3. Join the words back together with a single dot.
        return ".".join(words)
        
