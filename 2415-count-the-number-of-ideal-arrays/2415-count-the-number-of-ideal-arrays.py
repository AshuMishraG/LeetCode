MOD = 10**9 + 7
# Max length of distinct divisor chain v1 | ... | vk <= 10^4 is ~14.
# We might need combinations C(n-1, k-1) where k-1 is up to 14.
MAX_COMB_K_MINUS_1 = 14 # Corresponds to k up to 15
MAX_DP_K = MAX_COMB_K_MINUS_1 + 1 # k=15

# --- Modular Arithmetic Helpers ---
def fast_pow(base, power):
    """Calculates base^power % MOD."""
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        power //= 2
    # Ensure result is non-negative (Python handles negative results correctly, but good habit)
    return result

def inverse(a):
    """Calculates modular inverse using Fermat's Little Theorem (MOD is prime)."""
    # Handle inverse of 0 if it ever occurs, though unlikely in this context
    if a == 0: return 0 # Or raise an error
    return fast_pow(a, MOD - 2)

# Precompute modular inverses for numbers up to MAX_COMB_K_MINUS_1
# We need inv[r] where r = k-1 goes up to MAX_COMB_K_MINUS_1
inv = [1] * (MAX_COMB_K_MINUS_1 + 1) # inv[0] = 1 (or unused), inv[1]..inv[MAX_COMB_K_MINUS_1]
for i in range(1, MAX_COMB_K_MINUS_1 + 1):
    inv[i] = inverse(i)
# --- End Modular Arithmetic ---


class Solution:
    # Renamed method to match the expected name
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        Calculates the number of ideal arrays using dynamic programming and combinatorics.
        Time: O(MAX_K * maxValue * log(maxValue)) - Dominated by DP part
              If MAX_K is constant, O(maxValue * log(maxValue))
        Space: O(maxValue) for DP array
        """
        # dp[x]: number of strictly increasing divisor chains ending at x
        # We will update this array iteratively for k=1, k=2, ...
        # Initialize for k=1: dp[x] = 1 for all 1 <= x <= maxValue
        dp = [0] * (maxValue + 1)
        for i in range(1, maxValue + 1):
            dp[i] = 1

        total_ans = 0
        # Calculate C(n-1, k-1) iteratively. Start with C(n-1, 0) = 1
        comb_n_minus_1_k_minus_1 = 1

        # Determine the effective limit for DP calculations based on MAX_K
        limit_k = min(n, MAX_DP_K)
        dp_calculation_possible = True # Flag to track if DP calc should continue

        # Loop through possible lengths 'k' of the distinct value sequence up to n
        for k in range(1, n + 1):

            # 1. Calculate G(k) = sum(dp[1..maxValue]) if DP calculation is still possible
            gk = 0
            if dp_calculation_possible:
                # Sum up the current dp state to get G(k)
                # This sum corresponds to sequences of length k
                current_gk = sum(dp[1:]) % MOD
                if current_gk == 0 and k > 1: # Optimization: if no seq of length k, none for > k
                   dp_calculation_possible = False # Stop DP updates and G(k) calculation
                   gk = 0
                else:
                   gk = current_gk

                # If k reaches the calculated limit, stop future DP updates
                if k == limit_k:
                    dp_calculation_possible = False
            else:
                # If DP calculation stopped, G(k) for subsequent k is 0
                gk = 0


            # If gk is 0, no contribution from this k or any larger k based on DP limit.
            # If we stopped DP calc, we still need combinations if n is large.
            # However, if gk=0, the term added is 0 anyway. Let's check if we can break early.
            # If dp_calculation_possible is False AND gk is 0, all future terms will be 0.
            if not dp_calculation_possible and gk == 0:
                 break # Can break the main loop

            # 2. Get Combination C(n-1, k-1) -> comb_n_minus_1_k_minus_1
            if k > 1:
                # Update combination from C(n-1, k-2) to C(n-1, k-1)
                # C(N, r) = C(N, r-1) * (N - r + 1) / r
                # N = n-1, r = k-1
                numerator = (n - k + 1)
                if numerator < 0: # Avoid issues if n=k (comb becomes 0)
                    comb_n_minus_1_k_minus_1 = 0
                elif k - 1 <= MAX_COMB_K_MINUS_1:
                    # Ensure intermediate values stay positive if needed
                    comb_n_minus_1_k_minus_1 = (comb_n_minus_1_k_minus_1 * numerator) % MOD
                    # Use precomputed inverse for denominator k-1
                    comb_n_minus_1_k_minus_1 = (comb_n_minus_1_k_minus_1 * inv[k - 1]) % MOD
                else:
                    # If k-1 exceeds precomputed inverse range, calculate C(n-1, k-1) directly
                    # This happens if n is large, but k (distinct values) is small.
                    # We can calculate the inverse on the fly, but safer to use the iterative update.
                    # Since G(k) must be 0 if k > MAX_DP_K, this branch is complex.
                    # Let's rely on gk=0 check to break. If gk!=0 here, there's a logic flaw.
                    # If we reach here, it implies n is large, k is large ( > MAX_DP_K),
                    # but somehow gk was non-zero (which shouldn't happen).
                    # Or n is large, k <= MAX_DP_K, but k-1 > MAX_COMB_K_MINUS_1 (if estimates differ).
                    # Assume the gk == 0 check handles the cases where k > MAX_DP_K.
                    # If k-1 > MAX_COMB_K_MINUS_1, this implies MAX_K estimate was too small, but
                    # let's assume it's correct.
                    # Fallback: If combination becomes 0 due to numerator=0, it's handled.
                     pass # Rely on gk=0 break or numerator check

            # 3. Add contribution G(k) * C(n-1, k-1)
            term = (gk * comb_n_minus_1_k_minus_1) % MOD
            total_ans = (total_ans + term) % MOD


            # 4. Calculate dp_{k+1} from dp (which holds counts for length k)
            # Only do this if DP calculation should continue
            if dp_calculation_possible:
                dp_next = [0] * (maxValue + 1)
                # This loop is the performance bottleneck
                for y in range(1, maxValue + 1):
                    if dp[y] == 0: continue
                    # Add dp[y] to dp_next[x] for multiples x = m*y, m >= 2
                    # Iterate multiples efficiently
                    for x in range(y * 2, maxValue + 1, y):
                        dp_next[x] = (dp_next[x] + dp[y]) % MOD
                dp = dp_next # dp now holds counts for sequences of length k+1

        # Ensure final answer is positive modulo MOD
        return (total_ans + MOD) % MOD