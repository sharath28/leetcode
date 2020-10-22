class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        cycle_len = 2*numRows - 2
        i = 0
        final_string = ""
        while i< numRows:
            j = 0
            while j +i < len(s):
                final_string += s[j+i]
                if (i != 0 and i != numRows - 1 and j + cycle_len - i < len(s)):
                    final_string += s[j + cycle_len - i]
                j += cycle_len
            i += 1
        return final_string
