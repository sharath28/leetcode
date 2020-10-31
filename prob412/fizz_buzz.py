class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        final_list = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                final_list.append("FizzBuzz")
            elif i%3==0:
                final_list.append("Fizz")
            elif i%5==0:
                final_list.append("Buzz")
            else:
                final_list.append(str(i))
        return final_list
