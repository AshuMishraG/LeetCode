class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        ans = 0
        # min_i: index of the most recent min_k
        # max_i: index of the most recent max_k
        # i0: index of the most recent element *outside* the [min_k, max_k] range
        #     This acts as the "left boundary" - any valid subarray must start *after* i0.
        min_i = max_i = i0 = -1 
        
        for i, x in enumerate(nums):
            # Update the last seen index if x is min_k or max_k
            if x == min_k: min_i = i
            if x == max_k: max_i = i
            
            # If x is out of bounds, update the left boundary i0
            if not min_k <= x <= max_k: 
                i0 = i 
                # Note: Resetting min_i and max_i here is not needed,
                # because the condition `j > i0` below will handle it.
                
            # Determine the leftmost possible start index 'l' for a valid subarray ending at 'i'.
            # A valid subarray nums[l..i] must contain both min_k and max_k seen *after* i0.
            # Therefore, the start 'l' must be <= min_i and <= max_i.
            # So, the latest index that *must* be included is min(min_i, max_i).
            # Let's call this required latest start 'j'.
            # j = min(min_i, max_i) # Equivalent logic to the line below
            j = min_i if min_i < max_i else max_i # Slightly more concise way to write min(min_i, max_i)

            # Now, we need to count how many valid start indices 'l' exist for the subarray ending at 'i'.
            # Conditions for 'l':
            # 1. l > i0 (must be within the current valid segment)
            # 2. l <= j (must include the most recent min_k and max_k within the segment)
            # So, we need i0 < l <= j.
            
            # The number of integers 'l' in the range (i0, j] is j - i0.
            # This range is only valid if j > i0 (meaning both min_k and max_k were found
            # *after* the last invalid element).
            if j > i0: 
                ans += j - i0 # Add the count of valid starting positions for subarrays ending at i.
                
        return ans # Python's integers handle the potentially large count