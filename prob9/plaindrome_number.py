class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0 or (x%10==0 and x!=0)):
            return False
        rev_num = 0
        while x>rev_num:
            rev_num = rev_num*10 + x%10
            print(rev_num)
            x=x/10
        return x == rev_num or x == rev_num/10
