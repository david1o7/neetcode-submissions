from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        alien_book = defaultdict(list)
        for alien, prereq in prerequisites:
            alien_book[alien].append(prereq)

        #0 for unvisit, 1 for checking(ben may have entered the loop), 2 for safe
        visited = [0] * numCourses

        def is_evil_loop(i):
            if visited[i] == 2:
                return False

            if visited[i] == 1:
                return True
            
            visited[i] = 1

            for prereq in alien_book[i]:
                if is_evil_loop(prereq):
                    return True
            
            visited[i] = 2
            return False

        for alien in range(numCourses):
            if is_evil_loop(alien):
                return False
        
        return True