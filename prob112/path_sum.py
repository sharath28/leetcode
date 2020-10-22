# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        else:
            ans = 0
            sub_sum = sum1 - root.val
            if sub_sum == 0 and root.left == None and root.right == None:
                return True
            if root.left is not None:
                ans = ans or self.hasPathSum(root.left,sub_sum)
            if root.right is not None:
                ans = ans or self.hasPathSum(root.right,sub_sum)
            return ans
