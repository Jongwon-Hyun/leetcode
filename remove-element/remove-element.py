class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for el in nums:
            if el != val:
                nums[cnt] = el
                cnt += 1
        return cnt