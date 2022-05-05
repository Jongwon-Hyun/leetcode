class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0 
        while i < len(nums):
            if nums[j] == 0:
                nums.append(nums[j])
                del nums[j]
                i += 1
            else:
                i += 1
                j += 1
                