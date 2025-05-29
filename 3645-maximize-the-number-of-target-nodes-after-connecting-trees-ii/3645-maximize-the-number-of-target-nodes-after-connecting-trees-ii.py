class Solution:
  def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
    n = len(edges1) + 1
    m = len(edges2) + 1

    adj1 = collections.defaultdict(list)
    for u, v in edges1:
      adj1[u].append(v)
      adj1[v].append(u)

    adj2 = collections.defaultdict(list)
    for u, v in edges2:
      adj2[u].append(v)
      adj2[v].append(u)

    def get_depths_and_parity_counts(num_nodes: int, adj: collections.defaultdict[int, list[int]], start_node: int = 0) -> tuple[list[int], int, int]:
      """
      Performs BFS to calculate depths and count nodes by depth parity.
      Returns (depths_list, even_depth_count, odd_depth_count).
      Assumes graph is connected (tree) and start_node is valid.
      Constraints num_nodes >= 2 ensure start_node=0 is valid and graph is non-trivial.
      """
      depths = [-1] * num_nodes
      
      q = collections.deque([(start_node, 0)]) # (node_index, depth_value)
      depths[start_node] = 0
      
      even_depth_count = 0
      odd_depth_count = 0
      
      while q:
        curr, d = q.popleft()

        if d % 2 == 0:
          even_depth_count += 1
        else:
          odd_depth_count += 1
        
        for neighbor in adj[curr]:
          if depths[neighbor] == -1: # If not visited
            depths[neighbor] = d + 1
            q.append((neighbor, d + 1))
            
      return depths, even_depth_count, odd_depth_count

    depths1, n1_even, n1_odd = get_depths_and_parity_counts(n, adj1, 0)
    # For T2, we only need the counts, not the full depths array for later steps.
    _, n2_even, n2_odd = get_depths_and_parity_counts(m, adj2, 0) 

    max_t2_contrib = max(n2_even, n2_odd)

    ans = [0] * n
    for i in range(n):
      t1_contrib = 0
      if depths1[i] % 2 == 0: # Node i in T1 has even depth
        t1_contrib = n1_even
      else: # Node i in T1 has odd depth
        t1_contrib = n1_odd
      
      ans[i] = t1_contrib + max_t2_contrib
            
    return ans