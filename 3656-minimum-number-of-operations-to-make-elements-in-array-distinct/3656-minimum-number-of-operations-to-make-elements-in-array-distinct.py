class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        max_possible_ops = (n + 2) // 3

        for k in range(max_possible_ops + 1):
            start_index = min(3 * k, n)

            remaining_subarray = nums[start_index:]

            if len(set(remaining_subarray)) == len(remaining_subarray):
                return k

        return max_possible_ops