# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()

        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val

            curr.val = sum % 10 + carry
            if l1.next or l2.next:
                curr.next = ListNode()
                curr = curr.next

            if sum >= 10:
                carry = 1
            else:
                carry = 0

            l1 = l1.next
            l2 = l2.next


        rest = None
        if l1 or l2:
            rest = l1 or l2 

        while rest:
            sum = rest.val + carry
            curr.val = sum % 10
            if rest.next:
                curr.next = ListNode()
                curr = curr.next
            if sum >= 10:
                carry = 1
            else: 
                carry = 0
            rest = rest.next


        if carry:
            curr.next = ListNode()
            curr = curr.next
            curr.val = 1

        return dummy
            