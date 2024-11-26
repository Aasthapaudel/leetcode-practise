from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join([str(i) for i in digits]))  # Convert list to number
        s += 1  # Increment the number by 1
        result = list(str(s))  # Convert the number back to a string and then to a list of characters
        return [int(i) for i in result]  # Convert each character back to an integer
