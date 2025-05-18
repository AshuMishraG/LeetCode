class Solution:
  def colorTheGrid(self, m: int, n: int) -> int:
    MOD = 10**9 + 7

    # Step 1: Generate valid column patterns
    # A pattern is a tuple of m colors (0, 1, or 2).
    # These patterns must satisfy: no two vertically adjacent cells have the same color.
    def generate_valid_column_patterns(m_rows: int) -> list[tuple[int, ...]]:
        if m_rows == 0: # Based on constraints m >= 1, this won't be hit.
            return [] 
        
        # Start with patterns for the first row (each pattern is (color,))
        current_level_patterns: list[tuple[int, ...]] = []
        for color_val in range(3): # 0, 1, 2 for the three colors
            current_level_patterns.append((color_val,))

        # Build patterns for subsequent rows by extending previous patterns
        # For _r from 1 to m_rows-1 (i.e., for row index 1 up to m-1)
        for _r in range(1, m_rows):
            next_level_patterns: list[tuple[int, ...]] = []
            for pattern_so_far in current_level_patterns:
                last_color_in_pattern = pattern_so_far[-1] # Color of cell (_r-1, current_col)
                for color_val in range(3): # Potential color for cell (_r, current_col)
                    if color_val != last_color_in_pattern: # Must differ from cell above
                        new_pattern = pattern_so_far + (color_val,) 
                        next_level_patterns.append(new_pattern)
            current_level_patterns = next_level_patterns
            if not current_level_patterns: # Should not occur with 3 available colors
                 break 
        return current_level_patterns

    valid_patterns = generate_valid_column_patterns(m)
    num_patterns = len(valid_patterns)

    if num_patterns == 0: # Safety, though m >= 1 implies num_patterns > 0
        return 0
    
    # Constraints: n >= 1.

    # Step 2: Precompute compatibility between patterns for column transitions
    # adj[prev_idx] stores a list of curr_idx, where valid_patterns[curr_idx]
    # can validly follow valid_patterns[prev_idx] in an adjacent column.
    adj: list[list[int]] = [[] for _ in range(num_patterns)]

    # Helper to check horizontal compatibility:
    # pattern1 from previous column, pattern2 from current column.
    # Compatible if all horizontally adjacent cells (pattern1[i] and pattern2[i]) have different colors.
    def check_horizontal_compatibility(p1: tuple[int, ...], p2: tuple[int, ...], m_rows: int) -> bool:
        for i in range(m_rows):
            if p1[i] == p2[i]: 
                return False
        return True

    for prev_idx in range(num_patterns):
        for curr_idx in range(num_patterns):
            if check_horizontal_compatibility(valid_patterns[prev_idx], valid_patterns[curr_idx], m):
                adj[prev_idx].append(curr_idx)

    # Step 3: Dynamic Programming
    # dp_prev[pattern_idx] = number of ways to color columns up to (k-1),
    #                          with the (k-1)-th column having pattern_idx.
    
    # Initialize for the first column (k=1).
    # Each valid pattern can form the first column in exactly one way.
    dp_prev = [1] * num_patterns

    # Iterate for columns k = 2 to n. This loop runs n-1 times.
    # If n=1, this loop is skipped, and the initial dp_prev is used.
    for _col_num in range(2, n + 1): 
        dp_curr = [0] * num_patterns
        for prev_idx in range(num_patterns):
            if dp_prev[prev_idx] == 0: # Optimization: no ways to reach this prev_pattern state
                continue
            # For each pattern that could be in the current column (curr_idx),
            # add the number of ways dp_prev[prev_idx] to reach it.
            for curr_idx in adj[prev_idx]:
                dp_curr[curr_idx] = (dp_curr[curr_idx] + dp_prev[prev_idx]) % MOD
        dp_prev = dp_curr # Current state becomes "previous" for the next column's calculation

    # Step 4: Final result
    # Sum of ways to color n columns, ending with any valid pattern in the n-th column.
    total_ways = 0
    for count in dp_prev:
        total_ways = (total_ways + count) % MOD
    
    return total_ways