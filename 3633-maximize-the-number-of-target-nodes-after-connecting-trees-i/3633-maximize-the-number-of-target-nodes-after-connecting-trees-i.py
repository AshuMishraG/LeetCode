class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        adj1 = [[] for _ in range(n)]
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)

        adj2 = [[] for _ in range(m)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Precompute distances in tree1
        dist1 = [[0] * n for _ in range(n)]
        for v in range(n):
            visited = [False] * n
            q = deque([(v, 0)])
            visited[v] = True
            while q:
                node, d = q.popleft()
                dist1[v][node] = d
                for neighbor in adj1[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((neighbor, d + 1))

        # Precompute distances in tree2
        dist2 = [[0] * m for _ in range(m)]
        for u in range(m):
            visited = [False] * m
            q = deque([(u, 0)])
            visited[u] = True
            while q:
                node, d = q.popleft()
                dist2[u][node] = d
                for neighbor in adj2[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((neighbor, d + 1))

        # Precompute max reachable in tree2 within k-1
        max_tree2_counts = [0] * m
        for u in range(m):
            count = 0
            for node in range(m):
                if dist2[u][node] <= (k - 1) if k >= 1 else -1:
                    count += 1
            max_tree2_counts[u] = count

        max_tree2 = max(max_tree2_counts) if m > 0 and k >= 1 else 0

        answer = []
        for v in range(n):
            count_tree1 = sum(1 for node in range(n) if dist1[v][node] <= k)
            answer.append(count_tree1 + (max_tree2 if k >= 1 else 0))

        return answer