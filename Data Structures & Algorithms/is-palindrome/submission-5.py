class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Initialize pointers pointing to the start and end of the string 

        start = 0
        end = len(s) - 1

        # Continue looping through while start pointer is less than end 
        while start < end:

            # Check if start is less than end and it is not a alphanumeric character
            while start < end and not s[start].isalnum():
                # Moves start forward if both conditions met
                start +=1
            # Check if end is greater than start and it is not a alphanumeric character
            while end > start and not s[end].isalnum():
                # Moves end backward if both conditions met
                end -=1 
            # Checks if both characters are not equal, returns false if so 
            if s[start].lower() != s[end].lower():
                return False
            # Increments start and decrements end pointer
            start +=1
            end -= 1
        # If all alphanumeric characters are equal for all pointer increments, return  true
        return True