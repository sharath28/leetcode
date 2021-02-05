class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        # while x>0 or y>0:
        #     if x == 0:
        #         while y > 0:
        #             if y%2!=0:
        #                 count += 1
        #             y /= 2
        #         break
        #     elif y == 0:
        #         while x > 0:
        #             if x%2!=0:
        #                 count += 1
        #             x /= 2
        #         break
        #     if x%2!=y%2:
        #         count += 1
        #     x /= 2
        #     y /= 2
        # return count
        temp = x^y
        while temp>0:
            if temp%2!=0:
                count += 1
            temp //= 2
        return count

            
