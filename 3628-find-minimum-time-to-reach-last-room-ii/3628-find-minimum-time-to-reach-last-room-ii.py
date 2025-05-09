class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])

        # dist[r][c][parity] stores the minimum time to ARRIVE at (r, c)
        # parity = 0: even number of moves made (0, 2, 4...). Next move costs 1.
        # parity = 1: odd number of moves made (1, 3, 5...). Next move costs 2.
        dist = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]

        # Priority queue: (current_arrival_time, r, c, moves_parity)
        pq = []

        # Start at (0,0) at time t=0. 0 moves made, so parity is 0.
        dist[0][0][0] = 0 
        heapq.heappush(pq, (0, 0, 0, 0)) 

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while pq:
            current_arrival_time, r, c, current_moves_parity = heapq.heappop(pq)

            if current_arrival_time > dist[r][c][current_moves_parity]:
                continue
            
            # Determine cost of the NEXT move
            if current_moves_parity == 0: # 0, 2, 4... moves made. Next move is (1st, 3rd, 5th overall)
                actual_move_cost = 1
            else: # 1, 3, 5... moves made. Next move is (2nd, 4th, 6th overall)
                actual_move_cost = 2
            
            next_moves_parity = 1 - current_moves_parity

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < N and 0 <= nc < M:
                    # Departure time from (r,c) towards (nr,nc):
                    # Must be at/after current_arrival_time at (r,c) AND
                    # at/after moveTime[nr][nc] (constraint to start moving TO (nr,nc))
                    departure_time = max(current_arrival_time, moveTime[nr][nc])
                    
                    time_arrive_at_neighbor = departure_time + actual_move_cost

                    if time_arrive_at_neighbor < dist[nr][nc][next_moves_parity]:
                        dist[nr][nc][next_moves_parity] = time_arrive_at_neighbor
                        heapq.heappush(pq, (time_arrive_at_neighbor, nr, nc, next_moves_parity))
        
        ans = min(dist[N-1][M-1][0], dist[N-1][M-1][1])
        
        # The problem implies reachability. If not, one might return -1.
        return ans if ans != float('inf') else -1 