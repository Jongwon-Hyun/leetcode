class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        tmp = []
        if len(arr) < 2:
            result = [-1]
        else:
            for i in range(len(arr)):
                if i == len(arr) - 1:
                    result.append(-1)
                else:
                    tmp = arr[i + 1:]
                    maxNum = max(tmp)
                    result.append(maxNum)
                    tmp = []

        return result