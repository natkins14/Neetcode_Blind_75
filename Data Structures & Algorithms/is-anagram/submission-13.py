class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        t_sorted = sorted(t)
        s_sorted = sorted(s)

        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False
        
        return True