import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s)==0:
        #     return -1
        # if len(s)<2:
        #     return 0
        # s_dict = {}
        # for ch in s:
        #     if ch in s_dict:
        #         s_dict[ch] += 1
        #     else:
        #         s_dict[ch] = 1
        # index_list = []
        # for ch in s_dict:
        #     if s_dict[ch] == 1:
        #         index_list.append(s.index(ch))
        # if len(index_list)>=1:
        #     return min(index_list)
        # else:
        #     return -1
        count = collections.Counter(s)
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1
