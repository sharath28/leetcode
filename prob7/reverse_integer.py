class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x = x*(-1)
            rev_num = 0
            while x>0:
                rev_num = rev_num*10+x%10
                x=x/10
            rev_num = rev_num*(-1)
            if rev_num>-(2**31):
                return rev_num
            else:
                return 0
        else:
            rev_num = 0
            while x>0:
                rev_num = rev_num*10+x%10
                x=x/10
            if rev_num<(2**31-1):
                return rev_num
            else:
                return 0
