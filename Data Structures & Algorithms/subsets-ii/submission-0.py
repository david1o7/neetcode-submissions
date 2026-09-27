class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(comb, start_point):
            res.append(list(comb))

            for i in range(start_point, len(nums)):
                if i > start_point and nums[i] == nums[i-1]:
                    continue

                comb.append(nums[i])

                backtrack(comb, i + 1)

                comb.pop()
            
        backtrack([], 0)
        return res
                