class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_map = {}

        for x in strs:

            m = ''.join(sorted(x))

            if m in my_map:
                my_map[m].append(x)
            
            else:
                my_map[m] = [x]
        
        result = list(my_map.values())

        return result