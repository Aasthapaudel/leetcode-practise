# Assuming ListNode class definition is as follows:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to start the merged list
        tail = dummy  # Tail pointer for the merged list
        
        # Merge the two lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1  # Attach l1 node to the merged list
                l1 = l1.next  # Move l1 pointer forward
            else:
                tail.next = l2  # Attach l2 node to the merged list
                l2 = l2.next  # Move l2 pointer forward
            
            tail = tail.next  # Move tail pointer forward
        
        # If one of the lists is not empty, attach the remainder
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next  # Return the head of the merged list
