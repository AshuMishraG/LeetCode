class Solution:
  def sortColors(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    low = 0      # Pointer for the end of the 0s section
    mid = 0      # Pointer for the current element being processed
    high = n - 1 # Pointer for the start of the 2s section (from the right)

    # Iterate while the unprocessed section (mid to high) exists
    while mid <= high:
      if nums[mid] == 0:
        # If the element is 0, swap it with the element at 'low'
        nums[low], nums[mid] = nums[mid], nums[low]
        # Increment both 'low' and 'mid'
        low += 1
        mid += 1
      elif nums[mid] == 1:
        # If the element is 1, it's in the correct relative place, move to the next element
        mid += 1
      else: # nums[mid] == 2
        # If the element is 2, swap it with the element at 'high'
        nums[mid], nums[high] = nums[high], nums[mid]
        # Decrement 'high' (the 2s section grows from the right)
        # 'mid' stays, as the new nums[mid] needs to be processed
        high -= 1