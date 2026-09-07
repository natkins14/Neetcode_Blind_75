class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_map = {}

        for i in strs:

            m = ''.join(sorted(i))

            if m in my_map: 

                my_map[m].append(i)
            
            else: 
                my_map[m] = [i]
        
        return_values = list(my_map.values())

        return return_values
 
