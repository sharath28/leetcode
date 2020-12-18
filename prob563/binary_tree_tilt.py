# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.total_sum = 0

    def inorder(self,root):
        if root == None:
            return 0
        left_sum = self.inorder(root.left)
        right_sum = self.inorder(root.right)
        # temp_val = root.val
        temp_val = abs(left_sum-right_sum)
        self.total_sum += temp_val
        return left_sum + right_sum + root.val

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        return self.total_sum
        
