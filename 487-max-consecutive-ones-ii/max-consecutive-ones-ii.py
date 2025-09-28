class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Returns the maximum number of consecutive 1s after flipping at most one 0.
        """

        # Initialize left boundary of the sliding window.
        left = 0
        # Count of zeros currently inside the window [left..right].
        zero_count = 0
        # Variable to track the best (maximum) window length seen so far.
        best = 0

        # Iterate right boundary from 0 to len(nums)-1.
        right = 0
        while right < len(nums):
            # If the current element is zero, increase the zero counter.
            if nums[right] == 0:
                zero_count += 1

            # If we now have more than one zero, shrink the window from the left
            # until the window again has at most one zero.
            while zero_count > 1:
                # If the element leaving the window is zero, decrement the counter.
                if nums[left] == 0:
                    zero_count -= 1
                # Move left boundary forward.
                left += 1

            # Update the best length with the current valid window size.
            # Window size is (right - left + 1).
            current_len = right - left + 1
            if current_len > best:
                best = current_len

            # Move the right boundary forward to expand the window.
            right += 1

        # 'best' is the length of the largest window containing at most one zero,
        # which corresponds to flipping at most one zero.
        return best
