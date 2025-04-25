class Solution:
    """
    Finds the count of interesting subarrays using prefix sums and a frequency map.
    An interesting subarray nums[l..r] has cnt % modulo == k, where cnt is the
    number of elements nums[i] (l <= i <= r) such that nums[i] % modulo == k.
    """
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        """
        Args:
            nums: The input list of integers.
            modulo: The modulo value for the conditions.
            k: The target remainder value for the conditions.

        Returns:
            The total count of interesting subarrays. Python integers handle arbitrary size,
            so overflow is not an issue for the count.
        """
        n = len(nums)
        # freq map stores counts of prefix count remainders encountered so far.
        # Key: prefix_cnt % modulo, Value: count of occurrences
        # Using defaultdict simplifies lookup and initialization (defaults to 0).
        freq = collections.defaultdict(int)
        
        # Initialize for the empty prefix (before index 0).
        # The count of relevant elements (P[0]) is 0. The remainder is 0 % modulo = 0.
        # This frequency count (freq[0]=1) represents the possibility of starting
        # a subarray from index 0 (l=0).
        freq[0] = 1
        
        current_prefix_cnt = 0 # Tracks the running count of elements where nums[i] % modulo == k.
                               # This corresponds to P[i+1] after processing index i.
        total_interesting_subarrays = 0 # Accumulates the final count.

        # Iterate through the array nums
        for i in range(n):
            # Update the prefix count based on the current element nums[i]
            if nums[i] % modulo == k:
                current_prefix_cnt += 1
            
            # Calculate the remainder of the current prefix count with respect to modulo.
            # This is P[i+1] % modulo.
            current_prefix_cnt_mod = current_prefix_cnt % modulo
            
            # We need to find the number of starting indices l (l <= i) such that
            # the subarray nums[l..i] is interesting. The condition translates to:
            # P[l] % modulo == (P[i+1] % modulo - k + modulo) % modulo
            # Calculate the target remainder required for P[l] % modulo.
            target_mod = (current_prefix_cnt_mod - k + modulo) % modulo
            
            # Look up how many previous prefix sums P[l] had this target remainder.
            # Each such P[l] corresponds to a valid start 'l' for an interesting subarray ending at 'i'.
            total_interesting_subarrays += freq[target_mod]
            
            # Update the frequency map: Record the remainder of the current prefix count P[i+1].
            freq[current_prefix_cnt_mod] += 1
            
        return total_interesting_subarrays