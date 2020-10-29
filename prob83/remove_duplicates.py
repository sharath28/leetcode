# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = head
        while head!=None:
            next_node = head.next
            if next_node !=None:
                if next_node.val == head.val:
                    temp = next_node.next
                    head.next = temp
                else:
                    head = head.next
            else:
                head=head.next
        return dummy_head
