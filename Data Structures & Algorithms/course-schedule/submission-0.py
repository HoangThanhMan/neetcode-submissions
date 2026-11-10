class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        mp = {i : [] for i in range(numCourses)}
        for i in range(len(prerequisites)):
            mp[prerequisites[i][0]].append(prerequisites[i][1])

        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if mp[c] == []:
                return True

            visited.add(c)
            for item in mp[c]:
                if not dfs(item):
                    return False
            visited.remove(c)
            mp[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            