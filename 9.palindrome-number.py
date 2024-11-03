class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromic
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        while x > rev:
            last_digit = x % 10
            rev = rev * 10 + last_digit
            x = x // 10
        
        # Check if the number is palindromic
        return x == rev or x == rev // 10
