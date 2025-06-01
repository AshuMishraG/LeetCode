class Solution:
  def distributeCandies(self, n: int, limit: int) -> int:
    
    # Helper function to calculate C(val + 2, 2)
    # This is the number of ways to distribute 'val' candies among 3 children
    # with only the constraint that each child receives >= 0 candies.
    # Formula: (val+2)*(val+1)/2
    def ways(val: int) -> int:
        if val < 0:
            return 0
        # Python's integers handle arbitrary size, so no overflow for intermediate products.
        return (val + 2) * (val + 1) // 2

    # k_bad is the minimum number of candies a child must receive to violate the limit.
    # If a child has x_i candies, x_i > limit is equivalent to x_i >= limit + 1.
    k_bad = limit + 1
    
    ans = 0
    
    # Term 1: Total ways to distribute n candies among 3 children without an upper limit.
    ans += ways(n)
    
    # Term 2: Subtract cases where at least one child violates the limit.
    # There are C(3,1) = 3 ways to choose which child violates the limit.
    # If one child (say, child 1) gets > limit candies (i.e., >= k_bad),
    # we pre-assign k_bad candies to child 1. The remaining sum is n - k_bad.
    # Distribute these n - k_bad candies among the 3 children.
    ans -= 3 * ways(n - k_bad)

    ans += 3 * ways(n - 2 * k_bad)
    
    ans -= ways(n - 3 * k_bad)
            
    return ans