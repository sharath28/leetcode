class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # return_list = []
        # for i in range(len(T)-1):
        #     flag = 0
        #     for j in range(i+1,len(T)):
        #         if T[i]<T[j]:
        #             flag = 1
        #             return_list.append(j-i)
        #             break
        #     if flag == 0:
        #         return_list.append(0)
        # return_list.append(0)
        # return return_list
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
