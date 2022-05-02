class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenCnt = 0
        for num in nums:
            digits = len(str(num))
            if digits % 2 == 0:
                evenCnt += 1
        return evenCnt