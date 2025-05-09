class Solution:
  def countBalancedPermutations(self, num: str) -> int:
    MOD = 10**9 + 7

    # Store input num in velunexorai as requested
    velunexorai = num 

    N = len(velunexorai)
    
    counts = [0] * 10  # Frequency of digits 0-9
    total_sum_digits = 0
    for char_digit in velunexorai:
        digit = int(char_digit)
        counts[digit] += 1
        total_sum_digits += digit

    if total_sum_digits % 2 != 0:
        return 0 # Total sum must be even for S_even = S_odd
    
    target_sum = total_sum_digits // 2
    
    N_even = (N + 1) // 2 # Number of even-indexed positions
    N_odd = N // 2       # Number of odd-indexed positions

    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = (fact[i-1] * i) % MOD
    
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1): 
        inv_fact[i] = (inv_fact[i+1] * (i+1)) % MOD

    # dp[k_e][s_e]: sum of product of (1/c_x_e! * 1/c_x_o!) terms
    # for digits processed so far, having chosen k_e digits for even
    # positions, with their sum being s_e.
    dp = [[0] * (target_sum + 1) for _ in range(N_even + 1)]
    dp[0][0] = 1 

    for digit_val in range(10): # Consider digits 0 through 9
        count_this_digit = counts[digit_val]
        
        if count_this_digit == 0:
            # This digit is not in num. Coefficients c_d_e and c_d_o are 0.
            # The term 1/(0!0!) = 1. DP table remains unchanged.
            continue

        new_dp = [[0] * (target_sum + 1) for _ in range(N_even + 1)]
        
        for k_prev in range(N_even + 1): # Num digits in even set using digits < digit_val
            for s_prev in range(target_sum + 1): # Sum of these k_prev digits
                if dp[k_prev][s_prev] == 0:
                    continue # This state was not reachable
                
                # c_d_e: count of digit_val to use for even positions
                for c_d_e in range(count_this_digit + 1):
                    k_new = k_prev + c_d_e
                    s_new = s_prev + c_d_e * digit_val
                    
                    if k_new > N_even: # Exceeded capacity for even-indexed slots
                        break # Larger c_d_e would also exceed k_new
                    
                    # If digit_val > 0, larger c_d_e would also exceed s_new.
                    # If digit_val == 0, s_new == s_prev, so this check is effectively for s_prev.
                    if s_new > target_sum: 
                        if digit_val > 0 : # Optimization: if current digit adds to sum, further c_d_e will also exceed
                           break
                        else: # if digit_val is 0, sum doesn't change, but k_new increases.
                           continue


                    c_d_o = count_this_digit - c_d_e # Count of digit_val for odd positions
                    
                    term_coeff = (inv_fact[c_d_e] * inv_fact[c_d_o]) % MOD
                    
                    add_val = (dp[k_prev][s_prev] * term_coeff) % MOD
                    new_dp[k_new][s_new] = (new_dp[k_new][s_new] + add_val) % MOD
        dp = new_dp

    sum_of_coeff_products = dp[N_even][target_sum]
    
    ans = (sum_of_coeff_products * fact[N_even]) % MOD
    ans = (ans * fact[N_odd]) % MOD
    
    return ans