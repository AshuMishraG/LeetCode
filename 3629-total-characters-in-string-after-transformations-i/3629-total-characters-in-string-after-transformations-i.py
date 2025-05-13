class Solution:
  def lengthAfterTransformations(self, s: str, t: int) -> int:
    MOD = 1_000_000_007

    if t == 0:
        # After 0 transformations, length of s is just len(s).
        # len(s) is at most 10^5, which is less than MOD.
        return len(s) 

    # dp_prev_lengths[i] stores L(chr(ord('a')+i), k-1)
    # Initialize for k=0: L(char, 0) = 1 for all characters.
    dp_prev_lengths = [1] * 26
    
    # dp_curr_lengths[i] will store L(chr(ord('a')+i), k)
    dp_curr_lengths = [0] * 26 

    # Loop for k from 1 to t transformations
    for _iteration_num in range(1, t + 1):
        # Calculate lengths for current number of transformations k
        # based on dp_prev_lengths (which holds lengths for k-1 transformations)

        # For 'a' through 'y' (char_code 0 to 24)
        # L(c, k) = L(next_char(c), k-1)
        for char_code in range(25): # 0 to 24
            dp_curr_lengths[char_code] = dp_prev_lengths[char_code + 1]
        
        # For 'z' (char_code 25)
        # L('z', k) = L('a', k-1) + L('b', k-1)
        dp_curr_lengths[25] = (dp_prev_lengths[0] + dp_prev_lengths[1]) % MOD
        
        # Current results become previous results for the next iteration.
        # Swap lists: dp_prev_lengths will point to the newly computed values,
        # and dp_curr_lengths will point to the older values (to be overwritten).
        dp_prev_lengths, dp_curr_lengths = dp_curr_lengths, dp_prev_lengths
    
    # After t iterations, dp_prev_lengths holds L(char, t) for each character.
    # (This is because dp_curr_lengths was last computed for transformation t,
    # and then swapped into dp_prev_lengths).
    
    final_total_length = 0
    for char_in_s in s:
        char_code = ord(char_in_s) - ord('a')
        final_total_length = (final_total_length + dp_prev_lengths[char_code]) % MOD
            
    return final_total_length