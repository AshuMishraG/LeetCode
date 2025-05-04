class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        """
        Counts equivalent domino pairs using a canonical representation and a hash map.
        """
        canonical_counts = collections.defaultdict(int) # Stores counts of canonical forms
        pair_count = 0

        for domino in dominoes:
            a, b = domino[0], domino[1]
            # Create the canonical form (smaller number first)
            canonical = tuple(sorted((a, b))) # Using tuple(sorted()) is concise
            # Or: canonical = (min(a, b), max(a, b))

            # The current domino forms pairs with previously seen identical canonical forms
            current_count = canonical_counts[canonical]
            pair_count += current_count

            # Increment the count for this canonical form
            canonical_counts[canonical] += 1

        return pair_count