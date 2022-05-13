class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startIdx = 0
        endIdx = len(numbers) - 1
        
        while startIdx < endIdx:
            sum = numbers[startIdx] + numbers[endIdx]
            
            if sum == target:
                return [startIdx + 1, endIdx + 1]
            elif sum < target:
                startIdx += 1
            elif sum > target:
                endIdx -= 1