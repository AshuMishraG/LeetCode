class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        m = len(queries)

        if n == 0: # No numbers to zero out
            return m # All queries can be removed

        # 1. Pre-check feasibility: Can nums be zeroed using ALL queries?
        #    For each index i, nums[i] must be <= total queries covering i.
        max_coverage_at_idx_diff_array = [0] * (n + 1) # diff array for sweep line
        for l_query, r_query in queries:
            # Apply +1 at start of interval, -1 at end+1
            max_coverage_at_idx_diff_array[l_query] += 1
            if r_query + 1 <= n: # r_query+1 can be up to n
                max_coverage_at_idx_diff_array[r_query + 1] -= 1
        
        current_total_coverage = 0
        for i in range(n):
            current_total_coverage += max_coverage_at_idx_diff_array[i]
            if nums[i] > current_total_coverage:
                return -1 # Impossible to zero out nums[i]
        
        # Group queries by their start index for efficient access during sweep
        queries_starting_at_idx = [[] for _ in range(n)]
        for original_idx, (l_query, r_query) in enumerate(queries):
            # Storing (r_query, original_idx) to prioritize by r_query later
            queries_starting_at_idx[l_query].append((r_query, original_idx))

        num_chosen_queries = 0
        # Min-priority queue for right endpoints of active CHOSEN queries
        active_chosen_queries_min_pq = []  # Stores r_val
        # Max-priority queue for (r_val, query_id) of POTENTIAL (available, not-yet-chosen) queries
        # Implemented with min-heap storing (-r_val, query_id)
        potential_queries_max_pq = [] 

        # 2. Sweep line from left to right (index i)
        for i in range(n):
            # Add queries starting at current index i to potential_queries_max_pq
            for r_val, query_id in queries_starting_at_idx[i]:
                heapq.heappush(potential_queries_max_pq, (-r_val, query_id))
            
            # Remove chosen queries from active_chosen_queries_min_pq if they no longer cover i
            # (i.e., their r_val < i)
            while active_chosen_queries_min_pq and active_chosen_queries_min_pq[0] < i:
                heapq.heappop(active_chosen_queries_min_pq)
            
            # Lazily remove potential queries from potential_queries_max_pq if they no longer cover i
            # (i.e., their r_val < i)
            while potential_queries_max_pq and -potential_queries_max_pq[0][0] < i:
                heapq.heappop(potential_queries_max_pq)

            # Determine how many more queries need to be chosen for nums[i]
            current_provided_decrements = len(active_chosen_queries_min_pq)
            needed_decrements_for_nums_i = nums[i]
            
            shortfall = needed_decrements_for_nums_i - current_provided_decrements
            
            if shortfall > 0:
                for _ in range(shortfall):
                    # The pre-check guarantees that if shortfall > 0,
                    # potential_queries_max_pq will have enough valid queries.
                    if not potential_queries_max_pq:
                        # This state should not be reached if the logic and pre-check are correct.
                        # It implies an inconsistency or an impossible scenario missed by pre-check.
                        return -1 # Should indicate an error or impossible situation.
                    
                    # Select the available query that extends furthest to the right
                    neg_r_new, _ = heapq.heappop(potential_queries_max_pq) # query_id not needed further for this logic
                    r_new = -neg_r_new # Actual right endpoint
                    
                    heapq.heappush(active_chosen_queries_min_pq, r_new)
                    num_chosen_queries += 1
        
        # 3. Result: Max removable = Total - Min chosen
        return m - num_chosen_queries