class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        n = len(nums)
        
        # dp_even_prev: Max sum using a prefix of nodes, with an even number of them XORed.
        # dp_odd_prev: Max sum using a prefix of nodes, with an odd number of them XORed.
        
        # Base case: Before processing any nodes.
        # Sum is 0 with 0 (even) flips.
        dp_even_prev = 0 
        # It's impossible to have an odd number of flips if no nodes are processed,
        # or this state is considered infinitely bad.
        dp_odd_prev = float('-inf') 

        for i in range(n):
            val_original = nums[i]
            val_xor = nums[i] ^ k
            
            # Calculate current dp_even
            # Option 1: Don't XOR nums[i]. Need even flips from dp_even_prev.
            # Option 2: XOR nums[i]. Need odd flips from dp_odd_prev.
            current_dp_even = max(dp_even_prev + val_original, 
                                  dp_odd_prev + val_xor)
            
            # Calculate current dp_odd
            # Option 1: Don't XOR nums[i]. Need odd flips from dp_odd_prev.
            # Option 2: XOR nums[i]. Need even flips from dp_even_prev.
            current_dp_odd = max(dp_odd_prev + val_original, 
                                 dp_even_prev + val_xor)
            
            # Update states for the next iteration
            dp_even_prev = current_dp_even
            dp_odd_prev = current_dp_odd
            
        # The final answer must have an even number of total flips.
        return dp_even_prev