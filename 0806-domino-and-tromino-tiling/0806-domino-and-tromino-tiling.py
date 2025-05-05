class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        # Base cases handled by initial values
        if n == 0:
            return 0 # Or 1 depending on interpretation, problem constraints say n >= 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp_k_minus_3 = 1  # Corresponds to f(0) for the first iteration (k=3)
        dp_k_minus_2 = 1  # Corresponds to f(1) for the first iteration (k=3)
        dp_k_minus_1 = 2  # Corresponds to f(2) for the first iteration (k=3)

        for k in range(3, n + 1):
            # Calculate dp_k = (2 * dp_k_minus_1 + dp_k_minus_3) % MOD
            # Use temporary variable to avoid modifying dp_k_minus_1 too early
            dp_k = (2 * dp_k_minus_1 + dp_k_minus_3) % MOD

            # Update states for the next iteration (k+1)
            # The old dp_k_minus_2 becomes the new dp_k_minus_3
            # The old dp_k_minus_1 becomes the new dp_k_minus_2
            # The current dp_k becomes the new dp_k_minus_1
            dp_k_minus_3 = dp_k_minus_2
            dp_k_minus_2 = dp_k_minus_1
            dp_k_minus_1 = dp_k

        # After the loop, dp_k_minus_1 holds the value for f(n)
        return dp_k_minus_1