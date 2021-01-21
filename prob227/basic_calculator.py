class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return eval(s.replace('/','//'))
        if s == None or len(s)==0:
            return 0
        s_len = len(s)
        stack = []
        curr_num = 0
        operation = '+'
        for i in range(s_len):
            curr_char = s[i]
            if curr_char.isdigit()==True:
                curr_num = (curr_num*10)+(ord(curr_char)-ord('0'))
            if (curr_char.isdigit()==False and curr_char.isspace()==False) or i == s_len -1:
                if operation == '-':
                    # print(curr_num)
                    stack.append(-curr_num)
                elif operation == '+':
                    stack.append(curr_num)
                elif operation == '*':
                    stack.append(stack.pop()*curr_num)
                elif operation == '/':
                    temp = stack.pop()
                    val = temp/float(curr_num)
                    stack.append(int(val))
                operation = curr_char
                curr_num = 0
        result = 0
        # print(stack)
        while stack:
            result += stack.pop()
        return result
