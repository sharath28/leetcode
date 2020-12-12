# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
#         def inorder(r):
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []

#         def find_two_swapped(nums):
#                 n = len(nums)
#                 x = y = -1
#                 for i in range(n - 1):
#                     if nums[i + 1] < nums[i]:
#                         y = nums[i + 1]
#                         # first swap occurence
#                         if x == -1:
#                             x = nums[i]
#                         # second swap occurence
#                         else:
#                             break
#                 return x, y

#         def recover(r, count):
#                 if r:
#                     if r.val == x or r.val == y:
#                         r.val = y if r.val == x else x
#                         count -= 1
#                         if count == 0:
#                             return
#                     recover(r.left, count)
#                     recover(r.right, count)

#         nums = inorder(root)
#         x, y = find_two_swapped(nums)
#         recover(root, 2)
        stack = []
        x = y = pred = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right

        x.val, y.val = y.val, x.val
