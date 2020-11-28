# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.inorder_list = []

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        self.inorder_list.append(root)
        self.inorder(root.right)

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.inorder(root)
        for i in range(len(self.inorder_list)):
            if p == self.inorder_list[i]:
                if i != len(self.inorder_list)-1:
                    return self.inorder_list[i+1]
        return None
