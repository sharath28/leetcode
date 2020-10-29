# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first!=None:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next
        return dummy.next

##################
#Two pointer Approach
#         dummy = ListNode(0)
#         dummy.next = head
#         first = dummy
#         second = dummy
#         for i in range(1,n+2):
#             first = first.next

#         while first != None:
#             first = first.next
#             second = second.next

#         second.next = second.next.next

#         return dummy.next
