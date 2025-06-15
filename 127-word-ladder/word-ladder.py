class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + '*' + word[idx+1:]
                neighbors[pattern].append(word)
        visited = set([beginWord])
        q = [beginWord]
        path_length = 1
        while q:
            for _ in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return path_length
                for idx in range(len(word)):
                    pattern = word[:idx] + '*' + word[idx+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            path_length+=1
        return 0


