# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def util(self,root,p):
        if root == None:
            return p-1
        max_value = max(self.util(root.left,p+1),self.util(root.right,p+1))
        return max_value

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.util(root,1)
