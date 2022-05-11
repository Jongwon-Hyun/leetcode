class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # simple, pythonic
#         aBinaryNum = int(a, 2)
#         bBinaryNum = int(b, 2)
        
#         sum = aBinaryNum + bBinaryNum
        
#         return bin(sum)[2:]

        # no pythonic
        def convertToDecimal(n: str) -> int:
            result = 0
            powNum = 0
            for i in range(len(n)- 1, -1, -1):
                result += int(n[i]) * (2 ** powNum)
                powNum += 1
            return result
                
        def convertToBinary(n: int) -> str:
            result = ""
            while n >= 2:
                mod = n % 2
                n = n // 2
                result += str(mod)
            result += str(n)
            return result[::-1]
        
        
        sum = convertToDecimal(a) + convertToDecimal(b)
      
        return convertToBinary(sum)
                