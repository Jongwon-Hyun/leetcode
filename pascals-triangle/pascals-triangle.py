class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        if numRows == 0:
            return([])
        if numRows == 1:
            return([[1]])
        elif numRows == 2:
            return([[1],[1,1]])
        else:
            result = [[1],[1,1]]
            for i in range(2, numRows):
                tmp = [1]
                for j in range(i - 1):
                    tmp.append(result[i - 1][j] + result[i - 1][j + 1])
                tmp.append(1)
                result.append(tmp)

        return result