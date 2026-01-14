class Solution:
    def reverse(self, x: int) -> int:
        result = 0 
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if x < 0 :
            x = -(x)
            while x > 0 :
                ld = x % 10
                result = result *10 +ld
                x = x//10
            if result < INT_MIN or result > INT_MAX:
                return 0
            else:
                return -(result)


        while x > 0 :
            ld = x % 10
            result = result *10 +ld
            x = x//10
        if result < INT_MIN or result > INT_MAX:
            return 0

        return result
        
        

            
        