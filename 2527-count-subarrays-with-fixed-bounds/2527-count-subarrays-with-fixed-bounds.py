class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        """
        Counts the number of fixed-bound subarrays using a single pass.

        Args:
            nums: The input list of integers.
            minK: The required minimum value in the subarray.
            maxK: The required maximum value in the subarray.

        Returns:
            The total count of fixed-bound subarrays (using 64-bit capacity via Python's ints).
        """
        n = len(nums)
        total_count = 0
        
        # Index of the leftmost boundary of the current potentially valid segment.
        # Any valid subarray must start strictly after left_bound.
        left_bound = -1 
        
        # Indices of the most recent occurrences of minK and maxK.
        last_minK_idx = -1
        last_maxK_idx = -1

        for i in range(n):
            num = nums[i]

            # Check if the current number invalidates the current segment.
            if num < minK or num > maxK:
                left_bound = i  # This element cannot be in a fixed-bound subarray
                                # Reset the start of the valid window

            # Update the last seen indices for minK and maxK.
            if num == minK:
                last_minK_idx = i
            if num == maxK:
                last_maxK_idx = i

            # Calculate the potential start of valid subarrays.
            # A valid start 'l' must satisfy:
            # 1. l > left_bound (to be within the current valid range [minK, maxK])
            # 2. l <= last_minK_idx (to include minK)
            # 3. l <= last_maxK_idx (to include maxK)
            # Combining 2 and 3: l <= min(last_minK_idx, last_maxK_idx)
            # Combining all: left_bound < l <= min(last_minK_idx, last_maxK_idx)
            
            # The number of valid 'l' is the length of the interval (left_bound, min(last_minK_idx, last_maxK_idx)]
            potential_starts = min(last_minK_idx, last_maxK_idx) 
            
            # Only add count if both minK and maxK have been seen within the current valid segment
            # (i.e., their last seen indices are > left_bound).
            # The number of valid start indices is max(0, potential_starts - left_bound).
            count_for_i = max(0, potential_starts - left_bound)
            
            total_count += count_for_i

        return total_count