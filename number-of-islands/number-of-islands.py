class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        queue = []
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    queue.append((row,col))

                    while len(queue) != 0:
                        i,j = queue.pop(0)
                        grid[i][j] = "0"
                        
                        if i > 0 and grid[i - 1][j] == "1" and (i - 1,j) not in queue:
                            queue.append((i - 1,j))
                        if j > 0 and grid[i][j - 1] == "1" and (i,j - 1) not in queue:
                            queue.append((i,j - 1))
                        if i < len(grid) - 1 and grid[i + 1][j] == "1" and (i + 1,j) not in queue:
                            queue.append((i + 1,j))
                        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1" and (i,j + 1) not in queue:
                            queue.append((i,j + 1))
                    
                    count += 1
        
        return count
                        
                        
                        