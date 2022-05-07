class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinctNums = list(set(nums))
        
        if (len(distinctNums) < 3):
            return max(distinctNums)
        
        for i in range(2):
            del distinctNums[distinctNums.index(max(distinctNums))]
        
        return max(distinctNums)