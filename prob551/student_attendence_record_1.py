class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_dict = {}
        count = 0
        flag = 0
        for ch in s:
            if ch == 'A':
                count = 0
                flag = 0
                if ch in a_dict:
                    return False
                else:
                    a_dict[ch] = 1
            elif ch == 'L':
                if flag == 1:
                    count += 1
                    if count == 3:
                        return False
                else:
                    flag = 1
                    count += 1
            else:
                flag = 0
                count = 0
        return True
