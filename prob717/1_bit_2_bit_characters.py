class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if i == len(bits)-1:
                if bits[len(bits)-1] == 0:
                    return True
                else:
                    return False
            if bits[i] == 1:
                i = i + 2
            else:
                i = i + 1
        return False
