class Solution(object):
    def numBits(self,n):
        count = 0
        while n>0:
            if n%2!=0:
                count += 1
            n //= 2
        return count

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        final_list = []
        for i in range(num+1):
            final_list.append(self.numBits(i))
        return final_list
