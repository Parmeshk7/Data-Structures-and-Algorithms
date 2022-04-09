#815. Bus Routes 
#Difficulty : Hard

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_and_buses = defaultdict(list)
        n = len(routes)
        for i in range(n):
            for j in routes[i]:
                stop_and_buses[j].append(i)
        #print(stop_and_buses)
        
        q = deque([source])
        visited_stops = set()
        visited_buses = set()
        visited_stops.add(source)
        ans = 0
        
        while q:
            size = len(q)
            for i in range(size):
                curr_stop = q.popleft()
                if curr_stop == target:
                    return ans
                
                
                for bus in stop_and_buses[curr_stop]:
                    if bus not in visited_buses:
                        for stop in routes[bus]:
                            if stop not in visited_stops:
                                q.append(stop)
                                visited_stops.add(stop)
                visited_buses.add(bus)
            ans += 1
            
        return -1
