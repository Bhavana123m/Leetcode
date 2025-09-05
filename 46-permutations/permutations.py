class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False] * len(nums)
        permutations = []

        def get_perm(permutaions, path):
            if len(path) == len(nums):
                permutations.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                get_perm(permutations, path)
                path.pop()
                used[i] = False

        get_perm(permutations, [])
        return permutations
        
        # permutations = []

        # def get_perm(permutaions, path):
        #     if len(path) == len(nums):
        #         permutations.append(path[:])
        #         return
        #     for i in range(len(nums)):
        #         if nums[i] not in path:
        #             path.append(nums[i])
        #             get_perm(permutations, path)
        #             path.pop()

        # get_perm(permutations, [])
        # return permutations















































        
        # res = []
        # n = len(nums)
        # if n==1:
        #     return [[nums[0]]]
        # for i in range(n):
        #     num = nums.pop(i)
        #     perm = self.permute(nums)
        #     for each in perm:
        #         each.append(num)
        #     res+=perm
        #     nums.insert(i,num)
        # return res

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # result = []
        # path = []
        # used = [False] * len(nums)

        # def backtrack():
        #     if len(path) == len(nums):
        #         result.append(path[:])
        #         return
        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
        #         used[i] = True
        #         path.append(nums[i])
        #         backtrack()
        #         path.pop()
        #         used[i] = False

        # backtrack()
        # return result