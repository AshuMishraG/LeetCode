class Solution:
  def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
    n = len(nums)
    
    # If nums is empty (though constraints say 1 <= n), it's vacuously a Zero Array.
    if n == 0:
        return True 

    # diff_array is used to calculate the total number of times each index 
    # can be decremented based on query ranges.
    # diff_array has size n + 1. Indices 0 to n.
    # An entry diff_array[i] = x means that starting from index i, 
    # the count of covering queries changes by x.
    diff_array = [0] * (n + 1) 
    
    for l_idx, r_idx in queries:
      # Increment count for the start of the interval
      diff_array[l_idx] += 1
      
      # Decrement count for one past the end of the interval.
      # Since r_idx is at most n-1, r_idx + 1 is at most n.
      # diff_array[n] is a valid index for diff_array of size n+1.
      diff_array[r_idx + 1] -= 1
          
    # Calculate prefix sums to find actual coverage for each index k
    current_coverage_at_k = 0
    for k in range(n): # Iterate through indices 0 to n-1 of the nums array
      current_coverage_at_k += diff_array[k]
      # Now, current_coverage_at_k is the total number of queries
      # that include index k in their range [l, r].
      
      # If nums[k] (initial value) needs more decrements than available
      # through all queries covering k, then it's impossible.
      if nums[k] > current_coverage_at_k:
        return False
        
    # If all elements nums[k] have nums[k] <= coverage_count[k],
    # it's possible to make them all zero.
    return True