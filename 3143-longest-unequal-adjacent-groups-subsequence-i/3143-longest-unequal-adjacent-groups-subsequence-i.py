class Solution:
  def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
    n = len(words)
    # According to constraints, n >= 1, so words is never empty.
    # words[0] and groups[0] are always safe to access.

    # This list will store the words of our selected subsequence.
    selected_words = []

    # The first word, words[0], can always start a valid subsequence.
    # So, we add it to our list and record its group.
    selected_words.append(words[0])
    last_selected_group = groups[0]

    # Iterate through the rest of the words, starting from the second word (index 1).
    for i in range(1, n):
      # Check if the current word's group (groups[i]) is different from the
      # group of the last word we added to our subsequence (last_selected_group).
      if groups[i] != last_selected_group:
        # If it's different, this word can extend our alternating subsequence.
        # So, we add it.
        selected_words.append(words[i])
        # And update last_selected_group to the current word's group.
        last_selected_group = groups[i]
    
    return selected_words