class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = {i : [] for i in range(n)}
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in mp[node]:
                dfs(nei)

        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1

        return cnt