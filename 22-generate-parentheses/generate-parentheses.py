class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # can only add a '(' if you still have some left (open_count > 0).
        # can only add a ')' if it won’t lead to invalid syntax (i.e., close_count > open_count).
        # Backtrack — undo the last added character — to explore other possibilities 
        # to ensure that explore all paths efficiently without duplicating work or going into invalid branches

        if n == 1:
            return ["()"]
        def generate(current, open_count, close_count, result):
            # Base case: if no more brackets left to add
            if open_count == 0 and close_count == 0:
                result.append("".join(current))
                return
            # Add '(' if we still have open brackets left
            if open_count > 0:
                current.append('(')
                generate(current, open_count-1, close_count, result)
                current.pop()
            # Add ')' only if it won't lead to invalid sequence
            if close_count > open_count:
                current.append(')')
                generate(current, open_count, close_count-1, result) 
                current.pop()
            # if open_count == close_count:
            #     current.append('(')
            #     generate(current, open_count-1, close_count, result)
            # elif open_count == 0:
            #     valid_paranthesis.append(')')
            #     generate(current, open_count, close_count-1, result)
            # elif close_count == 0:
            #     valid_paranthesis.append('(')
            #     generate(current, open_count-1, close_count, result)
            # else:

            
            
        result = []
        open_brackets_count = n
        close_brackets_count = n
        generate([], open_brackets_count, close_brackets_count, result)
        
        return result

            