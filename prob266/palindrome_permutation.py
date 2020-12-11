class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_dict = {}
        for ch in s:
            if ch not in temp_dict:
                temp_dict[ch] = 1
            else:
                temp_dict[ch] += 1

        count = 0
        for ch in temp_dict:
            count += (temp_dict[ch]%2)

        if count <=1:
            return True
        else:
            return False
