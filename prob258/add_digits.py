class Solution(object):
    def findSum(self,num):
        num_list = list(str(num))
        num_list = map(int,num_list)
        return sum(num_list)

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num>9:
        #     num=self.findSum(num)
        # return num
        if num==0:
            return 0
        if num % 9 ==0:
            return 9
        return num%9
