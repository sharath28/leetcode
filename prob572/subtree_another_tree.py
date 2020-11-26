# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # tree1 = self.preorder(s,True)
        # tree2 = self.preorder(t,True)
        # if tree2 in tree1:
        #     return True
        # else:
        #     return False
        return self.traverse(s,t)

    def equals(self,x,y):
        if x == None and y == None:
            return True
        if x == None or y == None:
            return False
        return (x.val == y.val and self.equals(x.left,y.left) and self.equals(x.right,y.right))

    def traverse(self,s,t):
        return (s!=None and (self.equals(s,t) or self.traverse(s.left,t) or self.traverse(s.right,t)))

    def preorder(self,node,left):
        if node == None:
            if left:
                return "lnull"
            else:
                return "rnull"

        return "#"+str(node.val)+" "+self.preorder(node.left,True)+" "+self.preorder(node.right,False)
