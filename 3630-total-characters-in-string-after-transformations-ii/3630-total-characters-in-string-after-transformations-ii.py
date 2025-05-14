class Solution:
  def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
    MOD = 1_000_000_007
    D = 26 # Alphabet size

    if t == 0:
        return len(s) % MOD

    # Helper for matrix multiplication C = A_mat * B_mat
    def mat_mul(A_mat: list[list[int]], B_mat: list[list[int]]) -> list[list[int]]:
        C_mat = [[0] * D for _ in range(D)]
        for r_idx in range(D): # Row index for C_mat and A_mat
            for c_idx in range(D): # Column index for C_mat and B_mat
                current_sum = 0
                for k_idx in range(D): # Inner dimension
                    current_sum += A_mat[r_idx][k_idx] * B_mat[k_idx][c_idx]
                C_mat[r_idx][c_idx] = current_sum % MOD # Modulo after sum for the cell
        return C_mat

    # Helper for matrix power M_base^p_val using binary exponentiation
    def mat_pow(M_base: list[list[int]], p_val: int) -> list[list[int]]:
        res_mat = [[0] * D for _ in range(D)]
        for i in range(D):
            res_mat[i][i] = 1 # Start with identity matrix
        
        current_power_of_M = M_base # More descriptive name
        
        temp_p_val = p_val
        while temp_p_val > 0:
            if temp_p_val % 2 == 1:
                res_mat = mat_mul(res_mat, current_power_of_M)
            current_power_of_M = mat_mul(current_power_of_M, current_power_of_M)
            temp_p_val //= 2
        return res_mat

    # 1. Construct the transformation matrix A
    # A[orig_char_idx][expanded_to_char_idx] = count
    # This matrix defines: L_k[orig_char] = sum_{exp_char} A[orig_char][exp_char] * L_{k-1}[exp_char]
    # which in vector form is v_k = A * v_{k-1}
    A_matrix = [[0] * D for _ in range(D)]
    for orig_char_idx in range(D): # Character 'a' + orig_char_idx
        num_expansion = nums[orig_char_idx]
        for p_offset in range(1, num_expansion + 1):
            expanded_to_char_idx = (orig_char_idx + p_offset) % D
            A_matrix[orig_char_idx][expanded_to_char_idx] = \
                (A_matrix[orig_char_idx][expanded_to_char_idx] + 1) % MOD 
    
    # 2. Compute A_pow_t = A_matrix^t
    A_pow_t = mat_pow(A_matrix, t)
    
    # 3. L(c, t) = sum of elements in the c-th row of A_pow_t
    # final_len_for_each_start_char[c] will store L(c,t)
    final_len_for_each_start_char = [0] * D
    for char_idx_c in range(D): # This is 'c' in L(c,t)
        current_row_sum = 0
        for char_idx_j in range(D): # This is 'j' in sum over j
            current_row_sum = (current_row_sum + A_pow_t[char_idx_c][char_idx_j]) % MOD
        final_len_for_each_start_char[char_idx_c] = current_row_sum
        
    # 4. Calculate total length by summing L(s[i], t) for each char s[i] in original string
    total_final_len = 0
    for char_val_in_s in s:
        char_idx = ord(char_val_in_s) - ord('a')
        total_final_len = (total_final_len + final_len_for_each_start_char[char_idx]) % MOD
            
    return total_final_len