class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        temp = self.x 
        
        if(self.x < 0):
            return False
        
        ans = 0
        
        while(True): 
            if(self.x <= 0):
                break;
        
            last_digit = self.x % 10
            ans = last_digit + ans * 10 
            self.x = self.x // 10
            
            if(self.x == 0):
                break;

        if (ans == temp):
            return True
        else:
            return False

