class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total_time = 0
        
        for i in range(len(requests)-1):
            total_time += abs(requests[i] - requests[i+1])
        
        return total_time + requests[0] 