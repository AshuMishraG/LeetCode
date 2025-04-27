class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        """
        Counts the number of subarrays of length 3 where the sum of the 
        first and third elements equals exactly half the second element.

        Args:
            nums: A list of integers.

        Returns:
            The count of such subarrays.
        """
        count = 0
        n = len(nums)

        # Constraints guarantee n >= 3, so the loop is safe.
        # We iterate through all possible starting indices for a subarray of length 3.
        # The last possible starting index is n - 3.
        # range(n - 2) goes from 0 up to (but not including) n - 2, so indices 0..n-3.
        for i in range(n - 2):
            # Extract the three elements
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]

            # Check the condition: a + c == b / 2  (exactly)
            # This is equivalent to checking: 2 * (a + c) == b
            # This multiplication avoids integer division issues and correctly
            # handles the "exactly half" requirement (b must be even).
            if 2 * (a + c) == b:
                count += 1

        return count