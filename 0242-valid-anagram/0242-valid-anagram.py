class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s={}
        count_t={}
        for ch in s:
            if ch in count_s:
                count_s[ch]+=1
            else:
                count_s[ch]=1
        for ch in t:
            if ch in count_t:
                count_t[ch]+=1
            else:
                count_t[ch]=1
        if count_s==count_t:
            return True
        else:
            return False