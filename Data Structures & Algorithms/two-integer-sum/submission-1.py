class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Outer loop to initialize iteration 
        for i in range(len(nums)):

            # Finds the difference between the target and the first number in the array 
            diff = target - nums[i]

            # Inner for loop
            for x in range(i + 1, len(nums)):
                # Checks if the difference is equal to the value at indice 'x'
                if nums[x] == diff:
                    # If so, returns the indices i, x as an array with the smaller index first
                    return [i, x]