# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """


        # https://leetcode.com/problems/find-the-celebrity/solutions/7056530/boyer-moore-s-algorithm
        candidate = 0
        for person in range(1, n):
            res = knows(candidate, person)
            if res:
                candidate = person
        for person in range(n):
            if person == candidate:
                continue
            if knows(candidate, person) or not knows(person, candidate):
                return -1
        return candidate