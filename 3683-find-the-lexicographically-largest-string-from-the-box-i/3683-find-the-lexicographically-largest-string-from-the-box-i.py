class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)

        if numFriends == 1:
            # If only one friend, the word is split into 1 piece, which is the word itself.
            # The box contains only the original word.
            return word
        
        # For numFriends > 1:
        # Any piece w_j must have length L_j <= n - numFriends + 1.
        # Let max_allowed_len = n - numFriends + 1.
        # The set of all strings in the box is the set of all substrings of `word`
        # with length L such that 1 <= L <= max_allowed_len.
        # We need to find the lexicographically largest among these.
        
        # For any starting position i, consider substrings S_i,L = word[i:i+L].
        # If L1 < L2, then S_i,L1 is a prefix of S_i,L2.
        # Thus, S_i,L1 < S_i,L2 lexicographically.
        # So, for a fixed starting i, the largest candidate is the longest one
        # possible under the max_allowed_len constraint.
        
        max_allowed_len = n - numFriends + 1
        
        max_overall_substring = "" # Smallest possible string initially
        
        # Iterate through all possible starting positions for a substring
        for i in range(n):
            # Determine the length of the candidate substring starting at i.
            # It's the minimum of:
            # 1. Remaining length from index i to end of word (n - i)
            # 2. Max allowed length for a piece (max_allowed_len)
            current_len = min(n - i, max_allowed_len)
            
            # Extract the candidate substring
            # word[i : i + current_len]
            current_candidate = word[i : i + current_len]
            
            # If this candidate is non-empty (always true since current_len >= 1 unless n=0)
            # and larger than the current max, update.
            # An empty initial max_overall_substring takes care of the first candidate.
            if not max_overall_substring or current_candidate > max_overall_substring:
                max_overall_substring = current_candidate
                
        return max_overall_substring