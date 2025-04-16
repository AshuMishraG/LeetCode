import collections

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        """
        Counts the number of good subarrays using a sliding window approach.

        A subarray is good if it has at least k pairs (i, j) where i < j and nums[i] == nums[j].

        Args:
            nums: The input list of integers.
            k: The minimum number of pairs required for a subarray to be good.

        Returns:
            The total count of good subarrays.
        """
        n = len(nums)
        left = 0
        good_subarray_count = 0  # Use standard Python int (arbitrary precision)
        current_pairs = 0        # Use standard Python int
        counts = collections.defaultdict(int) # Stores frequency of numbers in the window [left, right]

        for right in range(n):
            # --- Expand Window (Add nums[right]) ---
            num_right = nums[right]

            # The number of new pairs formed by adding num_right is equal to its
            # current frequency *before* adding it.
            current_pairs += counts[num_right]

            # Increment the frequency of num_right
            counts[num_right] += 1

            # --- Shrink Window ---
            # While the current window [left, right] has enough pairs (>= k)
            # try to shrink it from the left to find the smallest valid window
            # ending at 'right'.
            while current_pairs >= k:
                num_left = nums[left]

                # Before removing num_left, its current count contributes pairs.
                # When removing it, we lose (counts[num_left] - 1) pairs.
                # (It stops forming pairs with the other counts[num_left]-1 occurrences).
                counts[num_left] -= 1
                current_pairs -= counts[num_left] # Subtract the *new* count

                # If the count drops to 0, we could optionally remove it from the dict
                # if counts[num_left] == 0:
                #    del counts[num_left] # Minor optimization, not strictly necessary

                # Move the left boundary
                left += 1

            # --- Count Subarrays ---
            # At this point, the window [left, right] has pairs < k (or k=0 initially).
            # However, any window [p, right] where 0 <= p < left *must* have had >= k pairs
            # before we shrunk the window past p.
            # The number of such starting points 'p' is 'left'.
            # So, there are 'left' good subarrays ending at the current 'right'.
            good_subarray_count += left

        return good_subarray_count