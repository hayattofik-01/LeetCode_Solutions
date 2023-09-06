class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevRef = {}
        
        headptr = head
        prev1 = head
        
        while headptr:
            prevRef[headptr] = prev1
            
            prev1 = headptr
            headptr = headptr.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head:
            if head.next and head.next.val < head.val:
                while prev.next and prev.next.val < head.next.val:
                    prev = prev.next

                temp = prev.next
                prev.next = head.next
                head.next = head.next.next
                prev.next.next = temp
                prev = dummy
            else:
                head = head.next

        return dummy.next