class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        p_dict = {}
        for i in range(len(ppid)):
            if ppid[i] not in p_dict:
                p_dict[ppid[i]] = [pid[i]]
            else:
                p_dict[ppid[i]].append(pid[i])
        kill_list = []
        queue = [kill]
        while queue:
            p = queue.pop(0)
            kill_list.append(p)
            if p in p_dict:
                queue += p_dict[p]
        return kill_list
                
