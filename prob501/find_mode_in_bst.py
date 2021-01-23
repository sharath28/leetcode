# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp_list = []
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            temp_list.append(root.val)
            inorder(root.right)

        inorder(root)
        temp_dict = {}
        for num in temp_list:
            if num in temp_dict:
                temp_dict[num] += 1
            else:
                temp_dict[num] = 1
        maxi = -9999
        return_list = []
        for num in temp_dict:
            if temp_dict[num] > maxi:
                maxi = temp_dict[num]
                return_list = [num]
            elif temp_dict[num] == maxi:
                return_list.append(num)
            else:
                continue
        return return_list
            
