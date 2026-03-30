# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Finding the middle. slow.next is always middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse 2nd half of list
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge both lists, second null 

        first, second = head, prev
        while second: # Second always equal to or shorter than first half
            tmp1, tmp2 = first.next, second.next
            first.next = second
            first = tmp1
            second.next = first
            second = tmp2


        