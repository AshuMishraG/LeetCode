class Solution:
  def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    adj = collections.defaultdict(list)
    in_degree = [0] * n

    # Build adjacency list and in-degrees
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    # dp[i][j] stores the max count of color j on a path ending at node i
    dp = [[0] * 26 for _ in range(n)]

    # Initialize queue for Kahn's algorithm
    queue = collections.deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    max_overall_color_value = 0
    processed_nodes_count = 0

    while queue:
        u = queue.popleft()
        processed_nodes_count += 1

        # Node u adds its color to paths ending at u
        color_u_idx = ord(colors[u]) - ord('a')
        dp[u][color_u_idx] += 1
        
        # Update the maximum color value found so far for any path
        # max(dp[u]) gives the highest frequency of any color for paths ending at u
        max_overall_color_value = max(max_overall_color_value, dp[u][color_u_idx]) 
        # Correction: The above line is subtly wrong. We need max over ALL colors in dp[u], not just the current node's color.
        # Example: path ...X->U. color(X)=A, color(U)=B. If path ...X has 3 'A's, dp[U] gets A_count=3 from X.
        # Then dp[U][B_idx] becomes 1. Max for path ...X->U is 3 (for A), not 1 (for B).
        # Correct way:
        current_path_max_freq = 0
        for count_in_dp_u in dp[u]:
            current_path_max_freq = max(current_path_max_freq, count_in_dp_u)
        max_overall_color_value = max(max_overall_color_value, current_path_max_freq)
        # A more Pythonic way for the above 3 lines:
        # max_overall_color_value = max(max_overall_color_value, max(dp[u]))


        # Propagate DP values to neighbors
        for v in adj[u]:
            for c_idx in range(26):
                # Paths ending at v (via u) can achieve counts from paths ending at u
                dp[v][c_idx] = max(dp[v][c_idx], dp[u][c_idx])
            
            in_degree[v] -= 1
            if in_degree[v] == 0: # If all predecessors of v are processed
                queue.append(v)
    
    # Cycle detection and result
    if processed_nodes_count < n:
        return -1  # A cycle was present
    else:
        return max_overall_color_value