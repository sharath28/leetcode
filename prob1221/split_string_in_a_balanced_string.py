class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        result = 0

        for char in s:
            if char == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                result += 1

        return result
