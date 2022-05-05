class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddList = []
        evenList = []
        for num in nums:
            if num % 2 == 0:
                evenList.append(num)
            else:
                oddList.append(num)
        
        return evenList + oddList
                