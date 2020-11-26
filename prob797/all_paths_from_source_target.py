class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph)-1
        results = []

        def backtrack(currnode,path):
            if currnode == target:
                results.append(list(path))
                return
            for nextnode in graph[currnode]:
                path.append(nextnode)
                backtrack(nextnode,path)
                path.pop()

        path = deque([0])
        backtrack(0,path)

        return results
