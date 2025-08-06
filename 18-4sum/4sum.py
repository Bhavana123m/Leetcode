class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ts = set()
                for k in range(j+1, len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    fourth = target - s
                    if(fourth in ts):
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k], fourth])))
                    ts.add(nums[k])
        return [list(t) for t in ans]

        
        # https://leetcode.com/problems/4sum/solutions/6938935/brute-force-hashmap-two-pointers-visual-walkthroughs-java-python-code-dry-runs
        # result = []
        # n = len(nums)
        # if n<4:
        #     return result
        # nums.sort()
        # for i in range(n-3):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1, n-2):
        #         if j > i+1 and nums[j] == nums[j-1]:
        #             continue
        #         left = j + 1
        #         right = n-1
        #         while left<right:
        #             total = nums[left] + nums[right] + nums[i] + nums[j]
        #             if total == target:
        #                 result.append([nums[i], nums[j], nums[left], nums[right]])
        #                 while left<right and nums[left+1] == nums[left]:
        #                     left+=1
        #                 while left< right and nums[right-1] == nums[right]:
        #                     right-=1
        #                 left+=1
        #                 right-=1
        #             elif total > target:
        #                 right-=1
        #             else:
        #                 left+=1
        # return result

       
        # result = set()

        # if len(nums)<4:
        #     return list(result)
        
        # sum_pair = {}
        # n = len(nums)

        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         total = nums[i]+nums[j]
        #         if total not in sum_pair:
        #             sum_pair[total] = []
        #         sum_pair[total].append((i,j))
        
        # for total, pairs1 in sum_pair.items():
        #     total2 = target - total
        #     if total2 not in sum_pair:
        #         continue
        #     else:
        #         pairs2 = sum_pair[total2]
        #         for pair1 in pairs1:
        #             for pair2 in pairs2:
        #                 if pair1[0]!=pair2[0] and pair1[0]!=pair2[1] and pair1[1]!=pair2[0] and pair1[1]!=pair2[1]:
        #                     quad = sorted([nums[pair1[0]], nums[pair1[1]], nums[pair2[0]], nums[pair2[1]]])
        #                     result.add(tuple(quad))
        
        # return list(result)
