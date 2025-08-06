class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # https://leetcode.com/problems/zigzag-conversion/solutions/5995884/beginner-friendly-step-by-steps-solution-beats-100-user-in-each-solution-of-me
        if numRows == 1 or numRows >= len(s):
            return s
        result = ""
        rows = ['']*numRows
        curr_row = 0
        goingDown = False
        for c in s:
            rows[curr_row]+=c

            if curr_row == 0 or curr_row == numRows-1:
                goingDown = not goingDown
            
            if goingDown:
                curr_row+=1
            else:
                curr_row-=1
        return ''.join(rows)
            
