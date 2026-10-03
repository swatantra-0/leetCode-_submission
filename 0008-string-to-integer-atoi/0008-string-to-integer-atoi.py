class Solution:
    def myAtoi(self, s: str) -> int:
       s = s.strip()
       if not s :
          return 0
       sing, i, res =1,0,0
       if s[0] == '-':
         sing = -1 
         i +=1
       elif s[0] =='+':
          i +=1
       while i < len(s) and s[i].isdigit():
            res = res * 10 + int (s[i])
            if sing * res > 2**31- 1:
                return 2**31-1
            if sing * res < - 2**31:
                return -2**31
            i +=1
       return sing * res
            
        
 
    
    
    

        