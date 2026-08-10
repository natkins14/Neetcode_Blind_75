class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Initialize pointers for start and end of the string 
        start = 0
        end = len(s) - 1

        # While start is less than end 
        while start < end: 
            
            # while start is less than end and is not alphanumeric
            while start < end and not s[start].isalnum():
                # otherwise increment start
                start += 1
            # while end is greater than start and is not alphanumeric
            while end > start and not s[end].isalnum():
                # otherwise decrement end 
                end -=1
            # evaluate if the characters at start and end are not equal to one other
            if s[start].lower() != s[end].lower():
                return False
            # increment start and decrement end 
            start +=1
            end -=1
        # return true if all characters are equal 
        return True