# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ele_list = []

    def inorder(self,root):
        if root == None:
            return
        self.ele_list.append(root.val)
        self.inorder(root.left)
        self.inorder(root.right)


    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.inorder(root1)
        self.inorder(root2)
        # print(self.ele_list)
        return_list = sorted(self.ele_list)
        return return_list
