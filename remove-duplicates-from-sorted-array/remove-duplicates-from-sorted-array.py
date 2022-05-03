class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            if nums[i] == nums[j]:
                del nums[j]
            else:
                i += 1
        return len(nums)