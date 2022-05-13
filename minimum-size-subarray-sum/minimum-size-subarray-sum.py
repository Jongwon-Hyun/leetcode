class Solution:
    def minSubArrayLen(self, target, nums):
        start = 0
        end = 0
        result = len(nums)
        
        if sum(nums) < target:
            return 0

        while start <= end and end < len(nums):
            num_sum = sum(nums[start:end + 1])
            
            if num_sum >= target:
                result = min(result,len(nums[start:end + 1]))
                start += 1
            elif num_sum < target:
                end += 1
                
        
        return result