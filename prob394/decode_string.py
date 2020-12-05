class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''

        stack = []
        counter = 0

        for i in range(len(s)):

            if s[i] != ']':
                stack.append(s[i])
                if s[i] == '[':
                    counter += 1

            else:

                str1 = ''
                num1 = ''

                while stack[len(stack)-1] != '[':

                    str1 = stack.pop() + str1

                stack.pop()

                while stack[len(stack)-1].isnumeric():

                    s1 = stack.pop()
                    if s1 == ']':
                        counter -= 1

                    num1 = s1 + num1

                    if len(stack) == 0:
                        break



                result += str1 * int(num1)

                if counter != 0:
                    stack.append(result)
                    result = ''

        remaining = ''

        while len(stack) != 0:
            remaining = stack.pop() + remaining
        result += remaining

        return result
