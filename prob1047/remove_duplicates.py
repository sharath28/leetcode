from string import ascii_lowercase
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # output = []
        # for ch in S:
        #     if output and ch == output[-1]:
        #         output.pop()
        #     else:
        #         output.append(ch)
        # return ''.join(output)
        duplicates = {2*ch for ch in ascii_lowercase}
        prev_len = -1

        while prev_len != len(S):
            prev_len = len(S)
            for d in duplicates:
                for d in duplicates:
                    S = S.replace(d,'')
        return S
