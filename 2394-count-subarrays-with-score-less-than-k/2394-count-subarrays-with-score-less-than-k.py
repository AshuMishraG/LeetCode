class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Counts the number of subarrays whose score (sum * length) is strictly less than k.

        Args:
            nums: A list of positive integers.
            k: An integer threshold.

        Returns:
            The count of valid subarrays.
        """
        n = len(nums)
        count = 0
        current_sum = 0
        left = 0

        for right in range(n):
            # Expand the window by including nums[right]
            current_sum += nums[right]

            # Current window is nums[left...right]
            # Shrink the window from the left while the score is too high
            # The check `current_sum * (right - left + 1) >= k` is the core logic.
            # We ensure left doesn't cross right implicitly by the nature of the calculation.
            # If left > right, length becomes <= 0, score <= 0, which is < k (since k >= 1).
            while current_sum * (right - left + 1) >= k and left <= right : # Check left <= right for safety
                current_sum -= nums[left]
                left += 1
                # No need to recalculate score inside the loop, just re-check condition

            # After the while loop, the window nums[left...right] is the largest window
            # ending at 'right' with score < k.
            # All subarrays ending at 'right' with start index i >= left are valid.
            # The number of such subarrays is (right - left + 1).
            # If left > right after shrinking, this correctly adds 0.
            count += (right - left + 1)

        return count