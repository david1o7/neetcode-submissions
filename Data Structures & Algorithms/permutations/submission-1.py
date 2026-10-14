class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        visited = set()

        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
                return

            for num in nums:
                if num in visited:
                    continue

                comb.append(num)
                visited.add(num)

                backtrack(comb)

                comb.pop()
                visited.remove(num)

        backtrack([])
        return res