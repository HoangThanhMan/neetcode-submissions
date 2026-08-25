# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        markNode = {}

        while head:
            if markNode.get(head, False) == False:
                markNode[head] = True
            else:
                return True
            
            head = head.next

        return False