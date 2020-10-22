# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ###############
        #Recursion
        # if root == None:
        #     return None
        # right = self.invertTree(root.right)
        # left = self.invertTree(root.left)
        # root.left = right
        # root.right = left
        # return root
        ###############
        #Iteration
        if root == None:
            return None
        queue = []
        queue.append(root)
        while len(queue)>0:
            curr = queue.pop(0)
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left!=None:
                queue.append(curr.left)
            if curr.right!=None:
                queue.append(curr.right)
        return root
