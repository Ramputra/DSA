class Solution:
	def removeVowels(self, s):
		l = 'aeiou'
		a = ''
		for i in s:
		    if i not in l:
		        a+=i
		        
		return a
		