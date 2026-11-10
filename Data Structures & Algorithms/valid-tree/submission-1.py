class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        mp = {i : [] for i in range(n)}
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)

        visited = set()
        def dfs(node, prevNode):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in mp[node]:
                if nei == prevNode:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n