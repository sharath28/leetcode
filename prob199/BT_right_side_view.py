# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
##############
#BFS with two queue
#         if root is None:
#             return []

#         next_level = deque([root,])
#         rightside = []
#         while next_level:
#             curr_level = next_level
#             next_level = deque()

#             while curr_level:
#                 node = curr_level.popleft()
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
#             rightside.append(node.val)
#         return rightside
################
#DFS
        if root is None:
            return []

        rightside = []
        def helper(node,level):
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right,node.left]:
                if child:
                    helper(child,level+1)

        helper(root, 0)
        return rightside
