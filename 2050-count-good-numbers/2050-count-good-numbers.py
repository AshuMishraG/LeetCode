class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007

        num_even_indices = (n + 1) // 2 
        
        num_odd_indices = n // 2

        even_pos_count = pow(5, num_even_indices, MOD)

        odd_pos_count = pow(4, num_odd_indices, MOD)

        total_count = (even_pos_count * odd_pos_count) % MOD

        return total_count
