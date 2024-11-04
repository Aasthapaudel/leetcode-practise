from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Initialize a pointer for traversing the list
        while i < len(nums):
            if nums[i] == val:  # If the current element is equal to val
                nums.pop(i)  # Remove the element
                # Do not increment i, as we need to check the next element in the same index
            else:
                i += 1  # Only increment i if we did not remove an element
        
        return len(nums)  # Return the new length of the modified list
