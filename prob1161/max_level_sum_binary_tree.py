# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum = -sys.maxsize - 1
        next_queue = [(root,1)]
        curr = []
        max_level = 1
        while next_queue:
            curr = next_queue
            next_queue = []
            curr_sum = 0
            while curr:
                node_level = curr.pop(0)
                curr_sum += node_level[0].val
                if node_level[0].right:
                    next_queue.append((node_level[0].right,node_level[1]+1))
                if node_level[0].left:
                    next_queue.append((node_level[0].left,node_level[1]+1))
            if curr_sum>max_sum:
                max_sum = curr_sum
                max_level = node_level[1]
        return max_level
                
