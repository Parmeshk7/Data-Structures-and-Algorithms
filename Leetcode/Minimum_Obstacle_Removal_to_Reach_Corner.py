#2290. Minimum Obstacle Removal to Reach Corner

# Approach : Dijkstra Algorithm to find Shortest Distance between (0,0) and (m-1, n-1)


class Solution:
    def dijkstra(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        minHeap = []
        visited = [[False]*n for i in range(m)]
        distance = [[math.inf]*n for i in range(m)]
        heappush(minHeap, (0, 0, 0))
        distance[0][0] = 0
        
        while minHeap:
            cost, i, j = heappop(minHeap)
            if visited[i][j]:
                continue
            visited[i][j] = True
            
            if j-1 >= 0:
                if distance[i][j-1] > cost+grid[i][j-1]:
                    distance[i][j-1] = cost + grid[i][j-1]
                    heappush(minHeap, (distance[i][j-1], i, j-1))
            if j+1 < n:
                if cost + grid[i][j+1] < distance[i][j+1]:
                    distance[i][j+1] = cost + grid[i][j+1]
                    heappush(minHeap, (distance[i][j+1], i, j+1))
            if i-1 >= 0:
                if cost + grid[i-1][j] < distance[i-1][j]:
                    distance[i-1][j] = cost + grid[i-1][j]
                    heappush(minHeap, (distance[i-1][j], i-1, j))
            if i+1 < m:
                if cost + grid[i+1][j] < distance[i+1][j]:
                    distance[i+1][j] = cost + grid[i+1][j]
                    heappush(minHeap, (distance[i+1][j], i+1, j))
            
        return distance[m-1][n-1]
                
            
        
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        return self.dijkstra(grid)
                
                
                
        
