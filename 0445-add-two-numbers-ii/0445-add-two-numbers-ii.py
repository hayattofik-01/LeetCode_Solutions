# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        nums2 = []
        def add(l1,l2):
            l = len(l1) - 1
            r = len(l2) - 1
            while l >= 0 and r>=0 :
                val = l1[l] + l2[r]
                print(val)
                if val >= 10 and l >= 1 :
                    l1[l] = (val % 10)
                    l1[l - 1] += val//10

                else:
                    l1[l] =val
                l-=1
                r-=1
            n = ListNode()
    
            
            while l >= 1:
                if l1[l] >= 10:
                    l1[l] = (l1[l] % 10)
                    l1[l - 1] += val//10
                l-=1
    
            if l1[0] >=10:
                l1 = [l1[0]//10,l1[0] % 10] + l1[1:]
            ptr = n
            for val in l1:
                ptr.next = ListNode(val = val)
                ptr = ptr.next
            
            return n.next
                
            
            
            
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
            
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        if len(nums1) > len(nums2):
            return add(nums1,nums2)
        return add(nums2,nums1)