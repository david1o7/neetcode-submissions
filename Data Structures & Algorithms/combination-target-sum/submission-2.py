class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(final_sum, comb, starting_point):
            if final_sum == 0:
                res.append(comb[:])
                return
            
            if final_sum < 0:
                return
            
            for i in range(starting_point, len(nums)):
                comb.append(nums[i])

                backtrack(final_sum - nums[i], comb, i)

                comb.pop()


        backtrack(target, [], 0)
        return res