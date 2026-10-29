# Runtime: 1 ms
# Memory: 19.4 MB

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        n = len(image)
        m = len(image[0])
        from collections import deque
        q = deque()
        q.append([image[sr][sc] , sr , sc])
        while q:
            node = q.popleft()
            pic = node[0]
            x = node[1]
            y = node[2]
            image[x][y] = color
            if x > 0 and image[x-1][y] == pic:
                image[x-1][y] = color
                q.append([pic , x-1 , y])
                
            if x + 1 < n and image[x+1][y] == pic:
                image[x+1][y] = color
                q.append([pic , x+1 , y])
                
            if y + 1 < m and image[x][y+1] == pic:
                image[x][y+1] = color
                q.append([pic , x , y+1])
                
            if y > 0 and image[x][y-1] == pic:
                image[x][y-1] = color
                q.append([pic , x , y-1])
        return image
                



        