class Solution(object):
    def dfs(self, s, i, graph, tmp, indexes, visited):
        visited[i] = 1
        tmp.append(s[i])
        indexes.append(i)
        for neigh in graph[i]:
            if visited[neigh] == 1:
                continue
            self.dfs(s, neigh, graph, tmp, indexes, visited)


    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        graph = defaultdict(list)
        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        visited = [0] * len(s)
        res = [None] * len(s)
        for i in range(len(s)):
            if visited[i] == 1:
                continue
            tmp = []
            indexes = []
            self.dfs(s, i, graph, tmp, indexes, visited)
            tmp.sort(reverse = True)
            indexes.sort()
            for index in indexes:
                res[index] = tmp[-1]
                tmp.pop()
        return "".join(res)
