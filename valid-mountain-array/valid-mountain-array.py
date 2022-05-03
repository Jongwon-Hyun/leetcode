class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        result = True
        status = "up"
        if len(arr) < 3 or arr[1] < arr[0]:
            result = False
        else:
            for i in range(len(arr) - 1):
                if status == "up":
                    if arr[i + 1] > arr[i]:
                        continue
                    elif arr[i + 1] == arr[i]:
                        result = False
                        break
                    else:
                        status = "down"
                else:
                    if arr[i + 1] < arr[i]:
                        continue
                    else:
                        result = False
                        break

        if status == "up":
            result = False

        return result