class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        """
        Calculates the minimum rotations to make one row equal.
        Checks candidates tops[0] and bottoms[0].
        """
        n = len(tops)

        # Helper function to check rotations for a given target value
        def check(target: int) -> int:
            rotations_top = 0  # Rotations to make tops[] equal to target
            rotations_bottom = 0 # Rotations to make bottoms[] equal to target

            for i in range(n):
                # If target is not present in the current domino, it's impossible
                if tops[i] != target and bottoms[i] != target:
                    return math.inf # Use infinity to signal impossibility for this target

                # Count rotations needed if we aim for the top row to be target
                elif tops[i] != target: # implies bottoms[i] == target
                    rotations_top += 1

                # Count rotations needed if we aim for the bottom row to be target
                elif bottoms[i] != target: # implies tops[i] == target
                    rotations_bottom += 1

            return min(rotations_top, rotations_bottom)

        # --- Main logic ---
        candidate1 = tops[0]
        candidate2 = bottoms[0]

        rotations1 = check(candidate1)

        # Only check candidate2 if it's different from candidate1
        if candidate1 != candidate2:
            rotations2 = check(candidate2)
        else:
            # If candidates are the same, the result is the same
            rotations2 = rotations1

        # Find the minimum rotations between the two candidates
        min_rotations = min(rotations1, rotations2)

        # If min_rotations is still infinity, it means neither candidate worked
        return min_rotations if min_rotations != math.inf else -1