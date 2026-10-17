class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        subset = []
        visited = set()

        def backtrack():
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                
                subset.append(nums[i])
                visited.add(nums[i])

                backtrack()

                subset.pop()
                visited.remove(nums[i])
        
        backtrack()
        return res



