# Runtime: 724 ms
# Memory: 133.7 MB

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # print(adj)
        vis = [False] * (n)
        def dfs(node,component):
            vis[node] = True
            component.append(node)
            for neigh in adj[node]:
                if not vis[neigh]:
                    dfs(neigh,component)

        for i in range(n):
            if not vis[i]:
                component = []
                dfs(i,component)
                if source in component and destination in component:
                    return True
        return False
        