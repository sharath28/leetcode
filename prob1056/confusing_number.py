class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        temp_dict = {'0':'0','6':'9','9':'6','8':'8','1':'1'}
        str_num = str(N)
        str_num1 = str_num[::-1]
        temp = ''
        for ch in str_num1:
            if ch not in temp_dict:
                return False
            else:
                temp += temp_dict[ch]
        if temp == str_num:
            return False
        else:
            return True
