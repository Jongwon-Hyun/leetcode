class Solution:
    def sortedSquares(self, nums):
        squarted = [num ** 2 for num in nums]
        squarted.sort()
        return squarted
        