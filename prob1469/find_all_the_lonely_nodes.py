# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.final_list = []

    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        elif root.left and not root.right:
            self.final_list.append(root.left.val)
        elif root.right and not root.left:
            self.final_list.append(root.right.val)

        self.getLonelyNodes(root.left)
        self.getLonelyNodes(root.right)
        return self.final_list
