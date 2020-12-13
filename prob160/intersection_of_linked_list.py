# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headA_dict = {}
        temp = headA
        while temp!=None:
            headA_dict[temp] = temp.val
            temp = temp.next

        while headB!=None:
            if headB in headA_dict:
                return headB
            else:
                headB = headB.next
        return headB
