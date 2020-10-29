# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #################
        #Iterative Approach
        # if head ==None:
        #     return None
        # if head.next == None:
        #     return head
        # first = head
        # second = head.next
        # while second !=None:
        #     temp = first.val
        #     first.val = second.val
        #     second.val = temp
        #     first = second.next
        #     if first == None:
        #         break
        #     second = second.next.next
        # return head
        #################
        #Recursion
        if head == None or head.next == None:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
