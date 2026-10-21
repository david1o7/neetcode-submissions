class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        galaxy_map = defaultdict(list)
        for u, v, w, in times:
            galaxy_map[u].append((v, w))

        fastest_time = {}

        omnitrix_brain = [(0, k)]

        while omnitrix_brain:
            current_time, current_base = heapq.heappop(omnitrix_brain)

            if current_base in fastest_time:
                continue
            
            fastest_time[current_base] = current_time

            for next_base, portal_time in galaxy_map[current_base]:
                if next_base not in fastest_time:

                    total_time = current_time + portal_time
                    heapq.heappush(omnitrix_brain, (total_time, next_base))


        if len(fastest_time) == n:
            return max(fastest_time.values())
        else:
            return -1 