# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        self.bst_list.append(root.val)
        self.inorder(root.right)

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.bst_list = []
        self.inorder(root)
        self.index = 0


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.index < len(self.bst_list):
            temp = self.bst_list[self.index]
            self.index += 1
            return temp


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.index < len(self.bst_list):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
