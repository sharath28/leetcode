class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_list = list(t)
        s_list = list(s)
        for i in t_list:
            if i not in s_list:
                return i
            else:
                s_list.remove(i)
