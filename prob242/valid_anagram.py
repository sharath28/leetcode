class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1
        for ch in t:
            if ch in t_dict:
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1
        for ch in s_dict:
            if ch not in t_dict:
                return False
            elif s_dict[ch]!=t_dict[ch]:
                return False
        return True
