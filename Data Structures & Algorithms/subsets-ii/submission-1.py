class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def backtrack(comb, starting_point):
            res.append(comb[:])

            for i in range(starting_point, len(nums)):
                if i > starting_point and nums[i - 1] == nums[i]:
                    continue
                
                comb.append(nums[i])

                backtrack(comb, i + 1)

                comb.pop() 
            
        backtrack([], 0)
        return res
                