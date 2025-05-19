class Solution:
  def triangleType(self, nums: list[int]) -> str:
    # It's easier to work with individual side lengths.
    # Constraints state nums.length == 3.
    s1 = nums[0]
    s2 = nums[1]
    s3 = nums[2]

    # Step 1: Check the triangle inequality theorem.
    # To simplify, sort the sides. Let a <= b <= c.
    # We only need to check if a + b > c.
    # (The problem statement implies nums[i] >= 1, so sides are positive.)
    
    sides = sorted(nums) # Creates a new sorted list [a, b, c]
    a, b, c = sides[0], sides[1], sides[2]

    if a + b <= c:
      return "none"

    # Step 2: If it's a valid triangle, classify it.
    # We use the original s1, s2, s3 for clarity in matching sides,
    # though it could also be done with a, b, c.
    
    # Check for equilateral (all three sides equal)
    if s1 == s2 and s2 == s3: # s1 == s2 == s3 is also valid Python
      return "equilateral"
    
    # Check for isosceles (exactly two sides equal)
    # Since we've already handled equilateral, if any pair is equal,
    # it implies exactly two are equal.
    elif s1 == s2 or s1 == s3 or s2 == s3:
      return "isosceles"
      
    # Check for scalene (all sides different)
    else:
      return "scalene"