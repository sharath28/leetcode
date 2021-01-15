class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        # return len(s.split())
        for i in range(len(s)):
            if (i==0 or s[i-1]==' ') and s[i] != ' ':
                count += 1
        return count
