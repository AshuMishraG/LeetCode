class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        """
        Calculates the number of possible hidden sequences.

        Args:
            differences: A list of integers representing the differences between
                         consecutive elements of the hidden sequence.
            lower: The lower bound for the elements in the hidden sequence.
            upper: The upper bound for the elements in the hidden sequence.

        Returns:
            The number of possible hidden sequences, or 0 if none exist.
        """

        # Python's integers handle arbitrary size, so overflow isn't an issue
        # for the prefix sums themselves.

        current_sum = 0  # Represents the current prefix sum (relative value)
        min_prefix_sum = 0 # Tracks the minimum relative value encountered
        max_prefix_sum = 0 # Tracks the maximum relative value encountered

        # Calculate prefix sums iteratively and find the min/max relative values
        for diff in differences:
            current_sum += diff
            min_prefix_sum = min(min_prefix_sum, current_sum)
            max_prefix_sum = max(max_prefix_sum, current_sum)

        # Let the hidden sequence start with 'x'.
        # The elements are x + prefix_sum[k].
        # We need: lower <= x + prefix_sum[k] <= upper for all k.

        # The most restrictive bounds are:
        # lower <= x + min_prefix_sum  => x >= lower - min_prefix_sum
        # x + max_prefix_sum <= upper  => x <= upper - max_prefix_sum

        # Define the valid range for the starting element 'x'
        start_x = lower - min_prefix_sum
        end_x = upper - max_prefix_sum

        # Calculate the number of possible integer values for 'x'
        # If end_x < start_x, the range is invalid, so the count is 0.
        count = end_x - start_x + 1

        # Return the count, ensuring it's not negative
        return max(0, count)