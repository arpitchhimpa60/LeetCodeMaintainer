# Runtime: 14 ms
# Memory: 19.4 MB

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for i in s:
            if i in dic_s:
                dic_s[i] +=1
            else:
                dic_s[i]  = 1
        dic_t = {}
        for i in t:
            if i in dic_t:
                dic_t[i] +=1
            else:
                dic_t[i]  = 1
        if dic_s == dic_t:
            return True
        else:
            return False

        