class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # rev = s[::-1]
        i = 0
        for j in range(n-1,-1,-1):
            if s[i] == s[j]:
                i += 1
        if i == n:
            return s

        remain_rev = s[i:n]
        remain_rev = remain_rev[::-1]
        return remain_rev+self.shortestPalindrome(s[0:i])+s[i:]

#         rev = s
#         rev = rev[::-1]
#         j = 0
#         for i in range(n):
#             if s[:n-i]==rev[i:]:
#                 return rev[0:i]+s
#         return ""

        
