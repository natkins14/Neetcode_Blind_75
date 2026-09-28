class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Initialize a Hash Table 

        my_map = {}

        # Iterate through strings in strs

        for x in strs: 

            # Need to sort the str 

            m = ''.join(sorted(x))

            # Check if the string is in the hashmap 

            if m in my_map:

                # if so, append it to the list 

                my_map[m].append(x)

            # if not, create a new list with x 
            
            else:
                my_map[m] = [x] 
            
        # return the hash table entries as a list of lists 

        return_values = list(my_map.values())

        return return_values

        