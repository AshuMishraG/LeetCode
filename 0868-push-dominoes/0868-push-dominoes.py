class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Solves the Push Dominoes problem using the segment processing approach.

        Args:
            dominoes: The initial state string.

        Returns:
            The final state string.
        """
        n = len(dominoes)
        # Convert to list for easy modification
        dom_list = list(dominoes)

        symbols = ['L'] + dom_list + ['R']
        res = list(symbols) # Create a mutable copy to work with
        
        left_boundary_idx = 0 # Index of the last non-'.' symbol found

        # Iterate through the symbols including sentinels
        for right_boundary_idx in range(1, len(symbols)):
            # Found the end of a potential '.' segment
            if symbols[right_boundary_idx] != '.':
                left_symbol = symbols[left_boundary_idx]
                right_symbol = symbols[right_boundary_idx]

                if left_symbol == right_symbol:
                    # Case 1: L...L or R...R
                    # Fill the entire segment with the boundary symbol
                    fill_char = left_symbol # Either 'L' or 'R'
                    for k in range(left_boundary_idx + 1, right_boundary_idx):
                        res[k] = fill_char
                
                elif left_symbol == 'R' and right_symbol == 'L':
                    # Case 2: R...L (Forces collide)
                    num_dots = right_boundary_idx - left_boundary_idx - 1
                    if num_dots > 0:
                        # Fill left half with 'R'
                        for k in range(left_boundary_idx + 1, left_boundary_idx + 1 + num_dots // 2):
                            res[k] = 'R'
                        # Fill right half with 'L'
                        # Start from right_boundary_idx - 1 and go leftwards
                        for k in range(right_boundary_idx - 1, right_boundary_idx - 1 - num_dots // 2, -1):
                            res[k] = 'L'

                # Update the left boundary for the next segment
                left_boundary_idx = right_boundary_idx

        # Remove the sentinels and join back into a string
        return "".join(res[1:-1])