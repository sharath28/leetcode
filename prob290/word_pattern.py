class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p_list = list(pattern)
        s_list = s.split(' ')
        temp = {}
        if len(s_list) != len(p_list):
            return False
        seen = set()
        for i in range(len(s_list)):
            # print(temp)
            if p_list[i] not in temp:
                if s_list[i] in seen:
                    return False
                temp[p_list[i]] = s_list[i]
                seen.add(s_list[i])
            else:
                if temp[p_list[i]] != s_list[i]:
                    return False
        return True
            
