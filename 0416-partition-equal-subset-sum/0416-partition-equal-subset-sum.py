class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        n = len(nums)

        dp = [False] * (target_sum + 1)
        dp[0] = True 

        for num in nums:
            for s in range(target_sum, num - 1, -1): 
                dp[s] = dp[s] or dp[s - num]

        return dp[target_sum]

class SolutionSet:
     def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        achievable_sums = {0} 
        
        for num in nums:
            sums_to_add = set()
            for s in achievable_sums:
                new_sum = s + num
                if new_sum == target:
                    return True
                if new_sum < target:
                     sums_to_add.add(new_sum)
            
            achievable_sums.update(sums_to_add)
            
        return False