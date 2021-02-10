class Solution(object):
    def isValid(self, s):
        
        self.s = s
        
        stack = []
         
        for k in range(0, len(self.s)):
            if(s[k] == "(" or s[k] == "{" or s[k] == "["):
                stack.append(s[k])
            
            else:
                if(len(stack) == 0):
                    return False
                
                if(s[k] == ")"):
                    if(stack[-1]) == "(":
                        stack.pop()
                    else:
                        return False
                
                if(s[k] == "}"):
                    if(stack[-1]) == "{":
                        stack.pop()
                    else:
                        return False
                
                if(s[k] == "]"):
                    if(stack[-1]) == "[":
                        stack.pop()
                    else:
                        return False
                
        return len(stack) == 0
                    
                    
                
