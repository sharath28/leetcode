# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.temp_sum = 0

    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.right)
        self.temp_sum = self.temp_sum + root.val
        root.val = self.temp_sum
        self.postorder(root.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.postorder(root)
        return root
