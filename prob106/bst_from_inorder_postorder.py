# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.pre_idx = 0

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up pre_idx element as a root
            root_val = postorder[self.pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            self.pre_idx -= 1
            # build left subtree
            root.right = helper(index+1, in_right)
            root.left = helper(in_left, index-1)
            # build right subtree

            return root
        self.pre_idx = len(postorder)-1
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        # preorder = postorder[::-1]
        return helper(0,len(inorder)-1)
