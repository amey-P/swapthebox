#
#   Written by mananeey Shree. Amey bhau Patil
#
import sys
import copy
import rationalise
import itertools

max_depth = 0

def display(grid):
    print
    for row in grid:
        print
        for cell in row:
            if cell is 0:
                sys.stdout.write(' ')
                continue
            sys.stdout.write(cell)


def file_inp():
    grid = []
    f = open(raw_input("Name of the file to be loaded : "),'r')
    for line in f:
        grid.append([])
        line = line.strip('\n')
        for text in line:
            if text is '0':
                grid[-1].append(0)
                continue
            grid[-1].append(text)
    display(grid)
    if raw_input("\nPlease confirm layout (Y/N):") is 'y':
        max_depth = raw_input("\nThe grid must be solved in how many moves ? : ")
        rationalise.gravity(grid)
        return grid
    file_inp()


def get_grid():
    global max_depth
    grid = []
    print "Inflating Grid..."
    for a in range(9):
        grid.append([])
        for b in range(7):
            grid[a].append(0)

    print "\nDO NOT USE '0'(zero) !!!"
    for a in range(9):
        print
        for b in range(7):
            c = raw_input("Enter value for row {0}, column {1} :".format(a+1, b+1))
            if c=='':
                grid[a][b] = 0
            else:
                grid[a][b] = c
    max_depth = raw_input("\nThe grid must be solved in how many moves ? : ")
    print
    rationalise.gravity(grid)
    return grid

    
def permutate(grid,depth):
    depth+=1
    moves = [((a,b),(a+1,b)) for a in range(8) for b in range(7)]
    moves.extend([((a,b),(a,b+1)) for a in range(9) for b in range(6)])
    tmp_grid = []
    for move in moves:
        exp_grid = copy.deepcopy(grid)
        c = exp_grid[move[0][0]][move[0][1]]
        exp_grid[move[0][0]][move[0][1]] = exp_grid[move[1][0]][move[1][1]]
        exp_grid[move[1][0]][move[1][1]] = c
        while tmp_grid!=exp_grid:
            tmp_grid = copy.deepcopy(exp_grid)
            rationalise.gravity(exp_grid)
            rationalise.blow(exp_grid)
        if check_solved(exp_grid) is True:
            return move
        else:
            solution = [move]
            solution.extend(permutate(exp_grid,depth+1))
            return solution
    if depth is max_depth:
        return False


def check_solved(tmp_grid):
    for a in range(9):
        for b in range(7):
            if tmp_grid[a][b] != 0:
                return False
    return True
    

def main():
    print "Select input method : "
    print "1. Direct"
    print "2. File"
    response = raw_input()
    if response is '1':
        grid = get_grid()
    elif response is '2':
        grid = file_inp()
    else: main()
    ans = permutate(grid,0)
    if ans[-1] is False:
        print
        print "Couldn't solve"
    else:
        print
        print ans

    
if __name__ == '__main__':
    main()
