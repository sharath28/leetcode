# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #Recursion
        # if t1 == None:
        #     return t2
        # if t2 == None:
        #     return t1
        # t1.val += t2.val
        # t1.left = self.mergeTrees(t1.left,t2.left)
        # t1.right = self.mergeTrees(t1.right,t2.right)
        # return t1
        #Iteration
        if t1 == None:
            return t2
        stack = []
        stack.append((t1,t2))
        while len(stack) != 0:
            temp = stack.pop()
            if temp[0]==None or temp[1]==None:
                continue
            temp[0].val += temp[1].val
            if temp[0].left ==None:
                temp[0].left = temp[1].left
            else:
                stack.append((temp[0].left,temp[1].left))
            if temp[0].right ==None:
                temp[0].right = temp[1].right
            else:
                stack.append((temp[0].right,temp[1].right))
        return t1
