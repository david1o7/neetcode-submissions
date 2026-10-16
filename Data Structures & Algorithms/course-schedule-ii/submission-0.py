from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        alien_book = defaultdict(list)
        visited = [0] * numCourses

        for alien, prereq in prerequisites:
            alien_book[prereq].append(alien)
            visited[alien] += 1

        check_alien = deque()
        for i in range(numCourses):
            if visited[i] == 0:
                check_alien.append(i)

        saved_alien_order = []

        while check_alien:
            considering_alien = check_alien.popleft()
            saved_alien_order.append(considering_alien)

            for neighbor in alien_book[considering_alien]:
                visited[neighbor] -= 1

                if visited[neighbor] == 0:
                    check_alien.append(neighbor)

        if len(saved_alien_order) == numCourses:
            return saved_alien_order
        else :
            return []
    


