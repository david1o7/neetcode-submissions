class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(final_sum, comb, starting_point):
            if final_sum == 0:
                res.append(comb[:])
                return

            if final_sum < 0:
                return
            
            for i in range(starting_point, len(candidates)):
                if i > starting_point and candidates[i] == candidates[i - 1]:
                    continue
                
                comb.append(candidates[i])

                backtrack(final_sum - candidates[i], comb, i + 1)

                comb.pop()

        backtrack(target, [], 0)
        return res