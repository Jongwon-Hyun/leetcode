class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
# Formal
#         num = 0
#         for digit in digits:
#             num = num * 10 + digit
        
#         num += 1
        
#         result = []
#         while num > 0:
#             digit = num % 10
#             result.append(digit)
#             num = num // 10

#         result.reverse()
#         return result
        
        # simple
        num = int("".join(map(str, digits)))
        num += 1
        return [int(digit) for digit in str(num)]
        