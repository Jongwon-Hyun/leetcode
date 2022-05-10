class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowNum = len(matrix)
        colNum = len(matrix[0])
        left, right, up, down = -1, colNum, -1, rowNum
        maxElementCnt = rowNum * colNum
        rowCur = 0
        colCur = 0
        result = []

        while True:
            # right
            while colCur < right:
                result.append(matrix[rowCur][colCur])
                colCur += 1

            if len(result) == maxElementCnt:
                break

            colCur -= 1
            rowCur += 1
            up += 1

            # down
            while rowCur < down:
                result.append(matrix[rowCur][colCur])
                rowCur += 1

            if len(result) == maxElementCnt:
                break

            rowCur -= 1
            colCur -= 1 
            right -= 1

            # left
            while colCur > left:
                result.append(matrix[rowCur][colCur])
                colCur -= 1

            if len(result) == maxElementCnt:
                break

            colCur += 1
            rowCur -= 1
            down -= 1

            # up
            while rowCur > up:
                result.append(matrix[rowCur][colCur])
                rowCur -= 1

            if len(result) == maxElementCnt:
                break

            rowCur += 1
            colCur += 1
            left += 1

        return result