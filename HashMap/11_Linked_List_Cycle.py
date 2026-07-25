"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the 
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
class Solution(object):
    def hasCycle(self, head):
        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False
    
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
    
print(Solution().hasCycle(n1))