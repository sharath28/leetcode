class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        temp_dict = {'9':'6','1':'1','8':'8','6':'9','0':'0'}
        temp_str = ''
        for ch in num:
            if ch not in temp_dict:
                return False
            else:
                temp_str += temp_dict[ch]
        return temp_str == num[::-1]
