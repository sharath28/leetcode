class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        final_string = ''
        while i < len(s):
            if i+k>len(s):
                temp = s[i:]
                final_string += temp[::-1]
                i += k
            else:
                temp = s[i:i+k]
                final_string += temp[::-1]
                i += k
                final_string += s[i:i+k]
                i += k
        return final_string
