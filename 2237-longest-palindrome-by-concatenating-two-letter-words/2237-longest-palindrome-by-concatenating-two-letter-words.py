class Solution:
  def longestPalindrome(self, words: List[str]) -> int:
    counts = collections.Counter(words)
    total_length = 0
    # Flag to track if a center piece (like "gg" from an odd count) is available
    odd_palindrome_found = False  

    for word, count in counts.items():
        # Case 1: Word is a palindrome itself (e.g., "aa", "bb")
        if word[0] == word[1]:
            # Add pairs of this word (e.g., "aa...aa")
            # Each pair uses two "aa" words and adds 4 to length
            total_length += (count // 2) * 4
            # If there's an odd one out, it can be a center
            if count % 2 == 1:
                odd_palindrome_found = True
        # Case 2: Word is not a palindrome (e.g., "ab")
        # Only process if word[0] < word[1] to ensure each pair ("ab", "ba") 
        # is considered once.
        # E.g., we process "ab" and find "ba". When "ba" is iterated later, 
        # 'b' is not less than 'a', so it's skipped.
        elif word[0] < word[1]:
            rev_word = word[1] + word[0]
            if rev_word in counts:
                # Number of "ab...ba" pairs we can form
                num_pairs = min(count, counts[rev_word])
                total_length += num_pairs * 4
        # else (word[0] > word[1], e.g. "ba"): This is the reverse of a word ("ab")
        # that would have been processed under the word[0] < word[1] condition.
        # So, we do nothing for this case.
        
    # If we found any palindromic word with an odd count (like a single "gg"),
    # we can place one such word in the center of our palindrome.
    if odd_palindrome_found:
        total_length += 2
            
    return total_length