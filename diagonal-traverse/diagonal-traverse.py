from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dic[i+j].append(mat[i][j])
        
        result = []
        for key, value in dic.items():
            if key % 2 == 0:
                value = value[::-1]
            
            result.extend(value)
        
        return result