class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        return_list = []
        flag = 0
        for ch in str(num):
            if ch == '6' and flag == 0:
                return_list.append('9')
                flag = 1
            else:
                return_list.append(ch)
        return int(''.join(return_list))
