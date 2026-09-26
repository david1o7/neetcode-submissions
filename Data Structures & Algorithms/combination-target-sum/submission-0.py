class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(remain, comb, start_point):
            if remain == 0:
                res.append(list(comb))

            if remain < 0:
                return
            
            for i in range(start_point, len(nums)):
                comb.append(nums[i])
                backtrack(remain - nums[i], comb, i)
                comb.pop()
        backtrack(target, [], 0)
        return res