# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Slow is now the center of the list. Reverse second half of the list here
        curr = slow.next
        prev = slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev is now the start of the reversed list:
        # merge both lists

        list1 = head
        list2 = prev
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list1 = tmp1
            list2.next = tmp1
            list2 = tmp2
            