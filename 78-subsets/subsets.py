class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        def get_subsets(index, subsets, path):
            # print(path[:])
            subsets.append(path[:])
            # print(subsets)
            for i in range(index, len(nums)):
                path.append(nums[i])
                # print(path)
                # print(subsets)
                get_subsets(i+1,subsets, path)
                # print("Hi")
                path.pop()
                # print(i)

        get_subsets(0, subsets, [])
        return subsets

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     self.nums = nums
    #     subsets = []

    #     self.backtrack(0, subsets, [])
    #     return subsets
    
    # def backtrack(self, index, subsets, curr):
    #     subsets.append(curr[:])

    #     for i in range(index, len(self.nums)):

    #         curr.append(self.nums[i])
    #         self.backtrack(i + 1, subsets, curr)
    #         curr.pop()