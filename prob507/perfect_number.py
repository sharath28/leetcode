import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        end_range = int(math.floor(math.sqrt(num))+1)
        temp_sum = 0
        for i in range(1,end_range):
            if num % i == 0:
                if num // i == i:
                    temp_sum += i
                else:
                    temp_sum += i +(num//i)
        if temp_sum-num == num:
            return True
        else:
            return False
        # return num in (6, 28, 496, 8128, 33550336)
            
