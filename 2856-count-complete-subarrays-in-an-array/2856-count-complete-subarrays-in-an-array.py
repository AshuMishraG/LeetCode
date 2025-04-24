import collections

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        """
        Counts the number of complete subarrays using a sliding window.

        Args:
            nums: A list of positive integers.

        Returns:
            The number of complete subarrays.
        """
        n = len(nums)
        # 1. Calculate the target number of distinct elements
        target_distinct = len(set(nums))

        count = 0
        left = 0
        window_freq = collections.Counter() # Frequency map for the current window

        # 2. Sliding Window using 'right' pointer
        for right in range(n):
            # 3. Expand the window
            window_freq[nums[right]] += 1

            # 4. Check condition and Shrink window while condition holds
            # While the window has the required number of distinct elements
            while len(window_freq) == target_distinct:
                # 5. Count subarrays
                # The current window nums[left..right] is complete.
                # All subarrays starting at 'left' and ending at 'right' or later
                # (i.e., nums[left..right], nums[left..right+1], ..., nums[left..n-1])
                # are also complete. There are (n - 1 - right + 1) = n - right such subarrays.
                count += (n - right)

                # Shrink the window from the left
                window_freq[nums[left]] -= 1
                if window_freq[nums[left]] == 0:
                    del window_freq[nums[left]] # Remove element if count is zero
                left += 1 # Move the left pointer

        return count