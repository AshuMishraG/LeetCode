from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        # 1. Count the frequency of available digits
        input_counts = Counter(digits)
        result = []

        # 2. Iterate through all 3-digit even numbers
        for num in range(100, 1000, 2): # Start=100, End=999 (exclusive), Step=2 for even
            
            # 3. For each number, check if it can be formed
            
            # Get the digits required for the current number 'num'
            d1 = num // 100        # Hundreds digit
            d2 = (num // 10) % 10  # Tens digit
            d3 = num % 10          # Units digit
            
            # Count the frequency of digits required by 'num'
            required_counts = Counter([d1, d2, d3])
            
            # Check if we have enough digits in our input
            can_form_num = True
            for digit, required_count in required_counts.items():
                if input_counts[digit] < required_count:
                    can_form_num = False
                    break  # Not enough of this digit, cannot form the number
            
            # 4. If it can be formed, add it to the result
            if can_form_num:
                result.append(num)
                
        # 5. The result list is already sorted because we iterated in order.
        return result