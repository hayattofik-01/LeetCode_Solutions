# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        toList =[]

        while head:
            toList.append(head.val)
            head = head.next
        ans = [0 for i  in range(len(toList))]
        stack = []
        for n in range(len(toList)):

            while stack and toList[stack[-1]] < toList[n]:
                ans[stack.pop()] = toList[n]
            stack.append(n)
        return ans 




        