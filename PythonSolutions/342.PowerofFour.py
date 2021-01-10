import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
                                        
        if(math.log(num,4) != int(math.log(num,4))):
            return False              
        else:
            return True
