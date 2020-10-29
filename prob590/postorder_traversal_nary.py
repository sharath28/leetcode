"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def __init__(self):
        self.return_list = []

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        for child in root.children:
            self.postorder(child)
        self.return_list.append(root.val)
        return self.return_list
