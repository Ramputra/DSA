class Solution:
	def equilibrium(self,arr): 
    	a = sum(arr)-arr[0]
    	l = arr[0]
    	b = 'false'
    	for i in range(1, len(arr)):
    	    a-=arr[i]
    	    if a==l:
    	        b = 'true'
    	        return b
    	    else:
    	        l+=arr[i]
    	        
    	return b