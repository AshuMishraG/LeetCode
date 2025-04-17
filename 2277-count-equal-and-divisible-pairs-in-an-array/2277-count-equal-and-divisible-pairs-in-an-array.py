import math # Although not strictly needed for modulo, good habit for math ops
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        Counts pairs (i, j) such that i < j, nums[i] == nums[j], and (i * j) % k == 0.

        Args:
            nums: A list of integers.
            k: An integer divisor.

        Returns:
            The number of valid pairs.
        """
        count = 0
        n = len(nums)

        # Iterate through all possible pairs (i, j) where 0 <= i < j < n
        for i in range(n):
            for j in range(i + 1, n):
                # Check the first condition: nums[i] == nums[j]
                if nums[i] == nums[j]:
                    # If the first condition is met, check the second: (i * j) is divisible by k
                    # The modulo operator (%) gives the remainder of a division.
                    # If the remainder is 0, the number is divisible.
                    if (i * j) % k == 0:
                        # Both conditions met, increment the count
                        count += 1

        return count
