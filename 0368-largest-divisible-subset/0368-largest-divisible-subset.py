class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        nums.sort()

        dp = [1] * n 
        prev = [-1] * n 

        max_len = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i 

        result = []
        curr_idx = max_idx
        while curr_idx != -1:
            result.append(nums[curr_idx])
            curr_idx = prev[curr_idx] 
            
        return result[::-1] 