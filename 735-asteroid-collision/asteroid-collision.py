class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            while stack and asteroid<0<stack[-1]:
                element = stack[-1]
                if abs(element)>abs(asteroid):
                    break
                elif abs(element)==abs(asteroid):
                    stack.pop()
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroid)
        return stack

        # for asteroid in asteroids:
        #     if asteroid>0:
        #         stack.append(asteroid)
        #     else:
        #         while stack:
        #             element = stack[-1]
        #             if abs(element)>abs(asteroid):
        #                 break
        #             elif abs(element)==abs(asteroid):
        #                 stack.pop()
        #                 break
        #             else:
        #                 stack.pop()
        # return stack

