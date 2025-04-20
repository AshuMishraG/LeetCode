class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Counts the number of fair pairs (i, j) such that i < j and
        lower <= nums[i] + nums[j] <= upper.

        Args:
            nums: The input array of integers.
            lower: The lower bound for the pair sum (inclusive).
            upper: The upper bound for the pair sum (inclusive).

        Returns:
            The total count of fair pairs.
        """
        n = len(nums)
        nums.sort() # O(N log N)

        def count_pairs_le(target: int) -> int:
            """
            Counts pairs (i, j) with i < j such that nums[i] + nums[j] <= target
            using two pointers on the sorted nums array. Runs in O(N).
            """
            count = 0
            left = 0
            right = n - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    # If nums[left] + nums[right] <= target, then nums[left] can
                    # be paired with any element from nums[left+1] up to nums[right].
                    # The number of such elements is right - left.
                    count += (right - left)
                    left += 1 # Move left pointer to find pairs for the next element
                else:
                    # Sum is too large, need to decrease the sum by moving right pointer
                    right -= 1
            return count

        # Calculate count where sum <= upper
        count_upper = count_pairs_le(upper)

        # Calculate count where sum <= lower - 1 (or sum < lower)
        count_lower_minus_1 = count_pairs_le(lower - 1)

        # The result is the difference
        return count_upper - count_lower_minus_1