class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric_count = 0
        for num in range(low, high + 1):
            if self.is_symmetric(num):
                symmetric_count += 1
        return symmetric_count

    def is_symmetric(self, n: int) -> bool:
        s = str(n)
        length = len(s)

        if length % 2 != 0:
            return False

        half_length = length // 2

        sum_first_half = 0
        for i in range(half_length):
            sum_first_half += int(s[i]) 

        sum_second_half = 0
        for i in range(half_length, length):
            sum_second_half += int(s[i])

        return sum_first_half == sum_second_half