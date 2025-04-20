class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Calculates the minimum number of rabbits in the forest.

        Args:
            answers: A list of integers where answers[i] is the answer of the ith rabbit.

        Returns:
            The minimum total number of rabbits.
        """
        if not answers:
            return 0

        answer_counts = Counter(answers) # Efficiently count occurrences of each answer
        total_rabbits = 0

        for x, k in answer_counts.items():
            # x is the answer given by k rabbits.
            # Each such rabbit claims to be in a group of size x + 1.
            group_size = x + 1

            # Calculate how many groups of size 'group_size' are needed
            # to accommodate 'k' rabbits giving this answer.
            # We use ceiling division: ceil(k / group_size)
            # Integer arithmetic for ceiling: (k + group_size - 1) // group_size
            num_groups = (k + group_size - 1) // group_size

            # Each group contributes 'group_size' rabbits to the total count.
            total_rabbits += num_groups * group_size

            # Alternatively, using math.ceil:
            # num_groups = math.ceil(k / group_size)
            # total_rabbits += num_groups * group_size


        return total_rabbits