from collections import defaultdict

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = defaultdict(list)
        
        for i in range(0, rowIndex + 1):
            triangle[i] = [1]
            
            if i > 1:
                for j in range(1, i):
                    triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                    
            if i > 0:
                triangle[i].append(1)
        
        return triangle[rowIndex]
    
