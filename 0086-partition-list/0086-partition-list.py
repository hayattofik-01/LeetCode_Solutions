# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        lptr, rptr = left,right
        while head:
            if head.val < x:
                lptr.next = head
                lptr = lptr.next
            else:
                rptr.next = head
                rptr = rptr.next
            head = head.next
        lptr.next = right.next
        rptr.next = None
        return left.next
                
        