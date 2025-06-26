class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # We can go by other logic as well that 2 edges should have one node in common and that is our center node
        a,b = edges[0]
        c,d = edges[1]
        if a == c or a == d:
            return a
        return b


        edge_count = [0]*(len(edges)+2)
        for u, v in edges:
            edge_count[u]+=1
            edge_count[v]+=1
        for i in range(1,len(edges)+2):
            if edge_count[i] > 1:
                return i