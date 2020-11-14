class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return_list = []
        for i in range(0,len(s)-1):
            if s[i]=='+' and s[i+1]=='+':
                temp = s[:i]+'--'+s[i+2:]
                return_list.append(temp)
        return return_list
