class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Initialize a hash map 
        m = {}

        # Loop through the array 
        for i, num in enumerate(nums): 
            
            # Determine complement
            complement = target - num

            # Determine if num is in hashmap 
            if complement in m:

                # Return indices of complement and num
                return [m[complement], i]
            
            # Initialize index of num to be i
            m[num] = i

