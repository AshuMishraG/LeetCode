class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        factorials = [1] * (n + 1)
        for i in range(2, n + 1):
            factorials[i] = factorials[i-1] * i

        def calculate_valid_permutations(counts_tuple, n, factorials):
            counts = list(counts_tuple)
            
            denominator = 1
            for count in counts:
                if factorials[count] == 0 and count > 0: return 0 
                denominator *= factorials[count]

            if denominator == 0: return 0 
            
            total_perms = factorials[n] // denominator

            if n > 1 and counts[0] > 0:
                denom_zero = factorials[counts[0] - 1]
                for i in range(1, 10):
                    if factorials[counts[i]] == 0 and counts[i] > 0 : return total_perms
                    denom_zero *= factorials[counts[i]]

                if denom_zero == 0:
                    perms_start_zero = 0
                else:
                    perms_start_zero = factorials[n - 1] // denom_zero
                    
                return total_perms - perms_start_zero
            else:
                return total_perms

        unique_digit_counts = set()
        
        half_n = (n + 1) // 2 
        start_half = 10**(half_n - 1) if n > 1 else 1 
        end_half = 10**half_n
        
        if n == 1:
            for p in range(1, 10):
                if p % k == 0:
                    counts = [0] * 10
                    counts[p] = 1
                    unique_digit_counts.add(tuple(counts))
        else:
            for h in range(start_half, end_half):
                s_h = str(h)
                
                if n % 2 == 1: 
                    s_p = s_h + s_h[:-1][::-1] 
                else: 
                    s_p = s_h + s_h[::-1] 
                
                p = int(s_p)
                if p % k == 0:
                    counts = [0] * 10
                    for digit in s_p:
                        counts[int(digit)] += 1
                    unique_digit_counts.add(tuple(counts))

        total_good_count = 0
        for counts_tuple in unique_digit_counts:
            total_good_count += calculate_valid_permutations(counts_tuple, n, factorials)
            
        return total_good_count