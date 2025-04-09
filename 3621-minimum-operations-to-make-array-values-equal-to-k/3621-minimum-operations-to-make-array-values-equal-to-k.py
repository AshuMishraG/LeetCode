class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        distinct_greater_than_k = set()
        operations = 0

        for num in nums:
            if num < k:
                return -1

            if num > k:
                distinct_greater_than_k.add(num)

        return len(distinct_greater_than_k)