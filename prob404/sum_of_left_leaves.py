# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#         if root is None:
#             return 0

#         def is_leaf(node):
#             return node is not None and node.left is None and node.right is None

#         stack = [root]
#         total = 0
#         while stack:
#             sub_root = stack.pop()
#             if is_leaf(sub_root.left):
#                 total += sub_root.left.val

#             if sub_root.right is not None:
#                 stack.append(sub_root.right)

#             if sub_root.left is not None:
#                 stack.append(sub_root.left)
#         return total
        def process_subtree(subtree, is_left):
            if subtree is None:
                return 0

            if subtree.left is None and subtree.right is None:
                return subtree.val if is_left else 0

            return process_subtree(subtree.left,True) + process_subtree(subtree.right, False)

        return process_subtree(root,False)
