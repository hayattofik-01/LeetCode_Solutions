# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stackl1 = []
        stackl2 = []
        
        while l1:
            stackl1.append(l1.val)
            l1 = l1.next
        while l2 : 
            stackl2.append(l2.val)
            l2 = l2.next
            
        # the number to be passed to the next sum
        carry = 0
        # the current sum
        cursum = 0
        #the output linked list
        res = None
        while stackl1 or stackl2 or carry:
            cursum = carry 
            
            if stackl1:
                cursum += stackl1.pop()
            if stackl2:
                cursum += stackl2.pop()
            
            node = ListNode(val = cursum % 10)
            carry = cursum // 10
            node.next = res
            res = node 

        return res