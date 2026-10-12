class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(final_sub,comb, starting_point):
            if final_sub == 0:
                res.append(comb[:])
                return

            if final_sub < 0:
                return

            for i in range(starting_point, len(nums)):
                comb.append(nums[i])

                backtrack(final_sub - nums[i], comb, i)

                comb.pop()
            
        backtrack(target, [], 0)
        return res