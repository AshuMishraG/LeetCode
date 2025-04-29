class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts subarrays where the maximum element of the original array
        appears at least k times using a sliding window approach.

        Args:
            nums: The input list of integers.
            k: The minimum number of times the maximum element must appear.

        Returns:
            The total count of such subarrays.
        """
        n = len(nums)
        if n == 0:
            return 0

        # 1. Find the maximum element in the entire array
        # Using max() is concise and usually efficient enough (O(N))
        try:
            max_val = max(nums)
        except ValueError: # Handle case of empty list if constraints allowed
             return 0

        # Initialize sliding window variables and result
        left = 0
        max_val_count = 0
        result = 0 # Use standard Python integers (arbitrary precision)

        # 2. Iterate through the array with the right pointer
        for right in range(n):
            # Expand the window to the right
            if nums[right] == max_val:
                max_val_count += 1

            # 3. Shrink the window from the left while the condition is met
            # The condition `max_val_count >= k` means the window [left..right]
            # (and potentially shorter versions ending at right) is valid.
            # We shrink `left` until the window [left..right] is *just* invalid
            # (count < k) or becomes the minimal valid window.
            while max_val_count >= k:
                # Before moving `left`, check if we are losing a max_val
                if nums[left] == max_val:
                    max_val_count -= 1
                # Shrink the window
                left += 1

            result += left

        return result