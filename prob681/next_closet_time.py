class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        curr = 60 * int(time[:2]) + int(time[3:])
        # print(curr)
        allowed = {int(x) for x in time if x!=':'}
        # print(allowed)
        while True:
            curr = (curr+1)%(24*60)
            if all(digit in allowed
                  for block in divmod(curr,60)
                  for digit in divmod(block,10)):
                return "{:02d}:{:02d}".format(*divmod(curr,60))
