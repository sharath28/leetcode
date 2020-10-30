class Solution(object):
    def find_sum(self,n):
        num_list = list(str(n))
        num_list = map(int,num_list)
        num_square_list = [i*i for i in num_list]
        return sum(num_square_list)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = {}
        while True:
            n = self.find_sum(n)
            if n == 1:
                return True
            if n in temp:
                return False
            else:
                temp[n]=1
        
