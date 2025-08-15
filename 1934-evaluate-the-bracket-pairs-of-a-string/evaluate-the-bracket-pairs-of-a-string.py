class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d={i[0]:i[1] for i in knowledge}
        t = s.split("(")
        ans = t[0]
        for i in range(1, len(t)):
            a, b = t[i].split(")")
            ans += d.get(a, "?") + b
        return ans

