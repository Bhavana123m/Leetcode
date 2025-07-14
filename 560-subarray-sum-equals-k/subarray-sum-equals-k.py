class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix_arr = [0]*n
        prefix_arr[0] = nums[0]
        for i in range(1, n):
            prefix_arr[i] = prefix_arr[i-1]+nums[i]

        map_count = defaultdict(int)
        count = 0
        for i in range(n):
            if prefix_arr[i]==k:
                count+=1
            need = prefix_arr[i] - k
            if need in map_count:
                count += map_count[need]
            map_count[prefix_arr[i]] = map_count.get(prefix_arr[i], 0) + 1

        return count
