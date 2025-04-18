class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generates the nth term of the count-and-say sequence iteratively.

        Args:
            n: The term number (1-based).

        Returns:
            The nth term as a string.
        """
        if n == 1:
            return "1"

        current_s = "1" # Represents countAndSay(1)

        # Loop n-1 times to generate terms from 2 to n
        for _ in range(n - 1):
            next_s_parts = [] # Use a list for efficient building
            i = 0
            len_s = len(current_s)

            while i < len_s:
                current_char = current_s[i]
                count = 0
                # Find the end of the consecutive group
                j = i
                while j < len_s and current_s[j] == current_char:
                    count += 1
                    j += 1

                # Append the count (as string) and the character
                next_s_parts.append(str(count))
                next_s_parts.append(current_char)

                # Move the main pointer to the start of the next group
                i = j

            # Join the parts to form the next string
            current_s = "".join(next_s_parts)

        return current_s