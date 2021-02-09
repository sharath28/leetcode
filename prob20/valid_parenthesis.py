class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening_list = {'(':1,'{':2,'[':3}
        closing_list = {')':1,'}':2,']':3}
        for i in s:
            if i in opening_list:
                stack.append(i)
            if i in closing_list:
                if len(stack)==0:
                    return False
                temp = stack[len(stack)-1]
                stack.pop(len(stack)-1)
                if opening_list[temp]!=closing_list[i]:
                    return False
                else:
                    continue
        if len(stack)==0:
            return True
        else:
            return False
