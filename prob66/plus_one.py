class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        while True:
            if digits[i]==9:
                if i-1==-1:
                    digits[i]=0
                    digits.insert(0,1)
                    break
                else:
                    digits[i]=0
                    i=i-1
            else:
                digits[i]=digits[i]+1
                break
        return digits
