class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        maxNum = max(nums)
        tmpNums = nums.copy()
        tmpNums.remove(maxNum)
        
        judge = [x for x in tmpNums if x * 2 > maxNum]
        
        if len(judge) > 0:
            return -1
        else:
            return nums.index(maxNum)