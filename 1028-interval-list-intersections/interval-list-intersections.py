class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]
            low = max(a1, b1)
            high = min(a2, b2)

            if low <= high:
                res.append([low, high])
            
            if a2<b2:
                i+=1
            else:
                j+=1
        return res