# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        ptr = head
        counter = defaultdict(int)

        while ptr:
            counter[ptr.val] +=1
            ptr = ptr.next
        while head :
            if counter[head.val] == 1:
                ans.append(head.val)
            head = head.next
               
        res = ListNode()
        resptr = res
        for num in ans:
            resptr.next = ListNode(num,None)
            resptr = resptr.next
        return res.next


        