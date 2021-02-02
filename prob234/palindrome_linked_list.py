# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head!=None:
            vals.append(head.val)
            head = head.next
        return vals==vals[::-1]
#         self.front_pointer = head

#         def recursively_check(current_node=head):
#             if current_node is not None:
#                 if not recursively_check(current_node.next):
#                     return False
#                 if self.front_pointer != current_node.val:
#                     return False
#                 self.front_pointer = self.front_pointer.next
#             return True

#         return recursively_check()
