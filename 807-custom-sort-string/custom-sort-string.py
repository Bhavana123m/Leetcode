class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        out = []
        for ch in order:
            if ch in count:
                out.append(ch * count[ch])
                del count[ch]
        for ch, freq in count.items():
            out.append(ch * freq)

        return "".join(out)