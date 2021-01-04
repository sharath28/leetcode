class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        temp_dict = defaultdict(list)
        for item in items:
            temp_dict[item[0]].append(item[1])
        return_list = []
        for item in temp_dict:
            temp_list = temp_dict[item]
            temp_list = sorted(temp_list,reverse=True)
            sum_val = sum(temp_list[:5])
            return_list.append([item,sum_val//5])
        return return_list
