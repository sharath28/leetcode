class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = ""
        l2_num = ""
        while l1 is not None:
            l1_num = l1_num + str(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2_num = l2_num + str(l2.val)
            l2 = l2.next
        l1_num = int(l1_num[::-1])
        l2_num = int(l2_num[::-1])
        sum = l1_num + l2_num
        sum_list = map(int,list(str(sum)))
        sum_list = sum_list[::-1]
        l3 = ListNode(0)
        l4 = l3
        print(sum_list)
        for i in range(len(sum_list)-1):
            l3.val = sum_list[i]
            next_node = ListNode(0)
            l3.next = next_node
            l3 = l3.next
        l3.val = sum_list[-1]
        return l4
