class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        for x in range(len(s)):
            if s_sorted[x] != t_sorted[x]:
                return False
        
        return True