class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Calculate S_total: sum of all integers from 1 to n
        # S_total = n * (n + 1) // 2
        s_total = n * (n + 1) // 2

        # Calculate num2: sum of integers in [1, n] divisible by m
        
        # How many numbers from 1 to n are divisible by m?
        # These are m, 2m, 3m, ..., k*m where k*m <= n
        # So, k_max = n // m
        count_divisible_by_m = n // m
        
        # num2 = m * (1 + 2 + ... + count_divisible_by_m)
        # sum_1_to_k = k * (k + 1) // 2
        sum_of_multipliers = count_divisible_by_m * (count_divisible_by_m + 1) // 2
        num2 = m * sum_of_multipliers
        
        # We want num1 - num2.
        # Since S_total = num1 + num2, then num1 = S_total - num2.
        # So, num1 - num2 = (S_total - num2) - num2 = S_total - 2 * num2
        
        result = s_total - 2 * num2
        return result