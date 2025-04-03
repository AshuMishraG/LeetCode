class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        max_triplet_value = 0
        max_so_far = 0
        max_diff_so_far = 0

        for current_num in nums:
            
            if max_diff_so_far > 0:
                 potential_triplet = max_diff_so_far * current_num
                 max_triplet_value = max(max_triplet_value, potential_triplet)

            potential_new_diff = max_so_far - current_num
            max_diff_so_far = max(max_diff_so_far, potential_new_diff)

            max_so_far = max(max_so_far, current_num)
            
        return max_triplet_value