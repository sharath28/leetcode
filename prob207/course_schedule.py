class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        course_dict = defaultdict(list)

        for relation in prerequisites:
            next_course, prev_course = relation[0],relation[1]
            course_dict[prev_course].append(next_course)

        path = [False]*numCourses

        for curr_course in range(numCourses):
            if self.isCyclic(curr_course, course_dict, path):
                return False
        return True

    def isCyclic(self,curr_course,course_dict,path):
        if path[curr_course]:
            return True

        path[curr_course] = True

        ret = False

        for child in course_dict[curr_course]:
            ret = self.isCyclic(child,course_dict,path)
            if ret:break
        path[curr_course] = False
        return ret
