class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(comb, open_count, close_count):
            if len(comb) == 2 * n:
                res.append(comb)
                return

            if open_count < n :
                backtrack(comb + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(comb + ")", open_count, close_count + 1)
            
        backtrack("", 0, 0)
        return res