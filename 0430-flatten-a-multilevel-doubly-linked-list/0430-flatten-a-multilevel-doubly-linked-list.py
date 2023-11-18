"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : return head
        dummy = Node(0)
        pointer , stack = dummy,[head]

        while stack:
            temp = stack.pop()
            if temp.next : stack.append(temp.next)
            if temp.child : stack.append(temp.child)
            pointer.next = temp
            temp.prev = pointer
            temp.child = None
            pointer = temp
        dummy.next.prev = None
        return dummy.next 


