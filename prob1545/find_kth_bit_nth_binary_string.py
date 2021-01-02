class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def invert(s):
            temp_s = ""
            s = s[::-1]
            for ch in s:
                if ch == "0":
                    temp_s += '1'
                else:
                    temp_s += '0'
            return temp_s
        s1 = "0"
        i = 2
        while i <= n:
            temp_s = s1 + "1"+invert(s1)
            s1 = temp_s
            i += 1
        return s1[k-1]
