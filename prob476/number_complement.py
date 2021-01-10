class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        todo, bit = num, 1
        while todo:
            num = num^bit
            bit = bit << 1
            todo = todo >> 1
        return num
