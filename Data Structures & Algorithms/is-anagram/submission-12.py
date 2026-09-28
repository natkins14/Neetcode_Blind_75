class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for x in range(len(sorted_s)):

            if sorted_s[x] != sorted_t[x]:

                return False
        
        return True