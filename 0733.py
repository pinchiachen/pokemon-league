## 2022/10/20

## BFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set((sr, sc))
        value = image[sr][sc]
        image[sr][sc] = color
        queue = [[sr, sc]]
        m = len(image)
        n = len(image[0])
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        while len(queue) > 0:
            [x, y] = queue.pop(0)
            for [dx, dy] in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or (new_x, new_y) in visited:
                    continue
                visited.add((new_x, new_y))
                if image[new_x][new_y] == value:
                    queue.append([new_x, new_y])
                    image[new_x][new_y] = color
        return image