# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ####Approach 1
        # if head==None:
        #     return None
        # if head.next == None:
        #     return head
        # new_node = ListNode(head.val)
        # temp = head.next
        # while temp!=None:
        #     next_node = temp.next
        #     temp.next = new_node
        #     new_node = temp
        #     if next_node==None:
        #         return temp
        #     temp = next_node
        prev = None
        curr = head
        while curr!=None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
