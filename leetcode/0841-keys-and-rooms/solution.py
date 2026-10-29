# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        from collections import deque
        n = len(rooms)
        vis = [False] * n
        q = deque([0])
        vis[0] = True
        while q:
            curr = q.popleft()
            for neigh in rooms[curr]:
                if not vis[neigh]:
                    vis[neigh] = True
                    q.append(neigh)
        for i in vis:
            if i==False:
                return False
        return True
                

        