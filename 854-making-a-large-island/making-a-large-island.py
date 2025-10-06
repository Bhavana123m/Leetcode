class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # If grid is empty, no area
        if grid is None or len(grid) == 0:
            return 0

        n = len(grid)

        # id_grid will store component ids (0 for water, >1 for island ids)
        id_grid = [[0] * n for _ in range(n)]
        # comp_size maps id -> size of that island
        comp_size = {}

        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # DFS to label an island and count its size
        def dfs(r, c, cid):
            # Stack to avoid recursion depth issues on large n (iterative DFS)
            stack = [(r, c)]
            id_grid[r][c] = cid
            count = 1

            # Process until the stack is empty
            while len(stack) > 0:
                cr, cc = stack.pop()

                # Explore all 4 neighbors
                k = 0
                while k < 4:
                    dr, dc = dirs[k]
                    nr = cr + dr
                    nc = cc + dc
                    # Check bounds and whether this neighbor is unvisited land
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1 and id_grid[nr][nc] == 0:
                            id_grid[nr][nc] = cid
                            count = count + 1
                            stack.append((nr, nc))
                    k = k + 1

            return count

        # First pass: label each island with a unique id and compute its size
        current_id = 2   # start ids from 2 so we can distinguish from 0/1 if needed
        r = 0
        max_existing = 0  # track the largest existing island size
        while r < n:
            c = 0
            while c < n:
                if grid[r][c] == 1 and id_grid[r][c] == 0:
                    # Label this island and get its size
                    size = dfs(r, c, current_id)
                    comp_size[current_id] = size
                    # Update max existing island size
                    if size > max_existing:
                        max_existing = size
                    current_id = current_id + 1
                c = c + 1
            r = r + 1

        # If there is no zero to flip (i.e., the entire grid is land), return n*n
        # Alternatively, if there are islands already, max_existing is their size
        # We'll compute the best possible flip below; but handle the all-ones early
        all_ones = (max_existing == n * n)
        if all_ones:
            return n * n

        # Second pass: consider flipping each zero and compute merged size
        best = max_existing  # even if we can't improve by flipping, this is valid
        r = 0
        while r < n:
            c = 0
            while c < n:
                if grid[r][c] == 0:
                    # Collect distinct neighbor component ids
                    neighbor_ids = set()

                    k = 0
                    while k < 4:
                        dr, dc = dirs[k]
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            cid = id_grid[nr][nc]
                            if cid > 1:  # it's a land cell belonging to component cid
                                # Use a set to avoid double-counting the same component
                                neighbor_ids.add(cid)
                        k = k + 1

                    # Sum sizes of distinct neighbors and add 1 for the flipped cell
                    merged = 1
                    # Iterate through ids in the set and add their sizes
                    for cid in neighbor_ids:
                        merged = merged + comp_size[cid]

                    # Update best if this flip gives a larger island
                    if merged > best:
                        best = merged
                c = c + 1
            r = r + 1

        return best