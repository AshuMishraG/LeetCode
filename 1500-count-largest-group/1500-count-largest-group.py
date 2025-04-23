class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Counts the number of groups with the largest size, where grouping
        is based on the sum of digits.

        Args:
            n: The upper limit of numbers to consider (inclusive).

        Returns:
            The number of groups that have the largest size.
        """

        def get_digit_sum(num: int) -> int:
            """Helper function to calculate the sum of digits."""
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        # Max possible sum for n <= 10000 is 9+9+9+9 = 36.
        # Array indices 1 to 36 will store counts.
        group_counts = [0] * 37

        # Populate the counts for each digit sum group
        for i in range(1, n + 1):
            digit_sum = get_digit_sum(i)
            # Ensure the sum is within bounds (although it always will be for i >= 1)
            if 1 <= digit_sum < len(group_counts):
                group_counts[digit_sum] += 1

        max_size = 0
        # Find the maximum size among all groups (excluding index 0)
        # We can iterate directly over the relevant part of the list
        for size in group_counts[1:]: # Only consider sums from 1 upwards
             if size > max_size:
                 max_size = size

        # Count how many groups reached the maximum size
        result_count = 0
        if max_size == 0: # Edge case if n=0 (though constraints say n>=1)
             return 0

        for size in group_counts[1:]:
            if size == max_size:
                result_count += 1

        return result_count

    # Alternative single-pass approach after populating counts:
    def countLargestGroup_single_pass(self, n: int) -> int:
        def get_digit_sum(num: int) -> int:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        group_counts = [0] * 37
        for i in range(1, n + 1):
            digit_sum = get_digit_sum(i)
            if 1 <= digit_sum < len(group_counts):
                group_counts[digit_sum] += 1

        max_size = 0
        result_count = 0
        # Iterate counts (index 1 to 36) to find max and count simultaneously
        for size in group_counts[1:]:
            if size > max_size:
                max_size = size
                result_count = 1  # Reset count for the new max size
            elif size == max_size:
                # Only increment if max_size is actually positive
                # Ensures we don't count groups of size 0 if n is small
                if max_size > 0:
                    result_count += 1 # Another group matches the current max

        return result_count