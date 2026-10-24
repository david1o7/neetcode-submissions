class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        total_cost = 0 #cost of efficient path

        visited = [False] * n #some like a bloom filter for a visited friend

        friends_connected = 0 #keeping track of the number visited friends

        friends_coordInfo = [(0, 0)]

        while friends_connected < n:
            travel_cost, friend_location = heapq.heappop(friends_coordInfo)

            if visited[friend_location]:
                continue
            
            visited[friend_location] = True
            total_cost += travel_cost
            friends_connected += 1

            for nxt_friend in range(n):
                x1, y1 = points[friend_location]
                x2, y2 = points[nxt_friend]

                mah_dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(friends_coordInfo, (mah_dist, nxt_friend))

        return total_cost
