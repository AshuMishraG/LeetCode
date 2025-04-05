class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        overall_or = 0
        for x in nums:
            overall_or |= x

        multiplier = 1 << (n - 1)
        
        return overall_or * multiplier