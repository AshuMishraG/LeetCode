class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        Counts numbers with an even number of digits using optimized range checking.

        Args:
            nums: A list of integers.

        Returns:
            The count of numbers with an even number of digits.
        """
        even_digit_count = 0
        for num in nums:
            # Check if the number falls within the ranges for 2 or 4 digits, 
            # or if it's exactly the only 6-digit number possible (100000).
            if (10 <= num <= 99) or \
               (1000 <= num <= 9999) or \
               (num == 100000):
                even_digit_count += 1
                
        return even_digit_count
        
    # More Pythonic version using sum() and a generator expression:
    def findNumbers_pythonic_optimized(self, nums: list[int]) -> int:
        """
        Pythonic version of the optimized range checking approach.
        """
        return sum(1 for num in nums if (10 <= num <= 99) or \
                                         (1000 <= num <= 9999) or \
                                         (num == 100000))