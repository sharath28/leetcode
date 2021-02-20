"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def __init__(self):
        self.return_list = []
        self.value_list = []

    def inorder(self,root,level):
        if root == None:
            return
        if len(self.return_list)<level:
            self.return_list.append([root])
            self.value_list.append([root.val])
        else:
            self.return_list[level-1].append(root)
            self.value_list[level-1].append(root.val)

        self.inorder(root.left,level+1)
        self.inorder(root.right,level+1)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.inorder(root,1)
        print(self.value_list)
        for level in self.return_list:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root
