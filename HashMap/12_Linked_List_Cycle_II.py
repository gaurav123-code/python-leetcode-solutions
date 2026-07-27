"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, 
return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Find starting node of cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2      

ans = Solution().detectCycle(node1)

if ans:
    print(ans.val)
else:
    print(None)