class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Initializes an empty HashMap
        my_map = {}

        # Loops through nums and extracts the index and value 
        for i, num in enumerate(nums):
            # Calculates the difference between the target and num 
            diff = target - num
            # Determines if that differences is in the HashMap
            if diff in my_map:
                # If so, returns the index of the difference and i
                return [my_map[diff], i]
            # Otherwise, sets the index of num to i
            my_map[num] = i