class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        t_sorted = sorted(t)
        s_sorted = sorted(s)
        
        for x in range(len(s)):

            if t_sorted[x] != s_sorted[x]:
                return False
        
        return True