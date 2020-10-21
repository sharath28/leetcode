class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count = 0
        i=0
        n = len(s)
        while i<n:
            if s[i]=='I':
                if i == n-1:
                    count = count + 1
                    i += 1
                else:
                    if s[i+1]=='V':
                        count = count + 4
                        i += 2
                    elif s[i+1]=='X':
                        count = count + 9
                        i += 2
                    else:
                        count = count + 1
                        i += 1
            elif s[i]=='X':
                if i == n-1:
                    count = count + 10
                    i += 1
                else:
                    if s[i+1]=='L':
                        count = count + 40
                        i += 2
                    elif s[i+1]=='C':
                        count = count + 90
                        i += 2
                    else:
                        count = count + 10
                        i += 1
            elif s[i]=='C':
                if i == n-1:
                    count = count + 100
                    i += 1
                else:
                    if s[i+1]=='D':
                        count = count + 400
                        i += 2
                    elif s[i+1]=='M':
                        count = count + 900
                        i += 2
                    else:
                        count = count + 100
                        i += 1
            else:
                count = count + map_dict[s[i]]
                i += 1
        return count
