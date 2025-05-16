class Solution:
  def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
    n = len(words)
    # Constraints: 1 <= n <= 1000. So n is at least 1.

    # Helper function for Hamming distance.
    # It's called only when len(s1) == len(s2).
    def calculate_hamming_distance(s1: str, s2: str) -> int:
        dist = 0
        # Strings consist of lowercase English letters. Length is at most 10.
        for k in range(len(s1)): # len(s1) is fine as lengths are equal.
            if s1[k] != s2[k]:
                dist += 1
        return dist

    # dp[i] stores the length of the longest valid subsequence ending with words[i].
    dp = [1] * n
    # parent[i] stores the index of the word that comes before words[i]
    # in the longest valid subsequence ending with words[i].
    parent = [-1] * n # -1 indicates no predecessor (start of a subsequence).

    max_so_far_len = 1       # The maximum length found for any subsequence.
                             # Since n >= 1, there's always at least one word, so min length is 1.
    max_so_far_len_idx = 0   # The index of the last word in the longest subsequence found so far.
                             # Initialized to 0, as words[0] forms a subsequence of length 1.

    for i in range(n): # Current word words[i] is a potential end of a subsequence.
        # Try to extend a previous subsequence ending at words[j] (where j < i).
        for j in range(i):
            # Check condition 1: Groups must be different.
            if groups[j] == groups[i]:
                continue
            
            # Check condition 2: Words must have the same length.
            if len(words[j]) != len(words[i]):
                continue
            
            # Check condition 3: Hamming distance must be 1.
            if calculate_hamming_distance(words[j], words[i]) != 1:
                continue
            
            # If all conditions are met, words[j] can precede words[i].
            # Check if this forms a longer subsequence ending at words[i].
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
        
        # After checking all possible predecessors for words[i],
        # if the subsequence ending at words[i] is the longest found globally so far, update.
        if dp[i] > max_so_far_len:
            max_so_far_len = dp[i]
            max_so_far_len_idx = i

    # Reconstruct the longest subsequence using the parent array.
    # We start from the end of the longest subsequence (words[max_so_far_len_idx])
    # and backtrack to the beginning.
    
    # Pre-allocate list of the correct size for the result.
    longest_subsequence_words = [""] * max_so_far_len 
    
    current_idx_in_result_list = max_so_far_len - 1 # To fill from the end of the list.
    current_original_array_idx = max_so_far_len_idx    # Start with the last element of the chosen LIS.
    
    while current_original_array_idx != -1:
        longest_subsequence_words[current_idx_in_result_list] = words[current_original_array_idx]
        current_idx_in_result_list -= 1
        current_original_array_idx = parent[current_original_array_idx] # Move to the predecessor.
        
    return longest_subsequence_words