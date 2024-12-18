from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Check for an empty list
            return 0
        
        i = 0  # Pointer for the last unique element
        for j in range(1, len(nums)):  # Start from the second element
            if nums[j] != nums[i]:  # If a new unique element is found
                i += 1  # Move to the next position for unique elements
                nums[i] = nums[j]  # Update the list in-place with the new unique element
        
        # Return the number of unique elements
        return i + 1  # Return the count of unique elements

