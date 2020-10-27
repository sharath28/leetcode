"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.visit_dict = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None

        if head in self.visit_dict:
            return self.visit_dict[head]

        node = Node(head.val,None,None)
        self.visit_dict[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
