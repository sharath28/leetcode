class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (Y % 4 == 0 and Y%100 != 0) or Y%400==0:
            if M == 2:
                return 29
            else:
                return month_list[M-1]
        return month_list[M-1]
