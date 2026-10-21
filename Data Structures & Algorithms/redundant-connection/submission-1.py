class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        possible = [i for i in range(N + 1)]

        def find_boss(num):
            while num != possible[num]:
                num = possible[num]
            return num

        for u, v in edges:
            boss_of_u = find_boss(u)
            boss_of_v = find_boss(v)

            if boss_of_u == boss_of_v:
                return [u, v]

            possible[boss_of_u] = boss_of_v
