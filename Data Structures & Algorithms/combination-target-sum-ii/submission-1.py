class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(remain, comb, start_point):
            nonlocal res
            if remain == 0:
                res.append(list(comb))
                return

            if remain < 0:
                return
            
            for i in range(start_point, len(candidates)):
                if i > start_point and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > remain:
                    break

                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i + 1)
                comb.pop()
            
        backtrack(target, [], 0)
        return res
            
            