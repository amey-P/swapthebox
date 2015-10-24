import copy

tmp_grid = []

def cycle(grid):
    tmp = deepcopy(grid)
    while True:
        gravity(grid)
        blow(grid)
        if tmp == grid:
            break
        tmp = copy.deepcopy(grid)

def gravity(grid):
    tmp_grid = copy.deepcopy(grid)
    for a in range(9):
        for b in range(7):
            if grid[a][b]!=0:
                try:
                    if grid[a+1][b] == 0:
                        grid[a+1][b] = grid[a][b]
                        grid[a][b] = 0
                except:
                    pass
    if grid != tmp_grid:
        gravity(grid)
    return 
    
def blow(grid):
    queue = []
    for a in range(9):
        for b in range(7):
            x = b+1
            y = a+1
            horizontal_counter = 0
            vertical_counter = 0
            while x<7:
                if grid[a][x] is grid[a][b]:
                    horizontal_counter += 1
                x+=1
            while y<9:
                if grid[y][b] is grid[a][b]:
                    vertical_counter += 1
                y+=1
            if horizontal_counter >= 3:
                queue.extend([(a,l) for l in range(b,b+4)])
            if vertical_counter >= 3:
                queue.extend([(l,b) for l in range(a,a+4)])
    for x in queue:
        grid[x[0]][x[1]] = 0
    return
