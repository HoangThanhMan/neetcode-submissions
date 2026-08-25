# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        if length == n:
            return head.next

        prev = None
        cur = head
        i = 0
        
        while cur:
            if i == length - n:
                prev.next = cur.next
                break
            
            prev = cur
            cur = cur.next
            i += 1 
            
        return head    