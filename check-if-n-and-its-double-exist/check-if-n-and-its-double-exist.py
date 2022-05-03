class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        j = 0
        result = False
        while i < len(arr):
            if i != j and arr[i] == arr[j] * 2:
                result = True
                break
            else:
                if j >= len(arr) - 1:
                    i += 1
                    j = 0
                    continue
                j += 1

        return result