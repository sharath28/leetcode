class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        temp_dict = {}
        for ch in jewels:
            temp_dict[ch] = 1

        count = 0
        for ch in stones:
            if ch in temp_dict:
                count += 1
        return count
