# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.pre_idx = 0

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left = 0, in_right = len(inorder)):
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            self.pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root
        self.pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper()

        # idx = {}
        # for i, val in enumerate(inorder):
        #     idx[val] = i
        # stack = []
        # head = None
        # for val in preorder:
        #     if not head:
        #         head = TreeNode(val)
        #         stack.append(head)
        #     else:
        #         node = TreeNode(val)
        #         if idx[val]<idx[stack[-1].val]:
        #             stack[-1].left= node
        #         else:
        #             while stack and idx[stack[-1].val] < idx[val]:
        #                 u = stack.pop()
        #             u.right = node
        #         stack.append(node)
        # return head
