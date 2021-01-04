class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k == 0:
            return [0]*len(code)
        elif k > 0:
            return_list = []
            for i in range(len(code)):
                if i + k >= len(code):
                    temp = sum(code[i+1:])+sum(code[:k-(len(code)-(i+1))])
                    return_list.append(temp)
                else:
                    return_list.append(sum(code[i+1:i+1+k]))
            return return_list
        else:
            # print("hi")
            return_list = []
            k = abs(k)
            for i in range(len(code)):
                if i - k < 0:
                    temp = sum(code[:i]) + sum(code[len(code)+i-k:])
                    return_list.append(temp)
                else:
                    return_list.append(sum(code[i-k:i]))
            return return_list
