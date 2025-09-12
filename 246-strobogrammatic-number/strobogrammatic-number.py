class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mirror = {'0':'0', '8':'8','1':'1',"6":"9","9":"6"}
        start = 0
        end = len(num)-1
        while start<= end:
            if num[start] not in mirror or num[end] not in mirror:
                return False
            if num[start]!= mirror[num[end]]:
                return False
            start+=1
            end-=1
        return True