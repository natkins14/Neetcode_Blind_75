class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initialize hash map
        my_map = {}

        # Iterate through the array
        for i, num in enumerate(nums):

            # Compute element of complement 
            complement = target - num
            # Check if complement is in hash map 
            if complement in my_map:
                # If it is, return indices of current element and complement 
                return [my_map[complement], i]
            # Add num, indice to hash map 
            my_map[num] = i


