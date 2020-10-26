# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #############
        #Iteration
        # if not root:
        #     return True
        # stack = [(root, float('-inf'), float('inf')), ]
        # while stack:
        #     root,lower,upper = stack.pop()
        #     if not root:
        #         continue
        #     val = root.val
        #     if val<=lower or val>=upper:
        #         return False
        #     stack.append((root.right,val,upper))
        #     stack.append((root.left,lower,val))
        # return True
        #############
        #Recursion

        # def helper(root, lower = float('-inf'),upper = float('inf')):
        #     if not root:
        #         return True
        #     val = root.val
        #     if val<=lower or val>=upper:
        #         return False
        #     if not helper(root.right,val,upper):
        #         return False
        #     if not helper(root.left,lower,val):
        #         return False
        #     return True
        # return helper(root)

        ##############
        #Inorder Traversal
        stack,inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <=inorder:
                return False
            inorder = root.val
            root = root.right
        return True
