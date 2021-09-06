class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=0
        while(x!=0):
            y=(y*10)+(x%10)
            x=x/10
        return y
            
        
