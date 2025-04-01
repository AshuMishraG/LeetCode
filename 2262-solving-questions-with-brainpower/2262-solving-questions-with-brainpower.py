class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        dp = [0] * (n + 1) 

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            
            next_solvable_idx = min(n, i + brainpower + 1) 
            solve_option_points = points + dp[next_solvable_idx]
            
            skip_option_points = dp[i + 1]
            
            dp[i] = max(solve_option_points, skip_option_points)
            
        return dp[0]