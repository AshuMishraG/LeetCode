class Solution:
  def minSum(self, nums1: list[int], nums2: list[int]) -> int:
    sum1_val: int = 0
    zeros1_count: int = 0
    for x in nums1:
        if x == 0:
            zeros1_count += 1
        else:
            sum1_val += x

    sum2_val: int = 0
    zeros2_count: int = 0
    for x in nums2:
        if x == 0:
            zeros2_count += 1
        else:
            sum2_val += x

    # Calculate the sum for nums1 if all its zeros are replaced by 1s.
    # If zeros1_count is 0, this is sum1_val (the fixed sum of nums1).
    # Otherwise, it's the minimum possible sum nums1 can achieve.
    min_achievable_sum1 = sum1_val + zeros1_count
    
    # Similarly for nums2.
    min_achievable_sum2 = sum2_val + zeros2_count

    # Case 1: nums1 has no zeros, nums2 has no zeros.
    if zeros1_count == 0 and zeros2_count == 0:
        if sum1_val == sum2_val:
            return sum1_val
        else:
            return -1
    # Case 2: nums1 has no zeros, nums2 has zeros.
    # (The check zeros2_count > 0 is implicit due to Case 1 not matching)
    elif zeros1_count == 0: 
        # Target sum is sum1_val (fixed sum of nums1).
        # Possible if sum1_val >= min_achievable_sum2.
        if sum1_val >= min_achievable_sum2:
            return sum1_val
        else:
            return -1
    # Case 3: nums1 has zeros, nums2 has no zeros.
    # (The check zeros1_count > 0 is implicit due to Case 1 & 2 not matching)
    elif zeros2_count == 0: 
        # Target sum is sum2_val (fixed sum of nums2).
        # Possible if sum2_val >= min_achievable_sum1.
        if sum2_val >= min_achievable_sum1:
            return sum2_val
        else:
            return -1
    # Case 4: Both nums1 and nums2 have zeros.
    # (Implicitly zeros1_count > 0 and zeros2_count > 0)
    else: 
        # Both sums can be flexibly adjusted.
        # The minimum equal sum must be at least their respective minimums.
        return max(min_achievable_sum1, min_achievable_sum2)