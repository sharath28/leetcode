# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.return_list = []

    def inorder(self,root,level):
        if root == None:
            return
        if len(self.return_list)<level:
            self.return_list.append([root.val])
        else:
            self.return_list[level-1].append(root.val)
        self.inorder(root.left,level+1)
        self.inorder(root.right,level+1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.inorder(root,1)
        final_list = []
        i = 1
        for level in self.return_list:
            if i%2 == 1:
                final_list.append(level)
                i += 1
            else:
                final_list.append(level[::-1])
                i += 1
        return final_list
