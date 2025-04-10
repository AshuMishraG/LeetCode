class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        s_val = int(s)
        len_s = len(s)
        pow10_len_s = 10**len_s

        @cache
        def dp(p_str, index, is_tight, is_leading):
            n = len(p_str)
            if index == n:
                return 1 

            upper = int(p_str[index]) if is_tight else 9
            res = 0
            for digit in range(min(upper, limit) + 1):
                new_tight = is_tight and (digit == upper)
                if is_leading and digit == 0:
                    res += dp(p_str, index + 1, new_tight, True)
                else:
                    res += dp(p_str, index + 1, new_tight, False)
            return res

        def count_limited_digits_0_to_P(P):
            if P < 0:
                return 0
            p_str = str(P)
            count = dp(p_str, 0, True, True)
            dp.cache_clear() 
            return count

        def solve(N_val):
            if N_val < s_val: 
                 return 0

            P_max = (N_val - s_val) // pow10_len_s

            count_0_to_Pmax = count_limited_digits_0_to_P(P_max)

            prefix_count_1_to_Pmax = max(0, count_0_to_Pmax - 1)

            total = prefix_count_1_to_Pmax

            if s_val <= N_val:
                 total += 1

            return total

        result_finish = solve(finish)
        result_start_minus_1 = solve(start - 1)

        return result_finish - result_start_minus_1