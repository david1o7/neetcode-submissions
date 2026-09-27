class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(comb):
            nonlocal res
            if len(comb) == len(nums):
                res.append(list(comb))
                return

            for i in range(0, len(nums)):
                if nums[i] in visited:
                    continue
                
                comb.append(nums[i])
                visited.add(nums[i])

                backtrack(comb)

                comb.pop()
                visited.remove(nums[i])

        backtrack([])
        return res
