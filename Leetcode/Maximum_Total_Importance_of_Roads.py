#Maximum Total Importance of Roads


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = dict()
        for road in roads:
            degree[road[0]] = degree.get(road[0], 0) + 1
            degree[road[1]] = degree.get(road[1], 0) + 1
       
        values = [0]*n
        sorted_nodes = sorted(degree.items(), key=lambda x: x[1], reverse=True)
        val = n
        
        for pair in sorted_nodes:
            values[pair[0]] = val
            val -= 1
            
        importance = 0
        for u, v in roads:
            importance += values[u] + values[v]
        return importance
        
