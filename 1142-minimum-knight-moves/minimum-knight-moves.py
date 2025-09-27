class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Use symmetry: work in the first quadrant, x >= y >= 0
        x, y = abs(x), abs(y)
        # Knight moves
        steps = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]

        # Small, safe bounding box: we never need to wander far into negatives,
        # and going a bit beyond the target is fine.
        maxx, maxy = x + 2, y + 2
        q = deque()
        q.append((0, 0, 0))        # (cx, cy, distance)
        visited = set([(0, 0)])
        while q:
            cx, cy, d = q.popleft()
            if cx == x and cy == y:
                return d

            for dx, dy in steps:
                nx, ny = cx + dx, cy + dy
                # prune to first quadrant with a small buffer
                if -2 <= nx <= maxx and -2 <= ny <= maxy:
                    ax, ay = abs(nx), abs(ny)  # exploit symmetry
                    if (ax, ay) not in visited:
                        visited.add((ax, ay))
                        q.append((ax, ay, d + 1))
