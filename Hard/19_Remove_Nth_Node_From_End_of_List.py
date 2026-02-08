"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        solution = head
        s_tail = ListNode(0, head)
        s_head = head

        while n:
            s_head = s_head.next
            n -= 1

        while s_head:
            s_tail = s_tail.next
            s_head = s_head.next

        if s_tail.next == head:
            solution = head.next
            return solution

        if s_tail.next:
            s_tail.next = s_tail.next.next
        else:
            s_tail.next = None

        return solution


s = Solution()
assert not s.removeNthFromEnd(ListNode(1), 1)
