# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        node_list = []

        def bfs(root):
            queue = deque([(root,0,0)])
            while queue:
                node,row,column = queue.popleft()
                if node is not None:
                    node_list.append((column,row,node.val))
                    queue.append((node.left,row+1,column-1))
                    queue.append((node.right,row+1,column+1))

        bfs(root)

        node_list.sort()

        ret = OrderedDict()
        for col,row,val in node_list:
            if col in ret:
                ret[col].append(val)
            else:
                ret[col] = [val]

        return ret.values()
