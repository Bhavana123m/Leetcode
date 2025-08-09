class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count_word = {}

        for word in words:
            if word not in count_word:
                count_word[word] = 1
            else:
                count_word[word]+=1
        heap = [(-count, word) for word, count in count_word.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
        

        