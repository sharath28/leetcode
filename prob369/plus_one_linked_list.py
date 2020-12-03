# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1
        not_nine = not_nine.next


        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next
        
