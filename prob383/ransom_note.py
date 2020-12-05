class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_dict = {}
        m_dict = {}
        for ch in ransomNote:
            if ch in r_dict:
                r_dict[ch] += 1
            else:
                r_dict[ch] = 1
        for ch in magazine:
            if ch in m_dict:
                m_dict[ch] += 1
            else:
                m_dict[ch] = 1

        for ch in r_dict:
            if ch not in m_dict:
                return False
            else:
                if r_dict[ch]>m_dict[ch]:
                    return False
                else:
                    continue
        return True
            
