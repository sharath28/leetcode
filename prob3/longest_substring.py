class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ans= 0
        if len(s) == 1:
            return 1
        n = len(s)
        ans = i = j = 0
        temp_dict = {}
        while i<n and j<n:
            ch =  s[j]
            if ch not in temp_dict:
                temp_dict[ch] = 1
                j += 1
                if j-i > ans:
                    ans = j-i
            else:
                ch1 = s[i]
                del temp_dict[ch1]
                i += 1
        return ans

#######################
# Brute Force
#         for i in range(len(s)):
#             for j in range(i+1,len(s)+1):
#                 if self.allUnique(s,i,j):
#                     if (j-i) > ans:
#                         ans = j-i
#         return ans

#     def allUnique(self, s, start, end):
#         temp_dict = {}
#         for i in range(start,end):
#             ch = s[i]
#             if ch in temp_dict:
#                 return False
#             temp_dict[ch]=1
#         return True
