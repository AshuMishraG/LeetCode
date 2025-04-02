class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0 

        if n < 3:
            return 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]: 
                    diff = nums[i] - nums[j]
                    for k in range(j + 1, n):
                        current_value = diff * nums[k] 
                        max_value = max(max_value, current_value)

        return max_value