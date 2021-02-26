# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node):
            if node.left is None and node.right is None:
                leaves.append(node.val)
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)

        if root == None:
            return []

        if root.left == None and root.right == None:
            return [root.val]

        left = [root.val]

        if root.left != None:
            curr = root.left
            while curr != None:
                left.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
            left.pop()

        right = []
        if root.right != None:
            curr = root.right
            while curr != None:
                right.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            right.pop()
        right.reverse()

        leaves = []
        dfs(root)
        return left+leaves+right
