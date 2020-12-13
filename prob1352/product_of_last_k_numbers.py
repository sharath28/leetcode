class ProductOfNumbers(object):

    def __init__(self):
        self.arr = [1]


    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        # self.list.append(num)
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(self.arr[-1]*num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        # prod = 1
        # for i in range(len(self.list)-1,len(self.list)-k-1,-1):
        #     prod *= self.list[i]
        # return prod
        if k >= len(self.arr):
            return 0

        return (self.arr[-1]//self.arr[-k-1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
