class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumNums = sum(nums)
        leftSum = 0
        
        for i, num in enumerate(nums):
            if leftSum == sumNums - leftSum - num:
                return i
            leftSum += num
        
        return -1
                
            