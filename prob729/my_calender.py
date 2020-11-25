class MyCalendar(object):

    def __init__(self):
        self.booked_list = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for booked in self.booked_list:
            if booked[0]<end and booked[1]>start:
                return False
        self.booked_list.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
