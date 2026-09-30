class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current_partition = []

        def palindrome(sub_str):
            return sub_str == sub_str[::-1]
        
        def backtrack(start_point):
            if start_point == len(s):
                res.append(list(current_partition))
                return
            
            for end_point in range(start_point + 1, len(s) + 1):
                substring = s[start_point:end_point]

                if palindrome(substring):
                    current_partition.append(substring)
                    backtrack(end_point)
                    current_partition.pop()

        backtrack(0)
        return res