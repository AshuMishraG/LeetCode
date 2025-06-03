class Solution:
  def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    n = len(status)
    
    total_candies_collected = 0
    
    # box_has_been_processed[i] is true if box i has been added to the queue.
    # This ensures candies are collected and contents processed only once.
    box_has_been_processed = [False] * n 
    
    # box_is_possessed[i] is true if we currently have box i (either from initialBoxes or found inside another box).
    box_is_possessed = [False] * n
    
    # box_is_open[i] is true if box i's initial status is open, OR we have found a key for it.
    # This array is dynamically updated when keys are found.
    box_is_open = [s == 1 for s in status]

    # Queue for BFS: stores indices of boxes that we possess, are open, and haven't been processed yet.
    bfs_q = collections.deque()

    # Initialize with initial boxes:
    # For each box in initialBoxes, we now possess it.
    # If it's also open and not yet processed, add it to the queue.
    for box_idx in initialBoxes:
        box_is_possessed[box_idx] = True
        # A box can be processed if:
        # 1. We possess it (box_is_possessed[box_idx] is True)
        # 2. It's open (box_is_open[box_idx] is True)
        # 3. It hasn't been processed yet (not box_has_been_processed[box_idx])
        if box_is_open[box_idx] and not box_has_been_processed[box_idx]:
            bfs_q.append(box_idx)
            box_has_been_processed[box_idx] = True # Mark as added to queue to prevent re-adding

    # Start BFS
    while bfs_q:
        current_box_idx = bfs_q.popleft()
        
        # Collect candies from the opened box
        total_candies_collected += candies[current_box_idx]

        # Process keys found in current_box_idx
        for key_for_specific_box_idx in keys[current_box_idx]:
            # We found a key for key_for_specific_box_idx. So, this box is now considered "openable".
            box_is_open[key_for_specific_box_idx] = True 
            
            # If we already possess this box (key_for_specific_box_idx), 
            # it's now open, and we haven't processed it yet, add it to the queue.
            if box_is_possessed[key_for_specific_box_idx] and not box_has_been_processed[key_for_specific_box_idx]:
                # box_is_open[key_for_specific_box_idx] is True due to the line above
                bfs_q.append(key_for_specific_box_idx)
                box_has_been_processed[key_for_specific_box_idx] = True
        
        # Process boxes contained in current_box_idx
        for new_found_box_idx in containedBoxes[current_box_idx]:
            # We now possess this new_found_box_idx.
            box_is_possessed[new_found_box_idx] = True
            
            # If this newly possessed box is open (either initially, or we found its key earlier)
            # and we haven't processed it yet, add it to the queue.
            if box_is_open[new_found_box_idx] and not box_has_been_processed[new_found_box_idx]:
                bfs_q.append(new_found_box_idx)
                box_has_been_processed[new_found_box_idx] = True
                
    return total_candies_collected