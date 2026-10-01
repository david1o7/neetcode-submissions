class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current_path: list[str]):
            # Base case: if the current combination length equals the digits length
            if len(current_path) == len(digits):
                result.append("".join(current_path))
                return
                
            # Get the letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]
            
            # Loop through options, explore, and backtrack
            for letter in possible_letters:
                current_path.append(letter)
                backtrack(index + 1, current_path)
                current_path.pop()  # Backtrack step
                
        backtrack(0, [])
        return result
