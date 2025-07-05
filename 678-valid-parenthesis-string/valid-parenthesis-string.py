class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min = 0
        max = 0
        for c in s:
            if c == '(':
                min+=1
                max+=1
            elif c == ')':
                min-=1
                max-=1
            else:
                min-=1
                max+=1
            if max < 0:
                return False
            if min < 0:
                min = 0
        return min == 0

        # if s[0] == ')':
        #     return False
        # if s[len(s)-1] == '(':
        #     return False
        # count = 0
        # wild_card_count = 0
        # for c in s:
        #     if c == '(':
        #         count += 1
        #     elif c == ')':
        #         if count > 0:
        #             count -= 1
        #         elif wild_card_count > 0:
        #             wild_card_count -= 1
        #         else:
        #             return False
        #     elif c == '*':
        #         wild_card_count += 1

        # if count == 0:
        #     return True
        # # At this point, unmatched '(' left in count
        # if wild_card_count >= count:
        #     return True
        # return False
        # for c in s:
        #     if count<0 and wild_card_count == 0:
        #         return False
        #     if c == '(':
        #         count+=1
        #     elif c == ')':
        #         count-=1
        #     elif c == '*':
        #         wild_card_count+=1
        # if count == 0:
        #     return True
        # if count > 0:
        #     if wild_card_count-count>=0:
        #         return True
        #     return False
        # if count < 0:
        #     if wild_card_count+count>=0:
        #         return True
        #     return False
            