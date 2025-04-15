class BIT:
    """Binary Indexed Tree (Fenwick Tree) implementation."""
    def __init__(self, size):
        # Initialize tree with zeros. size is the number of elements (n)
        # Use size + 1 because BIT uses 1-based indexing internally
        self.tree = [0] * (size + 1)
        self.size = size + 1

    def update(self, idx, delta):
        """Adds delta to element at index idx (0-based)."""
        idx += 1 # Convert to 1-based index
        while idx < self.size:
            self.tree[idx] += delta
            # Move to the next node that contains this index
            idx += idx & (-idx) 

    def query(self, idx):
        """Queries prefix sum up to index idx (0-based)."""
        idx += 1 # Convert to 1-based index
        s = 0
        while idx > 0:
            s += self.tree[idx]
            # Move to the parent node
            idx -= idx & (-idx) 
        return s

class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        
        # Step 1: Create mapping from value to its index in nums2
        pos2_map = [0] * n
        for i in range(n):
            pos2_map[nums2[i]] = i

        # Step 2: Calculate left_counts using BIT (prefix sums)
        bit_prefix = BIT(n)
        left_counts = [0] * n
        for i in range(n):
            val = nums1[i]
            pos2_val = pos2_map[val]
            # Query count of elements seen *before* i (in nums1) AND *before* pos2_val (in nums2)
            # Query up to index pos2_val - 1 (inclusive)
            if pos2_val > 0:
                 left_counts[i] = bit_prefix.query(pos2_val - 1)
            else:
                 left_counts[i] = 0 # No elements have pos2 < 0
            
            # Update BIT with the current element's pos2
            bit_prefix.update(pos2_val, 1)

        # Step 3: Calculate right_counts using BIT (suffix sums)
        bit_suffix = BIT(n)
        right_counts = [0] * n
        for i in range(n - 1, -1, -1):
            val = nums1[i]
            pos2_val = pos2_map[val]
            
            # Query count of elements seen *after* i (in nums1, based on backward pass)
            # AND *after* pos2_val (in nums2)
            # Total elements seen so far - elements seen with pos2 <= pos2_val
            total_seen = bit_suffix.query(n - 1) # Query sum up to n-1 (all elements seen so far)
            elements_le_pos2_val = bit_suffix.query(pos2_val) # Query sum up to pos2_val
            right_counts[i] = total_seen - elements_le_pos2_val
            
            # Update BIT with the current element's pos2
            bit_suffix.update(pos2_val, 1)

        # Step 4: Calculate total good triplets
        total_good_triplets = 0
        for i in range(n):
            total_good_triplets += left_counts[i] * right_counts[i]

        return total_good_triplets