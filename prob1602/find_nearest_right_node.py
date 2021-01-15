# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        queue = [root,None]
        while queue:
            node = queue.pop(0)
            # print(node.val)
            if node == u:
                # print(queue)
                if len(queue) == 0:
                    return None
                else:
                    return queue[0]
            if node:
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            else:
                if queue:
                    queue.append(None)
        return None
