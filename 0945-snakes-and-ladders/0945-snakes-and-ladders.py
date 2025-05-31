class Solution:
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)
    target_square = n * n

    # Helper function to convert a 1-indexed square number 
    # to its 0-indexed (row, col) on the board.
    def get_coordinates(square_num: int) -> Tuple[int, int]:
        # Convert square_num to 0-indexed for easier calculation (0 to n*n-1)
        adjusted_s = square_num - 1 
        
        # Determine the 'row from bottom' (0-indexed). 
        # Example: for n=6, squares 1-6 (adjusted_s 0-5) are in row_from_bottom = 0.
        # Squares 7-12 (adjusted_s 6-11) are in row_from_bottom = 1.
        row_from_bottom = adjusted_s // n
        
        # Determine the actual board row index (0-indexed from top).
        # If row_from_bottom is 0, it's board row n-1 (the last row).
        # If row_from_bottom is 1, it's board row n-2.
        r = (n - 1) - row_from_bottom
        
        # Determine the column index (0-indexed).
        # This depends on the direction of numbering for that logical row.
        c: int
        if row_from_bottom % 2 == 0:  # Even row_from_bottom (0, 2, ...) means Left-to-Right numbering
            c = adjusted_s % n
        else:  # Odd row_from_bottom (1, 3, ...) means Right-to-Left numbering
            c = (n - 1) - (adjusted_s % n)
        return r, c

    # --- BFS Algorithm ---
    # State in queue: (current_square_number, moves_taken)
    queue: Deque[Tuple[int, int]] = collections.deque()
    queue.append((1, 0))  # Start at square 1, 0 moves made

    # 'visited' set stores square numbers that have been added to the queue.
    visited: Set[int] = {1}

    while queue:
        current_square, moves = queue.popleft()

        if current_square == target_square:
            return moves  # Reached the destination

        # Simulate a 6-sided die roll
        for die_roll in range(1, 7): # die_roll values: 1, 2, 3, 4, 5, 6
            next_potential_square = current_square + die_roll
            
            if next_potential_square > target_square:
                # Optimization: If this roll overshoots, subsequent larger rolls will too.
                break 

            r_land, c_land = get_coordinates(next_potential_square)
            
            final_destination_square: int
            if board[r_land][c_land] != -1:
                # Snake or ladder encountered. Move to its destination.
                final_destination_square = board[r_land][c_land]
            else:
                # No snake or ladder, land on the potential square.
                final_destination_square = next_potential_square
            
            if final_destination_square not in visited:
                visited.add(final_destination_square)
                queue.append((final_destination_square, moves + 1))
    
    # Target not reachable if queue empties
    return -1