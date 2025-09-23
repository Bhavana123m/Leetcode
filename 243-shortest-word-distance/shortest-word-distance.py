class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortestDistance = len(wordsDict)
        p1 = -1
        p2 = -1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            elif wordsDict[i] == word2:
                p2 = i
            if p1 != -1 and p2 !=-1:
                shortestDistance = min(shortestDistance, abs(p1-p2))
        return shortestDistance