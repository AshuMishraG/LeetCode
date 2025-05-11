class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3: # Cannot have 3 consecutive if array is too short
            return False
        
        # Iterate up to the point where a window of 3 elements can start
        # arr[i], arr[i+1], arr[i+2]
        for i in range(n - 2): 
            if arr[i] % 2 != 0 and \
               arr[i+1] % 2 != 0 and \
               arr[i+2] % 2 != 0:
                return True
        return False