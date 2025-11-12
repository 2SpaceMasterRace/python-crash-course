def numofIslands(grid: List[List[str]]) -> int:
    #INPUT: m x n 2D binary grid, 1 - land & 0 - water
    #OUTPUT: number of islands
    #NOTE: islands are connected horizontally and vertically, all four edges of the grid are surrounded by water

    if not grid:
        return 0

    def bfs(row,coloumn):
        queue = deque()
        visited.add((row,column))
        queue.append((row,coloumn))

        while queue:
            row, column = dequeue.popleft()
            directions = [[1,0],[-1,0], [0,1], [0,-1]]

        for dr, dc in directions:
            row,coloumn = row+dr, column+dc

            for(r in range(row) and c in range(column) and grid[r][c] == '1' and (r,c) is not visited):
                queue.append((r,c))
                visit.add((r,c))

    count = 0
    row = len(grid)
    coloumn = len(grid[0])
    visited = set()

    for r in range(row):
        for c in range(coloumn):
            if grid[r][c] == '1' and (r,c) not in visted:
                bfs(r,c)
                count += 1

    return count
