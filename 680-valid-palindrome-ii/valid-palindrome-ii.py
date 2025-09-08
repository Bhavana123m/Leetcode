class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def palindrome_check_to_from(front, back):
            while front < back:
                if s[front] == s[back]:
                    front+=1
                    back -=1
                else:
                    return False
            return True
        front  = 0
        back = len(s)-1
        while front < back:
            if s[front] == s[back]:
                front+=1
                back-=1
            else:
                # Skip one char left or right
                return palindrome_check_to_from(front + 1, back) or palindrome_check_to_from(front, back - 1)
        return True







































































        # def is_palindrome_range(s, left, right):
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True

        # left, right = 0, len(s) - 1
        # while left < right:
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         # Try skipping left or right character
        #         return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        # return True

# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         count = 1
#         left =0
#         right = len(s)-1
#         while left<right:
#             if s[left] == s[right]:
#                 left+=1
#                 right-=1
#             else:
#                 print((left, right))
#                 if count==1:
#                     if left+1 < len(s) and s[left+1] == s[right]:
#                         left+=1
#                     elif right-1 > 0 and s[right-1] == s[left]:
#                         right-=1
#                     else:
#                         return False
#                     count-=1
#                 else:
#                     return False
#         return True
# aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga