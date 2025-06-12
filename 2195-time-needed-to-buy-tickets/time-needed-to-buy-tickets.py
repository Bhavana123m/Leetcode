class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        value = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                time+=min(tickets[i], value)
            else:
                time+=min(tickets[i], value-1)
        return time