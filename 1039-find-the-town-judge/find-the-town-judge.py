class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_score = [0]*(n+1)
        for trustee, trusted in trust:
            trust_score[trustee] -=1
            trust_score[trusted] +=1
        for i in range(1, n+1):
            if trust_score[i] == n-1:
                return i
        return -1
        
        
        indegree = [0]*(n+1)
        outdegree = [0] * (n+1)

        for a,b in trust:
            outdegree[a]+=1
            indegree[b]+=1
        
        for i in range(1,n+1):
            if outdegree[i] == 0 and indegree[i] == n-1:
                return i
        return -1












































































        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        for i in range(1, n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1
        # if len(trust) == 1 and trust[0][1] == n:
        #     return n
        # trust_count = [0]*(n+1)
        # for (a, b) in trust:
        #     trust_count[a]-=1
        #     trust_count[b]+=1
        # print(trust_count)
        # for judge in range(1, len(trust_count)):
        #     if trust_count[judge] == n-1:
        #         return judge
        # return -1

