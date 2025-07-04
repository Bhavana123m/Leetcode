class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:  #Skip duplicates
                continue
            j = i+1
            k = n-1
            while j<k:
                sums = nums[i]+nums[j]+nums[k]
                if sums>0:
                    k-=1
                elif sums<0:
                    j+=1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
        return result
        
        # def is_duplicate(triplet, result_list):
        #     for t in result_list:
        #         if (
        #             (t[0] == triplet[0] and t[1] == triplet[1] and t[2] == triplet[2]) or
        #             (t[0] == triplet[0] and t[1] == triplet[2] and t[2] == triplet[1]) or
        #             (t[0] == triplet[1] and t[1] == triplet[0] and t[2] == triplet[2]) or
        #             (t[0] == triplet[1] and t[1] == triplet[2] and t[2] == triplet[0]) or
        #             (t[0] == triplet[2] and t[1] == triplet[0] and t[2] == triplet[1]) or
        #             (t[0] == triplet[2] and t[1] == triplet[1] and t[2] == triplet[0])
        #         ):
        #             return True
        #     return False

        # def two_sum_all(nums, target, index, result_list):
        #     seen = []
        #     for i in range(index+1, len(nums)):
        #         num = target - nums[i]
        #         if num in seen and not is_duplicate([nums[index], nums[i], num], result_list):
        #             result_list.append([nums[index], nums[i], num])
        #         seen.append(nums[i])
        #     # return result_list

        # # print(two_sum_all([0,1,2,3,4,2], 3))

        # result = []
        # for i in range(len(nums)):
        #     target = -nums[i]
        #     two_sum_all(nums, target, i, result)
        # return result

        














        
        # if len(nums) == 3:
        #     if sum(nums) == 0:
        #         return [nums]
        #     return []
        
        # result = set()
        # n, p, z = [], [], []
        # for num in nums:
        #     if num > 0:
        #         p.append(num)
        #     elif num < 0: 
        #         n.append(num)
        #     else:
        #         z.append(num)
        
        # N, P =set(n), set(p)

        # if len(z) >= 3:
        #     result.add((0, 0, 0))

        # if z:
        #     for num in P:
        #         if -num in N:
        #             result.add((-num, 0, num))
        # for i in range(len(p)):
        #     for j in range(i+1, len(p)):
        #         target = -(p[i] + p[j])
        #         if target in N:
        #             result.add(tuple(sorted([p[i],p[j],target])))
        # for i in range(len(n)):
        #     for j in range(i+1, len(n)):
        #         target = -(n[i]+n[j])
        #         if target in P:
        #             result.add(tuple(sorted([n[i], n[j], target])))
        
        # return [list(t) for t in result]
